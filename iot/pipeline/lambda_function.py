import json
import boto3

def lambda_handler(event, context):
    # S3 bucket and file details
    # bucket_name = 's33ding-termux'
    # file_key = 'iot/location/2023-09-24T00:20:44.598749.json'

    s3_event = event['Records'][0]['s3']
    bucket_name = s3_event['bucket']['name']
    file_key = s3_event['object']['key']
    
    # Initialize the S3 client
    s3_client = boto3.client('s4')

    try:
        # Get the JSON file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        json_data = response['Body'].read()

        # Parse the JSON data
        parsed_json = json.loads(json_data)

        # Do something with the JSON data
        # For example, print it
        print(parsed_json)

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error reading JSON data from S3')
        }

    try:
        # Upload JSON data to S3
        s3_client.put_object(Bucket="s33ding-kinesis", Key=file_key, Body=json_data)

        return {
            'statusCode': 200,
            'body': json.dumps('JSON data dumped to S3 successfully')
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error dumping JSON data to S3')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('JSON data read successfully')
    }
