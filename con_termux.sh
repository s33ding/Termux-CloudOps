#!/bin/bash

# Specify the path to the JSON file
JSON_FILE=$TERMUX_CRED

# Check if the JSON file exists
if [ ! -f "$JSON_FILE" ]; then
  echo "Oops! The JSON file '$JSON_FILE' seems to be missing."
  exit 1
fi

# Parse JSON using jq (make sure jq is installed)
HOST_NAME=$(jq -r .hostname "$JSON_FILE")
USER=$(jq -r .username "$JSON_FILE")
PASSWORD=$(jq -r .password "$JSON_FILE")
PORT=$(jq -r .port "$JSON_FILE")

# Display connection information with excitement
echo "Exciting Connection Time! 🚀"
echo "---------------------------------"
echo "Ready to connect to the host:"
echo "🌐 Hostname: $HOST_NAME"
echo "👤 Username: $USER"
echo "🔌 Port: $PORT"
echo "---------------------------------"

# Get ready for action with an SSH command
echo "Get ready for the thrill! Here's your SSH command:"
echo "💻 ssh $USER@$HOST_NAME -p $PORT"

# Perform SSH connection using the retrieved values
sshpass -p "$PASSWORD" ssh "$USER"@"$HOST_NAME" -p "$PORT"

