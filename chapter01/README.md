## Machine Learning Engineering on AWS

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="100px" align="left"></a>

**Chapter 1: Introduction to ML Engineering on AWS** <br />
This chapter focuses on helping the reader set up, understand the key concepts, and get their feet wet quickly with several
simplified AutoML examples.

<br />

### I. Links

| Shortened              | Original                                                                                                                    |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| https://bit.ly/3ea96tW | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter01/resize_and_reboot.py   |
| https://bit.ly/3CN4owx | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter01/utils.py               |
| https://bit.ly/3CHNQFT | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter01/hotel_bookings.gan.pkl |

### II. Commands

#### ➤ Essential prerequisites

##### Increasing Cloud9's storage

```
wget -O resize_and_reboot.py https://bit.ly/3ea96tW


python3 -m pip install --user --upgrade boto3


TARGET_METADATA_URL=http://169.254.169.254/latest/meta-data/instance-id
export EC2_INSTANCE_ID=$(curl -s $TARGET_METADATA_URL)
echo $EC2_INSTANCE_ID


python3 resize_and_reboot.py
```

##### Installing the Python prerequisites

```
python3 -m pip install -U pip
python3 -m pip install -U setuptools wheel


python3 -m pip install ipython


python3 -m pip install ctgan==0.5.0


python3 -m pip install pandas_profiling
```

##### Generating a synthetic dataset using a deep learning model

```
mkdir -p tmp


wget -O utils.py https://bit.ly/3CN4owx


wget -O hotel_bookings.gan.pkl https://bit.ly/3CHNQFT


touch data_generator.py
```

| Filename          | Source Code                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| data_generator.py | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter01/data_generator.py |

```
python3 data_generator.py
```

##### Train-test split

```
touch train_test_split.py
```

| Filename            | Source Code                                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------------------|
| train_test_split.py | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/blob/main/chapter01/train_test_split.py |

```
python3 train_test_split.py
```

##### Uploading the dataset to Amazon S3

```
BUCKET_NAME="<INSERT BUCKET NAME HERE>" 
aws s3 mb s3://$BUCKET_NAME


S3=s3://$BUCKET_NAME/datasets/bookings 
TRAIN=bookings.train.csv 
TEST=bookings.test.csv

aws s3 cp tmp/bookings.train.csv $S3/$TRAIN 
aws s3 cp tmp/bookings.test.csv $S3/$TEST
```

#### ➤ AutoML with AutoGluon

##### Setting up and installing AutoGluon

```
python3 -m pip install -U "mxnet<2.0.0" 
python3 -m pip install numpy
python3 -m pip install cython
python3 -m pip install pyOpenSSL --upgrade


python3 -m pip install autogluon
```

##### Performing your first AutoGluon AutoML experiment

```
ipython


from autogluon.tabular import ( 
    TabularDataset,
    TabularPredictor
)


train_loc = 'tmp/bookings.train.csv' 
test_loc = 'tmp/bookings.test.csv' 
train_data = TabularDataset(train_loc) 
test_data = TabularDataset(test_loc)


label = 'is_cancelled' 
save_path = 'tmp'
tp = TabularPredictor(label=label, path=save_path)
predictor = tp.fit(train_data) 


y_test = test_data[label]
test_data_no_label = test_data.drop(columns=[label])
y_pred = predictor.predict(test_data_no_label)


predictor.evaluate_predictions(
    y_true=y_test,
    y_pred=y_pred,
    auxiliary_metrics=True
)


exit()
```
