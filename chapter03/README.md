```
wget https://bit.ly/3KcsG3v -O train.py
mkdir -p model
mkdir -p data
wget https://bit.ly/3h1KBx2 -O data/training_data.csv
```

```
TRAINING_IMAGE=763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:1.8.1-cpu-py36-ubuntu18.04
docker run -it -v `pwd`:/env -w /env $TRAINING_IMAGE python train.py
```

```
docker build -t myfunction02 .
docker run  -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 --entrypoint /aws-lambda/aws-lambda-rie myfunction02:latest /opt/conda/bin/python -m awslambdaric app.handler
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"queryStringParameters":{"x":42}}'
```

```
wget https://bit.ly/344bLAF -O dlclambda.zip
unzip dlclambda.zip

chmod +x *.sh
./build.sh
./run.sh

<open new tab>
./invoke.sh
```

- create ECR repo
- view push commands

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 581320662326.dkr.ecr.us-east-1.amazonaws.com
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