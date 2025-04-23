import boto3
import json

def create_iam_policy():
    iam = boto3.client('iam')

    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "lambda:InvokeFunction",
                "Resource": "*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName='MyLambdaInvokePolicy',
        PolicyDocument=json.dumps(policy_document)
    )

    print(f"Policy ARN: {response['Policy']['Arn']}")
