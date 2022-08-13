import json
import uuid
import boto3

from time import sleep
from contextlib import contextmanager


sm_client = boto3.client('sagemaker')


@contextmanager
def block(label):
    print(f"[{label}]: START")
    yield
    print(f"[{label}]: END")


def random_string():
    return uuid.uuid4().hex.upper()[0:6]


def wait_for_endpoint_creation(endpoint_name):
    response = sm_client.describe_endpoint(EndpointName=endpoint_name)
    print(response['EndpointStatus'])

    while response['EndpointStatus'] != 'InService':
        response = sm_client.describe_endpoint(EndpointName=endpoint_name)
        print(response['EndpointStatus'])
        print('Sleeping for 30 seconds')
        sleep(30)


def create_endpoint_config(model_name):
    endpoint_config_name = 'endpoint-config-' + random_string()
    
    create_endpoint_config_response = sm_client.create_endpoint_config(
    EndpointConfigName = endpoint_config_name,
    ProductionVariants=[{
        'InstanceType': 'ml.m5.xlarge',
        'InitialVariantWeight': 1,
        'InitialInstanceCount': 1,
        'ModelName': model_name,
        'VariantName': 'AllTraffic'}]
    )
    
    return endpoint_config_name


def create_endpoint(endpoint_name, endpoint_config_name):
    create_endpoint_response = sm_client.create_endpoint(
        EndpointName=endpoint_name,
        EndpointConfigName=endpoint_config_name
    )
    
    print(create_endpoint_response)
    
    wait_for_endpoint_creation(endpoint_name)
    
    print('Endpoint is ready')
    

def update_endpoint(endpoint_name, endpoint_config_name):
    
    wait_for_endpoint_creation(endpoint_name)
    
    update_endpoint_response = sm_client.update_endpoint(
        EndpointName=endpoint_name,
        EndpointConfigName=endpoint_config_name
    )

    print(update_endpoint_response)
    
    wait_for_endpoint_creation(endpoint_name)
    
    print('Endpoint is ready')


def create_model(model_name, package_arn, role):
    container_list = [{'ModelPackageName': package_arn}]

    create_model_response = sm_client.create_model(
        ModelName=model_name,
        ExecutionRoleArn=role,
        Containers=container_list
    )

    print(create_model_response)
