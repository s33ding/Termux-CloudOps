import subprocess
import json
import boto3
import string
import secrets

def create_iam_role(role_name=None, policy_file=None, description=None):

    # AWS CLI command to create the IAM role
    command = [
        "aws", "iam", "create-role",
        "--role-name", role_name,
        "--description", description,
        "--assume-role-policy-document", f"file://{policy_file}"
    ]

    # Execute the AWS CLI command and capture the output
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout
        # Parse the JSON output to extract the ARN
        role_info = json.loads(output)
        role_arn = role_info["Role"]["Arn"]
        return role_arn
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def create_iam_policy(policy_name=None, policy_document_file=None):

    # AWS CLI command to create the IAM policy
    command = [
        "aws", "iam", "create-policy",
        "--policy-name", policy_name,
        "--policy-document", f"file://{policy_document_file}"
    ]

    # Execute the AWS CLI command and capture the output
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout
        # Parse the JSON output to extract the ARN
        policy_info = json.loads(output)
        policy_arn = policy_info["Policy"]["Arn"]
        return policy_arn

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def attach_policy_to_role(role_name, policy_arn):
    # AWS CLI command to attach a policy to an IAM role
    command = [
        "aws", "iam", "attach-role-policy",
        "--role-name", role_name,
        "--policy-arn", policy_arn
    ]

    # Execute the AWS CLI command
    try:
        subprocess.run(command, check=True)
        print(f"Policy ARN '{policy_arn}' attached to IAM Role '{role_name}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def attach_policy_to_user(user_name, policy_arn):
    # AWS CLI command to attach a policy to an IAM user
    command = [
        "aws", "iam", "attach-user-policy",
        "--user-name", user_name,
        "--policy-arn", policy_arn
    ]

    # Execute the AWS CLI command
    try:
        subprocess.run(command, check=True)
        print(f"Policy ARN '{policy_arn}' attached to IAM User '{user_name}' successfully.")
        return user_name
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def create_iam_user(username):
    # Create an IAM client
    iam = boto3.client('iam')

    # Create the IAM user
    iam.create_user(UserName=username)
    print(f"IAM User '{username}' created.")

def generate_random_password(length=20):
    # Define the character set for the password
    password_chars = string.ascii_letters + string.digits  

    # Generate a random password
    password = ''.join(secrets.choice(password_chars) for i in range(length))

    return password

def enable_login_profile(username):
    # Create an IAM client
    iam = boto3.client('iam')

    # Generate a random password
    password = generate_random_password()

    # Check if the login profile already exists
    try:
        existing_profile = iam.get_login_profile(UserName=username)
        print(f"Login profile for '{username}' already exists.")
        
        # Get the AWS account ID
        account_id = boto3.client('sts').get_caller_identity()['Account']
        
        # Provide a link to the AWS Management Console login page
        login_url = f"https://{account_id}.signin.aws.amazon.com/console"
        
        iam.update_login_profile(UserName=username, Password=password, PasswordResetRequired=False)
        print(f"Login profile for '{username}' updated with a new random password.")
        return password, login_url
    except iam.exceptions.NoSuchEntityException:
        pass  # Continue to create a new login profile


    # Create or update the login profile with the random password
    try:
        iam.create_login_profile(UserName=username, Password=password, PasswordResetRequired=True)
        print(f"Login profile for '{username}' enabled with a random password.")
        
        # Get the AWS account ID
        account_id = boto3.client('sts').get_caller_identity()['Account']
        
        # Provide a link to the AWS Management Console login page
        login_url = f"https://{account_id}.signin.aws.amazon.com/console"
        
    except iam.exceptions.EntityAlreadyExistsException:
        iam.update_login_profile(UserName=username, Password=password, PasswordResetRequired=False)
        print(f"Login profile for '{username}' updated with a random password.")
        
        # Get the AWS account ID
        account_id = boto3.client('sts').get_caller_identity()['Account']
        
        # Provide a link to the AWS Management Console login page
        login_url = f"https://{account_id}.signin.aws.amazon.com/console"

    return password, login_url


def delete_user(username):
    # Create an IAM client
    iam = boto3.client('iam')

    # List attached policies for the IAM user
    try:
        attached_policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
        for policy in attached_policies:
            # Detach each policy from the user
            iam.detach_user_policy(UserName=username, PolicyArn=policy['PolicyArn'])
            print(f"Detached policy '{policy['PolicyName']}' from '{username}' successfully.")
    except iam.exceptions.NoSuchEntityException:
        print(f"IAM user '{username}' does not exist or has no attached policies.")

    # Delete the login profile
    try:
        iam.delete_login_profile(UserName=username)
        print(f"Login profile for '{username}' deleted successfully.")
    except iam.exceptions.NoSuchEntityException:
        print(f"Login profile for '{username}' does not exist.")

    # Delete the IAM user
    try:
        iam.delete_user(UserName=username)
        print(f"IAM user '{username}' deleted successfully.")
    except iam.exceptions.NoSuchEntityException:
        print(f"IAM user '{username}' does not exist.")

def list_users():
    # Create an IAM client
    iam = boto3.client('iam')

    # List all IAM users
    response = iam.list_users()

    # Extract and print user names
    if 'Users' in response:
        users = response['Users']
        if users:
            print("IAM Users:")
            for user in users:
                print(user['UserName'])
        else:
            print("No IAM users found.")
    else:
        print("No IAM users found.")

def get_account_id():
    sts = boto3.client('sts')
    response = sts.get_caller_identity()
    return response['Account']

def list_roles():
    # Initialize a Boto3 IAM client
    iam_client = boto3.client('iam')

    # List all IAM roles
    try:
        response = iam_client.list_roles()
        roles = response['Roles']
        
        if roles:
            print("IAM Roles:")
            for role in roles:
                print(f"Role Name: {role['RoleName']}")
                print(f"Role ARN: {role['Arn']}")
                print("-" * 30)

        else:
            print("No IAM roles found.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
