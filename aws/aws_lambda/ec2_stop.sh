import boto3
import os

region = 'us-east-1'
instances = ['i-0d8ac38ce91e29eb8']
ec2 = boto3.client('ec2', region_name=region)

# Get the correct password from the PASSWORD environment variable
correct_password = os.environ['PASSWORD']

def lambda_handler(event, context):
    # Get the password provided in the event payload
    provided_password = event.get('password', '')

    # Check if the provided password matches the correct password
    if provided_password == correct_password:
        # Stop the EC2 instances
        ec2.stop_instances(InstanceIds=instances)

        # Construct a response message
        response_message = 'Stopped your instances: ' + str(instances)
    else:
        # If the password is incorrect, return an error message
        response_message = 'Incorrect password. Instance not stopped.'

    # Return the response
    return {
        'statusCode': 200,  # You can set an appropriate status code
        'body': response_message
    }

