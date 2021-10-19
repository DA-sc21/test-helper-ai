import boto3
import json
import os
from dotenv import load_dotenv
load_dotenv()

def detect_text(bucket,path,studentID):

    client=boto3.client('rekognition')
    
    image = {'S3Object':{'Bucket':bucket,'Name':path}}
    response = client.detect_text(Image=image)

    correct = False 
    for textDetail in response['TextDetections']:
        # print(json.dumps(textDetail, indent=4, sort_keys=True))
        # print("DetectedText : " + str(textDetail['DetectedText']))
        # print("Confidence: " + str(textDetail['Type']))
        if studentID == str(textDetail['DetectedText']) :
            correct= True
            break

    return correct
    
def main():
    bucket="testhelper"
    path="test/" + os.environ['S3_TEMP_TEST'] + "/submission/" + os.environ['S3_TEMP_STUDENT'] + "/student_card.jpg"
    student_id=os.environ['STUDENT_ID']
    response =detect_text(bucket,path, student_id)
    if response :
        print("Result : True")
    else :
        print("Result : False")


if __name__ == "__main__":
    main()

