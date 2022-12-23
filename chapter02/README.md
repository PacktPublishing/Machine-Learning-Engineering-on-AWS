## Machine Learning Engineering on AWS

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="100px" align="left"></a>

**Chapter 2: Deep Learning AMIs** 

This chapter introduces the Deep Learning AMIs and how these are used to help machine learning practitioners perform ML experiments faster inside EC2 instances. Here, we will also dive a bit deeper into how AWS pricing works for EC2 instances so that we will have a better idea on how to optimize and reduce the overall costs of running ML workloads in the cloud.

**NOTES** 
- In case you encounter an error similar to `You have requested more vCPU capacity than your current vCPU limit of 0 allows for...`, feel free to request for an EC2 limit increase http://aws.amazon.com/contact-us/ec2-request to reach out to AWS support.
- Feel free to skip to Chapter 3 while waiting for the EC2 limit increase to be applied to your account (it takes around 1-2 days for this to be approved)

<br />

### I. Links

| Shortened              | Original                                                                                                                      |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| https://bit.ly/3h1KBx2 | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter02/data/training_data.csv   |
| https://bit.ly/3gXYM6v | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter02/data/validation_data.csv |
| https://bit.ly/35aKWem | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter02/data/test_data.csv       |
| https://bit.ly/33D0iYC | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter02/train.py                 |

### II. Commands

#### ➤ Downloading the sample dataset

```
mkdir -p data


wget https://bit.ly/3h1KBx2 -O data/training_data.csv 
wget https://bit.ly/3gXYM6v -O data/validation_data.csv 
wget https://bit.ly/35aKWem -O data/test_data.csv


yum install tree


tree

head data/training_data.csv
```

#### ➤ Training an ML model

```
mkdir -p logs


wget https://bit.ly/33D0iYC -O train.py


tree


for a in /sys/bus/pci/devices/*; do echo 0 | sudo tee -a $a/numa_node; done
```

| Filename | Source Code                                                                                         |
|----------|-----------------------------------------------------------------------------------------------------|
| train.py | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter02/train.py |

```
python3.9 train.py


tensorboard --logdir=logs --bind_all
```

#### ➤ Loading and evaluating the model

```
jupyter notebook --allow-root --port 8888 --ip 0.0.0.0
```

| Filename                      | Source Code                                                                                                                    |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Load and Evaluate Model.ipynb | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter02/Load%20and%20Evaluate%20Model.ipynb |

```
import tensorflow as tf 
tf.config.list_physical_devices('GPU')


model = tf.keras.models.load_model('model')
model.summary()


import numpy as np
def load_data(training_data_location):
    fo = open(training_data_location, "rb") 
    result = np.loadtxt(fo, delimiter=",")
    y = result[:, 0] 
    x = result[:, 1]
    
    return (x, y)
    
    
x, y = load_data("data/test_data.csv")
predictions = model.predict(x[0:5])
predictions


results = model.evaluate(x, y, batch_size=128)
results
```
