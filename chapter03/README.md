```
mkdir -p ch03
cd ch03
```

```
wget https://bit.ly/3KcsG3v -O train.py
mkdir -p model
mkdir -p data
wget https://bit.ly/3h1KBx2 -O data/training_data.csv
```

```
wget https://bit.ly/3Iz7zaV -O train.sh
chmod +x train.sh
./train.sh
```

```
wget https://bit.ly/3pt5mGN -O dlclambda.zip

unzip dlclambda.zip
cp model/model.pth app/model/model.pth

chmod +x *.sh
./build.sh

(check total size)
docker images | grep dlclambda

sudo ./download-rie.sh
./run.sh

<open new tab>
cd ch03
./invoke.sh
```

- create ECR repo
- view push commands

```
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 581320662326.dkr.ecr.us-west-2.amazonaws.com
```

- create lambda
- configure [10240 MB] [1 min]

```
{
  "queryStringParameters": {
    "x": 42
  }
}
```

- add trigger [API Gateway]
- Create an API > HTTP API
- Security: open

```
https://tedl9zcva7.execute-api.us-east-1.amazonaws.com/default/torchl-test?x=42
```


Getting started with AWS Deep Learning Containers
Essential Prerequisites
Training an ML Model
Preparing the Lambda Container Image
    Preparing ...
    Testing the Lambda Container Image locally
Pushing the Container Image to ECR
    Creating an ECR Repository
    Pushing the Container Image to ECR
Completing the Serverless API Endpoint
    Creating the Lambda Function for Inference
    API Gateway