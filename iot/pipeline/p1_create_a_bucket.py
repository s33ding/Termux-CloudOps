import boto3
import sys
import logging

def create_s3_bucket_with_trigger_and_return_details(
        bucket_name,
        lambda_function_arn,
        event_type="s3:ObjectCreated:*",
        region="us-east-1"
    ):

    # Initialize the S3 and Lambda clients
    s3_client = boto3.client("s3", region_name=region)
    lambda_client = boto3.client("lambda", region_name=region)

    try:
        # Create an S3 bucket with the specified name
        s3_client.create_bucket(Bucket=bucket_name)

        # Define the Lambda function trigger configuration
        trigger_config = {
            "LambdaFunctionConfigurations": [
                {
                    "LambdaFunctionArn": lambda_function_arn,
                    "Events": [event_type],
                }
            ]
        }

        # Add the trigger to the S3 bucket
        s3_client.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration=trigger_config
        )

        # Get the Access Control List (ACL) for the bucket
        bucket_acl = s3_client.get_bucket_acl(Bucket=bucket_name)

        # Return a dictionary with bucket details
        bucket_details = {
            "BucketName": bucket_name,
            "BucketACL": bucket_acl.get("Grants"),
            "S3TriggerConfig": trigger_config,
        }

        return bucket_details

    except Exception as e:
        logging.error(f"Error creating S3 bucket with trigger: {str(e)}")
        return None

func_bucket_name = lambda: sys.argv[1] if len(sys.argv) > 1 else input(
    "Enter the bucket name: "
)

func_lambda_function_arn  = lambda: sys.argv[1] if len(sys.argv) > 1 else input(
    "Enter the lambda_function_arn: "
)

# Example usage:
if __name__ == "__main__":
    # Define lambda function to set default user name if not provided as an argument

    bucket_name = func_bucket_name()
    lambda_function_arn = func_lambda_function_arn()

    bucket_details = create_s3_bucket_with_trigger_and_return_details(
        bucket_name, 
        lambda_function_arn
    )
    
    if bucket_details:
        print("S3 Bucket Details:")
        print(f"Bucket Name: {bucket_details['BucketName']}")
        print("Bucket ACL:")
        for grant in bucket_details["BucketACL"]:
            print(grant)
        print("S3 Trigger Configuration:")
        print(bucket_details["S3TriggerConfig"])
