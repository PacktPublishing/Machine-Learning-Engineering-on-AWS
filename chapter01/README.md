## INCREASING THE VOLUME SIZE OF THE CLOUD9 ENVIRONMENT

### Step # 1

Download the file `resize_and_reboot.py`

### Step # 2

Run the following in the terminal

**REFERENCE**: `increase_volume_size.sh`

```
pip3 install --user --upgrade boto3

TARGET_METADATA_URL=http://169.254.169.254/latest/meta-data/instance-id
export EC2_INSTANCE_ID=$(curl -s $TARGET_METADATA_URL)
echo $EC2_INSTANCE_ID
```

Run the `resize_and_reboot.py` script

```
python3 resize_and_reboot.py
```

## INSTALLING THE PREREQUISITES

### Step # 3

**REFERENCE**: `install_prereqs.sh`

Upgrade `pip`, `setuptools`, and `wheel`

```
pip3 install -U pip
pip3 install -U setuptools wheel
```

Install `IPython`, `ctgan`, and `pandas_profiling`

```
pip3 install ipython
pip3 install ctgan
pip3 install pandas_profiling
```

## GENERATING A SYNTHETIC DATASET USING CTGAN

### Step # 4

```
mkdir -p tmp
```

### Step # 5

Download the files `utils.py`, `data_generator.py` and `hotel_bookings.gan.pkl`

### Step # 6

Run the following command

```
python3 data_generator.py
```

### Step # 7

Download the file `train_test_split.py`

### Step # 8

Run the following commands

```
python3 train_test_split.py

BUCKET_NAME="mlengineering-on-aws"
aws s3 mb s3://$BUCKET_NAME

S3=s3://$BUCKET_NAME/datasets/bookings
aws s3 cp tmp/bookings.train.csv $S3/bookings.train.csv
aws s3 cp tmp/bookings.test.csv $S3/bookings.test.csv
```

## INSTALLING AND RUNNING AUTOGLUON

### Step # 9

Setup and Install `autogluon`

```
pip3 install -U "mxnet<2.0.0"
pip3 install numpy
pip3 install cython
pip3 install autogluon
```

### Step # 10

Download the file `autogluon_automl.py`

Run the following command

```
python3 autogluon_automl.py
```
