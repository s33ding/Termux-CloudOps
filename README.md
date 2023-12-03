# Exploring Android Resources with Linux Terminal for Storing Data in AWS Cloud

Course: Data Science and AI.
Subject: Integrative Project 4.
Professor: Sérgio da Costa Côrtes.
Student: Roberto Moreira Diniz

## Introduction
In the field of data engineering, my project delves into a distinctive intersection: the combination of data from Android smartphone sensors with cloud technology. My main objectives encompass understanding how to leverage mobile sensor data and achieve integration with cloud services, with an emphasis on building effective data pipelines.

### General Diagram of the Assembled Pipeline

## Project Overview
Key components of the project:
1. We begin by collecting sensor data using Termux-API on an Android device.
2. Next, we use Python with the Boto3 library to send this data in JSON format to S3, AWS's storage system.
3. AWS Lambda, code functions triggered by S3 events, in this case, responsible for processing the files and storing this information in a database system called DynamoDB.

## Challenges
In my journey, I encountered significant challenges in seeking solutions to operate a system that combines sensor data, the Linux system, cloud infrastructure, data visualization tools, and information security. To achieve this, I implemented:
- Identity and Access Management (IAM) policies.

### AWS IAM Operational Mechanism Diagram

- Efficient data pipelines with data processing using serverless AWS Lambda.

### S3 to DynamoDB Data Pipeline Diagram

- Proficiency in the Linux operating system, SSH protocol, bash scripts, and package installation and network systems.


- Integration and management of AWS resources through the software development kit (SDK) with Boto3 using Python.


## Results
Although my project is still ongoing, I am excited to highlight the significant advancements I have achieved independently. Besides my initial findings on connecting to the operating system of my mobile device, I gained control over a wide range of sensors, including biometric identification, camera, battery, and GPS, using open-source software called Termux-API. This expansion enriched my data collection and analysis capabilities. Additionally, I gained effective control over the resources of my personal AWS account, such as EC2 instances, directly from my mobile device using a software development kit (SDK) called Boto3, built in Python. Furthermore, my application was designed to work continuously through mobile internet connectivity, thanks to the use of Boto3, which surpasses the limitation of SSH, which only works on local networks. This means I can continuously send data to the cloud using my mobile data, regardless of my geographical location.

## Expectations and Contributions
- Valuable learning experience in the field of data engineering, especially in the context of cloud pipeline construction.
- Continuous exploration of Android sensor data in future projects.


## Conclusion
In conclusion, our journey through the integration of sensor data, cloud, and visualization is challenging and rewarding. We have seen how these diverse technologies can come together to solve real-world problems. Considering the need to connect things to cloud resources, where data continues its path using different technologies and tools in its pipelines, it is increasingly important to know these tools to stand out in the job market.

