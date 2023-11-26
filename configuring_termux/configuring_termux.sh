#!/bin/bash

# Update and upgrade Termux packages
pkg update -y
pkg upgrade -y

# Install Python and Pip
pkg install -y python

# Install Pip
pkg install -y python-pip

# Install AWS CLI using Pip
pip install awscli

# Configure AWS CLI
aws configure

# Verify installation
aws s3 ls

# Check if Git is installed
if ! git --version >/dev/null 2>&1; then
    echo "Git not found. Installing Git..."
    pkg install -y git
fi

# Install Vim and SSH
pkg install -y vim openssh

echo "AWS CLI installation and configuration completed."

# Additional tools for SSH or customizations can be added here

pkg install busybox termux-services -y
pkg install jq -y
pkg install htop

# Changing the passoword
passwd

# Updating the new softwares
pkg update -y
pkg upgrade -y

echo "Restarting Termux..."
exit
