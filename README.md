# Machine Learning Engineering on AWS 

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="256px" align="right"></a>

This is the code repository for [Machine Learning Engineering on AWS](https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595), published by Packt.

**Building, Scaling, and Securing Machine Learning Systems and MLOps Pipelines in Production**

## What is this book about?
There is a growing need for professionals who have experience working on machine learning engineering requirements as well as knowledge automating complex MLOps pipelines in the cloud. In this book, we will explore a variety of AWS services that ML practitioners can use to solve various ML engineering requirements and challenges in production.

This book covers the following exciting features: 
* Learn how to train and deploy TensorFlow and PyTorch models on AWS
* Use containers and serverless services for ML engineering requirements
* Learn how to set up a serverless data warehouse and data lake on AWS
* Build automated end-to-end MLOps pipelines using a variety of services
* Use AWS Glue DataBrew and SageMaker Data Wrangler for data engineering
* Explore different solutions for deploying deep learning models on AWS
* Apply cost optimization techniques to ML environments and systems
* Preserve data privacy and model privacy using a variety of techniques

If you feel this book is for you, get your [copy](https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, chapter10.

The code will look like the following:

```
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: kubeflow-eks-000
  region: us-west-2
  version: "1.21"

availabilityZones: ["us-west-2a", "us-west-2b", "us-west-2c", "us-west-2d"]

managedNodeGroups:
- name: nodegroup
  desiredCapacity: 5
  instanceType: m5.xlarge
  ssh:
    enableSsm: true
```

This book is for machine learning engineers, data scientists, and AWS cloud engineers interested in working on production data engineering, machine learning engineering, and MLOps requirements using a variety of AWS Services such as Amazon EC2, Amazon Elastic Kubernetes Service (EKS), Amazon SageMaker, AWS Glue, Amazon Redshift, AWS LakeFormation, and AWS Lambda. All you need is an AWS account to get things running. Prior knowledge of AWS, machine learning, and Python programming language will help you to grasp the concepts covered in this book more effectively.

With the following software and hardware list you can run all code files present in the book (Chapter 1-11).

### Software and Hardware List

| Chapter   | Software required                | OS required                        |
| --------- | ---------------------------------| -----------------------------------|
| 1-11      | AWS Account                      | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. 

## Get to Know the Author
**Joshua Arvin Lat** is the Chief Technology Officer (CTO) of NuWorks Interactive Labs, Inc. He previously served as the CTO of three Australian-owned companies and also served as the Director for Software Development and Engineering for multiple e-commerce start-ups in the past, which allowed him to be more effective as a leader. Years ago, he and his team won first place in a global cybersecurity competition with their published research paper. He is also an AWS Machine Learning Hero and has shared his knowledge at several international conferences, discussing practical strategies on machine learning, engineering, security, and management. He is the author of the books ["Machine Learning with Amazon SageMaker Cookbook: 80 proven recipes for data scientists and developers to perform machine learning experiments and deployments"](https://www.amazon.com/Machine-Learning-Amazon-SageMaker-Cookbook/dp/1800567030/) and ["Machine Learning Engineering on AWS: Building, Scaling, and Securing Machine Learning Systems and MLOps Pipelines in Production"](https://www.amazon.com/Machine-Learning-Engineering-AWS-Production/dp/1803247592/)
