#!/bin/bash

# Define the base password
base_password="M@g!c"

while true; do
    # Display the menu
    echo "Menu:"
    echo "1. Start EC2 Instances"
    echo "2. Stop EC2 Instances"
    echo "3. Exit"

    # Prompt the user for their choice
    read -p "Enter your choice (1/2/3): " choice

    case $choice in
        1)
            # Ask for the first three characters of the password
            read -p "Enter the first three characters of the password: " password_chars

            # Combine user input with the base password
            password="$password_chars$base_password"

            # Invoke the Lambda function to start EC2 instances with the password
            aws lambda invoke --function-name ec2_start --payload "{\"password\": \"$password\"}" response.json
            echo "Lambda function to start EC2 instances invoked."
            ;;
        2)
            # Ask for the first three characters of the password
            read -p "Enter the first three characters of the password: " password_chars

            # Combine user input with the base password
            password="$password_chars$base_password"

            # Invoke the Lambda function to stop EC2 instances with the password
            aws lambda invoke --function-name ec2_stop --payload "{\"password\": \"$password\"}" response.json
            echo "Lambda function to stop EC2 instances invoked."
            ;;
        3)
            # Exit the script
            echo "Exiting the script."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter 1, 2, or 3."
            ;;
    esac
done
