
```
mkdir -p ~/.aws-lambda-rie && curl -Lo ~/.aws-lambda-rie/aws-lambda-rie \
https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie \
&& chmod +x ~/.aws-lambda-rie/aws-lambda-rie

sudo ./download-rie.sh

cat run.sh

docker run -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 --entrypoint /aws-lambda/aws-lambda-rie dlclambda:latest /opt/conda/bin/python -m awslambdaric app.handler

./run.sh

cd ch03
 
cat invoke.sh

curl -XPOST "http://localhost:9000/2015-03-31/ functions/function/invocations" -d '{"queryStringParameters":{"x":42}}'
```
