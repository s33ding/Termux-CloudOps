import boto3
import os

region = 'us-east-1'
instances = ['i-0d8ac38ce91e29eb8']
ec2 = boto3.client('ec2', region_name=region)

# Define the correct password
correct_password = os.environ['PASSWORD']  # Replace with your actual password

def lambda_handler(event, context):
    # Get the password provided in the event payload
    provided_password = event.get('password', '')

    # Check if the provided password matches the correct password
    if provided_password == correct_password:
        # Start the EC2 instances
        ec2.start_instances(InstanceIds=instances)

        # Get the instance information to retrieve the IP address
        response = ec2.describe_instances(InstanceIds=instances)
        
        # Extract the IP address from the response
        instance_info = response['Reservations'][0]['Instances'][0]
        ip_address = instance_info['PublicIpAddress']

        # Construct a response message with the IP address
        response_message = f'Started your instances: {instances}\nIP Address: {ip_address}'
    else:
        # If the password is incorrect, return an error message
        response_message = 'Incorrect password. Instance not started.'

    # Return the response
    return {
        'statusCode': 200,  # You can set an appropriate status code
        'body': response_message
    }
