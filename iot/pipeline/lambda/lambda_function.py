import json
import boto3
from s3_objects import *
from rekognition_func import *
import pandas as p
from dynamo_func import *
from decimal import Decimal

def extract_name_and_age(s3_object_key):
    # Split the S3 object key by '/' to get the file name
    file_name = s3_object_key.split('/')[-1]

    # Extract name and age from the file name
    name, age_str = file_name.split('-')

    # Convert age string to an integer
    age = int(age_str.split('.')[0])

    return name, age


def lambda_handler(event, context):

    # Assuming that the S3 event has a key
    s3_object_key = event['Records'][0]['s3']['object']['key']
    bucket_name = "s33ding-termux"
    
    # Call the extract_name_and_age function to get name and age
    name, age = extract_name_and_age(s3_object_key)
    
    res = face_analyze(
        bucket_name = bucket_name ,
        key_name = s3_object_key 
        )

    res["RealAge"] = age
    res["PersonName"] = name
    
    # Serialize the dictionary to a JSON-formatted string
    json_data = json.dumps(res)
  
      # Parse the JSON string with Decimal support
    data = json.loads(json_data, parse_float=Decimal)
  
    # Insert the sample data into the DynamoDB table
    insert_into_dynamodb("FaceAnalysis", data)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }