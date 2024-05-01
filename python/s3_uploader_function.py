"""A simple Amazon CloudFormation helper function to upload files to Amazon S3."""

import json
import urllib.request
import boto3

def send_response(event, context, response_status, response_data):
    """Send a signal back to Amazon CloudFormation."""
    response_body = json.dumps({
        "Status": response_status,
        "Reason": "See the details in CloudWatch Log Stream: " + context.log_stream_name,
        "PhysicalResourceId": context.log_stream_name,
        "StackId": event['StackId'],
        "RequestId": event['RequestId'],
        "LogicalResourceId": event['LogicalResourceId'],
        "Data": response_data
    })

    headers = {
        'content-type': '',
        'content-length': str(len(response_body))
    }

    response_request =
        urllib.request.Request(
            event['ResponseURL'],
            method='PUT',
            data=response_body.encode('utf-8'),
            headers=headers
        )
    with request.urlopen(response_request) as response:
        print("Status code:", response.getcode())
        print("Status message:", response.msg)

def lambda_handler(event, context):
    """A simple Amazon CloudFormation helper function to upload files to Amazon S3."""

    try:
        # Log the entire event and context objects
        print("Event: ", json.dumps(event))
        print("Context: ", context)

        s3 = boto3.client('s3')
        bucket_name = event['ResourceProperties']['BucketName']
        url = event['ResourceProperties']['HtmlFileUrl']

        with urllib.request.urlopen(url) as response:
            data = response.read()

        # Store the data in S3.
        s3.put_object(
            Bucket=bucket_name,
            Key='calculator-page.html',
            Body=data,
            ContentType='text/html'
        )

        send_response(event, context, "SUCCESS", {"Message": "Resource creation successful"})

    except Exception as e:
        print("Failed to process:", e)
        send_response(event, context, "FAILED", {"Message": str(e)})
