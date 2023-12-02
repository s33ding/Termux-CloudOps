import boto3


def face_analyze(bucket_name, key_name):
    # Initialize the Amazon Rekognition client
    print(f's3://{bucket_name}/{key_name}')
    rekog = boto3.client('rekognition')

    try:
        # Call the DetectFaces API to analyze the image for facial features
        response = rekog.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': key_name
                }
            },
            Attributes=['ALL']
        )
        print("response:")
        print(response)

        
        # Check if a face was detected in the image
        if len(response['FaceDetails']) == 1:
            face_detail = response['FaceDetails'][0]
            face_data = {
                'AgeRange': f"{face_detail['AgeRange']['Low']} to {face_detail['AgeRange']['High']} years old",
                'Gender': face_detail['Gender']['Value'],
                'Smile': face_detail['Smile']['Value'],  # True if smiling, False if not
                'EyesOpen': face_detail['EyesOpen']['Value'],  # True if eyes open, False if closed
                'Beard': face_detail['Beard']['Value'],  # True if beard present, False if not
                'Mustache': face_detail['Mustache']['Value'],  # True if mustache present, False if not
                'Sunglasses': face_detail['Sunglasses']['Value'],  # True if wearing sunglasses, False if not,

            }
            
            for emotion in face_detail['Emotions']:
                face_data[emotion['Type']] = emotion['Confidence']
                
            return face_data
            
        else:
            return None  # No face detected or multiple faces detected

    except Exception as e:
        print('An error occurred:', str(e))
