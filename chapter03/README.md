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