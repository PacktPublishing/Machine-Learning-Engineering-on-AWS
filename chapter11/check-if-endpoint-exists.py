import boto3

sm_client = boto3.client('sagemaker')


def endpoint_exists(endpoint_name):
    response = sm_client.list_endpoints(
        NameContains=endpoint_name
    )
    
    results = list(
        filter(
            lambda x: \
            x['EndpointName'] == endpoint_name, 
            
            response['Endpoints']
        )
    )
    
    return len(results) > 0


def lambda_handler(event, context):
    endpoint_name = event['endpoint_name']
    
    return {
        'endpoint_exists': endpoint_exists(
            endpoint_name=endpoint_name
        )
    }
