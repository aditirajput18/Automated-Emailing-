import boto3
import csv
import json
import os
import urllib.parse

s3 = boto3.client('s3')
ses = boto3.client('ses')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket']
        file_key = body['file']
        subject = body['subject']
        message = body['message']

        local_path = '/tmp/recipients.csv'
        s3.download_file(bucket_name, file_key, local_path)

        with open(local_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                recipient = row[0].strip()
                if recipient:
                    ses.send_email(
                        Source=os.environ['SENDER_EMAIL'],
                        Destination={'ToAddresses': [recipient]},
                        Message={
                            'Subject': {'Data': subject},
                            'Body': {'Text': {'Data': message}}
                        }
                    )

        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'Emails sent successfully!'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
