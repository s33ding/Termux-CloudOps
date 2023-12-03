import sys
from shared_func.create_boto3_session_from_json import create_boto3_session
from shared_func.dynamo_func import *
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

def calculate_confusion_matrix(df):
    # Create a column 'predicted' to indicate whether RealAge is within the range
    df["predicted"] = (df["RealAge"] >= df["LowerAge"]) & (df["RealAge"] <= df["UpperAge"])

    # Create a column 'ActualLabel' to convert RealAge to binary labels based on the range
    df['ActualLabel'] = df.apply(lambda row: row['LowerAge'] <= row['RealAge'] <= row['UpperAge'], axis=1)

    # Create a column 'PredictedLabel' to convert the 'predicted' column to binary labels
    df['PredictedLabel'] = df['predicted']

    # Initialize variables for confusion matrix
    true_positive = ((df['ActualLabel'] == True) & (df['PredictedLabel'] == True)).sum()
    true_negative = ((df['ActualLabel'] == False) & (df['PredictedLabel'] == False)).sum()
    false_positive = ((df['ActualLabel'] == False) & (df['PredictedLabel'] == True)).sum()
    false_negative = ((df['ActualLabel'] == True) & (df['PredictedLabel'] == False)).sum()

    # Create a confusion matrix DataFrame
    confusion_matrix_df = pd.DataFrame({
        'Predicted False': [false_positive, true_negative],
        'Predicted True': [true_positive, false_negative]
    }, index=['Actual False', 'Actual True'])

    return confusion_matrix_df

# Initialize the Amazon DynamoDB client
session = create_boto3_session()

# Example usage:
table_name = 'FaceAnalysis'

df = dynamodb_to_dataframe(table_name)
df = df[["AgeRange", "RealAge"]]
df[['LowerAge', 'UpperAge']] = df['AgeRange'].str.extract(r'(\d+) to (\d+) years old').astype(int)

# Calculate the confusion matrix using the function
confusion_matrix_df = calculate_confusion_matrix(df)

print("Confusion Matrix:")
print(confusion_matrix_df)


# Drop unnecessary columns
df.drop(columns=["AgeRange", "predicted", "ActualLabel", "PredictedLabel"], inplace=True)

