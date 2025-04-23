# Serverless AWS Architecture Project

This project demonstrates the creation of a serverless architecture using AWS services like Lambda, API Gateway, DynamoDB, SQS, SNS, and IAM.

## Components

- **Lambda Function**: A basic AWS Lambda function that returns a simple message.
- **DynamoDB**: A table creation script for storing data.
- **SNS Topic**: A script to create an SNS topic for message notifications.
- **API Gateway**: An API to invoke the Lambda function.
- **SQS Queue**: A queue to store messages for processing.
- **IAM Policy**: A policy that allows invoking Lambda functions.

## Prerequisites

- AWS Account with necessary IAM permissions.
- Boto3 library installed: `pip install boto3`.
- AWS CLI configured with your credentials.

## Setup and Execution

1. Clone this repository and navigate to the project directory.
2. Ensure you have AWS credentials configured using the AWS CLI.
3. Create the necessary AWS resources by running each script in the terminal.

```bash
python dynamodb_table_creation.py
python sns_topic_creation.py
python api_gateway_configuration.py
python sqs_queue_creation.py
python iam_policy_creation.py
