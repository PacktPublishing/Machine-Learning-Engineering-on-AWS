import json

from utils import (
    create_model, 
    create_endpoint_config, 
    update_endpoint, 
    random_string,
    block
)


def lambda_handler(event, context):
    role = event['role']
    endpoint_name = event['endpoint_name']
    package_arn = event['package_arn']
    
    model_name = 'model-' + random_string()
    
    with block('CREATE MODEL'):
        create_model(
            model_name=model_name,
            package_arn=package_arn,
            role=role
        )
    
    with block('CREATE ENDPOINT CONFIG'):
        endpoint_config_name = create_endpoint_config(
            model_name
        )
    
    with block('UPDATE ENDPOINT'):
        update_endpoint(
            endpoint_name=endpoint_name, 
            endpoint_config_name=endpoint_config_name
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps(event),
        'model': model_name
    }
