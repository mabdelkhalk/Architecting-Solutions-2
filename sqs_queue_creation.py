import boto3

def create_sqs_queue():
    sqs = boto3.client('sqs')
    
    response = sqs.create_queue(QueueName='MyQueue')
    
    print(f"Queue URL: {response['QueueUrl']}")
