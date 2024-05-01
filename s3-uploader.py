"""A simple Amazon CloudFormation helper function to upload files to Amazon S3."""

import json
import urllib.request
import boto3

def lambda_handler(event, context):
    """A simple Amazon CloudFormation helper function to upload files to Amazon S3."""

    # Log the entire event and context objects
    print("Event: ", json.dumps(event))  # Convert the event dictionary to a JSON formatted string and print
    print("Context: ", context)          # The context object is not serializable to JSON directly without custom handling

    # Setup the S3 SDK client
    s3 = boto3.client('s3')
    bucket_name = event['ResourceProperties']['BucketName']
    
    # Open the URL
    url = event['ResourceProperties']['HtmlFileUrl']
    response = urllib.request.urlopen(url)
    data = response.read()
    
    # Store the data in S3.
    s3.put_object(Bucket=bucket_name, Key='calculator-page.html', Body=data, ContentType='text/html')
    
    return {'PhysicalResourceId': event.get('PhysicalResourceId', 'HtmlUploaderLambda')}
  