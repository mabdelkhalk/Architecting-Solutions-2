import boto3

def create_api_gateway():
    apigateway = boto3.client('apigateway')

    response = apigateway.create_rest_api(
        name='MyAPI',
        description='This is an example API Gateway',
    )

    print(f"API Gateway created with ID: {response['id']}")
