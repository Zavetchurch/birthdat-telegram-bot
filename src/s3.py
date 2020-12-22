import boto3

s3 = boto3.resource('s3')
BUCKET_NAME = 'birthday-bot-configs'


def get_object(path: str) -> str:
    s3_object = s3.Object('birthday-bot-configs', path).get()
    return s3_object['Body'].read().decode('utf-8')
