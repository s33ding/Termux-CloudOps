#!/bin/bash

# Step 1: Update and upgrade Termux packages
pkg update -y
pkg upgrade -y

# Step 2: Install Python and Pip
pkg install -y python

# Step 3: Install Pip
pkg install -y python-pip

# Step 4: Install AWS CLI using Pip
pip install awscli

# Step 5: Configure AWS CLI
aws configure

# Step 6: Verify installation
aws s3 ls

# Check if Git is installed
if ! git --version >/dev/null 2>&1; then
    echo "Git not found. Installing Git..."
    pkg install -y git
fi

# Step 7: Install Vim and SSH
pkg install -y vim openssh

echo "AWS CLI installation and configuration completed."

# Additional tools for SSH or customizations can be added here

pkg install busybox termux-services -y
pkg install jq -y


passwd

pkg update -y
pkg upgrade -y

echo "Restarting Termux..."
exit
