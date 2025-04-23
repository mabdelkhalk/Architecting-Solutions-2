import boto3

def create_sns_topic():
    sns = boto3.client('sns')
    response = sns.create_topic(Name='MyTopic')
    
    print(f"Topic ARN: {response['TopicArn']}")
