## Machine Learning Engineering on AWS

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="100px" align="left"></a>

**Chapter 10: Machine Learning Pipelines with Kubeflow on Amazon EKS** <br />
This chapter focuses on using Kubeflow Pipelines, Kubernetes, and Amazon Elastic Kubernetes Service to deploy an automated end-to-end MLOps pipeline on AWS.

<br />

### I. Links

| Shortened              | Original                                                                                                                                                        |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://bit.ly/3ByyDGV | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter10/ch10_prerequisites.zip                                     |
| https://bit.ly/3POP8CI | https://gist.githubusercontent.com/joshualat/8e64cb4b4de5f46fab010de97460a9be/raw/60fd1dc73ebfff717dac91f8a2bdc50310eacb22/management_experience_and_salary.csv |

### II. Notebooks, Scripts, and Files

| Label                                | Link                                                                                                                            |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Simple Kubeflow Pipeline.ipynb       | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter10/Simple%20Kubeflow%20Pipeline.ipynb   |
| basic_pipeline.yaml                  | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter10/basic_pipeline.yaml                  |
| ch10_prerequisites.zip               | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter10/ch10_prerequisites.zip               |
| management_experience_and_salary.csv | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter10/management_experience_and_salary.csv |

### III. Commands

#### ➤ Preparing the Essential Prerequisites

##### Attaching the IAM role to EC2 instance of the Cloud9 environment

```
ENV_ID=$C9_PID
aws cloud9 update-environment --managed-credentials-action DISABLE --environment-id $ENV_ID


rm -vf /home/ubuntu/.aws/credentials


aws sts get-caller-identity --query Arn
```

##### Updating the Cloud9 environment with the essential prerequisites

```
wget -O prerequisites.zip https://bit.ly/3ByyDGV
unzip prerequisites.zip


cd ch10_prerequisites
chmod +x *.sh


sudo ./00_install_kubectl_aws_jq_and_more.sh


aws --version


kustomize version


eksctl version


. ~/.bash_completion
. ~/.bash_profile
. ~/.bashrc


export AWS_REGION="us-west-2"
echo "export AWS_REGION=${AWS_REGION}" | tee -a ~/.bash_profile
aws configure set default.region ${AWS_REGION}


aws configure get default.region
```

#### ➤ Setting up Kubeflow on Amazon EKS

```
cd ~/environment

mkdir ch10

cd ch10


touch eks.yaml
```

**eks.yaml**
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

```
eksctl create cluster -f eks.yaml --dry-run


eksctl create cluster -f eks.yaml


kubectl get nodes -o wide


CLUSTER_NAME=kubeflow-eks-000
CLUSTER_REGION=us-west-2


eksctl utils associate-iam-oidc-provider --cluster $CLUSTER_NAME --approve -v4


aws eks update-kubeconfig --name $CLUSTER_NAME --region ${AWS_REGION}


export KUBEFLOW_VERSION=v1.5.1
export AWS_VERSION=v1.5.1-aws-b1.0.0
git clone https://github.com/awslabs/kubeflow-manifests.git && cd kubeflow-manifests
git checkout ${AWS_VERSION}
git clone --branch ${KUBEFLOW_VERSION} https://github.com/kubeflow/manifests.git upstream


cd deployments/vanilla

while ! kustomize build . | kubectl apply -f -; do echo "Retrying"; sleep 30; done


ns_array=(kubeflow kubeflow-user-example-com kserve cert-manager istio-system auth knative-eventing knative-serving)


for i in ${ns_array[@]}; do 
  echo "[+] kubectl get pods -n $i"
  kubectl get pods -n $i; 
  echo "---"
done


kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80 --address=localhost
```

#### ➤ Using the Kubeflow Pipelines SDK to build ML workflows

| Label                          | Source Code                                                                                                                   |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Simple Kubeflow Pipeline.ipynb | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter10/Simple%20Kubeflow%20Pipeline.ipynb |


#### ➤ Cleaning Up

```
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80 –-address=localhost


cd ~/environment/ch10/kubeflow-manifests/
cd deployments/vanilla/
kustomize build . | kubectl delete -f -


eksctl delete cluster --region $CLUSTER_REGION --name $CLUSTER_NAME
```
