## Machine Learning Engineering on AWS

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="100px" align="left"></a>

**Chapter 3: Deep Learning Containers** <br />
This chapter introduces the AWS Deep Learning Containers and how these are used to help machine learning practitioners perform ML experiments faster using containers. Here, we will also deploy a trained deep learning model inside an AWS Lambda Function using Lambda's container image support.

<br />

### I. Links

| Shortened              | Original                                                                                                                    |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| https://bit.ly/3h1KBx2 | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter02/data/training_data.csv |
| https://bit.ly/3KcsG3v | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter03/train.py               |
| https://bit.ly/3Iz7zaV | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter03/train.sh               |
| https://bit.ly/3pt5mGN | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter03/dlclambda.zip          |

### II. Commands

#### ➤ Essential prerequisites

##### Preparing the Cloud9 environment

```
mkdir -p ch03 

cd ch03
```

##### Downloading the sample dataset

```
mkdir -p data


wget https://bit.ly/3h1KBx2 -O data/training_data.csv


head data/training_data.csv
```

#### ➤ Using AWS Deep Learning Containers to train an ML model

```
wget https://bit.ly/3KcsG3v -O train.py


mkdir -p model


sudo apt install tree


tree


wget https://bit.ly/3Iz7zaV -O train.sh


chmod +x train.sh 

./train.sh


tree
```

#### ➤ Serverless ML deployment with Lambda’s container image support

##### Building the custom container image

```
wget https://bit.ly/3pt5mGN -O dlclambda.zip 

unzip dlclambda.zip


tree


cp model/model.pth app/model/model.pth


chmod +x *.sh


cat build.sh


./build.sh


docker images | grep dlclambda
```

##### Testing the container image

```
cat download-rie.sh


sudo ./download-rie.sh


cat run.sh


./run.sh


cd ch03

cat invoke.sh


./invoke.sh
```

##### Pushing the container image to Amazon ECR

```
docker tag dlclambda:latest <ACCOUNT ID>.dkr.ecr.us-west-2.amazonaws.com/dlclambda:1


docker images


docker push <ACCOUNT ID>.dkr.ecr.us-west-2.amazonaws.com/dlclambda:1
```

##### Running ML predictions on AWS Lambda

```
{
  "queryStringParameters": {
    "x": 42 
  }
}
```
