#!/bin/bash

# Specify the path to the JSON file
JSON_FILE=$TERMUX_CRED

# Check if the JSON file exists
if [ ! -f "$JSON_FILE" ]; then
  echo "JSON file '$JSON_FILE' not found."
  exit 1
fi

# Parse JSON using jq (make sure jq is installed)
HOST_NAME=$(jq -r .hostname "$JSON_FILE")
USER=$(jq -r .username "$JSON_FILE")
PASSWORD=$(jq -r .password "$JSON_FILE")

echo "connecting to $HOST_NAME as $USER!"

# Perform SSH connection using the retrieved values
sshpass -p "$PASSWORD" ssh "$USER"@"$HOST_NAME" -p 8022

