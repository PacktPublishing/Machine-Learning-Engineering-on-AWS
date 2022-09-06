## Machine Learning Engineering on AWS

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="100px" align="left"></a>

**Chapter 5: Pragmatic Data Processing and Analysis** <br />
This chapter focuses on the different services available such as AWS Glue DataBrew and Amazon SageMaker Data Wrangler when working on data processing and analysis requirements.

<br />

### I. Links

| Filename                         | Link                                                                                                                       |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| synthetic.bookings.dirty.parquet | https://github.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/raw/main/chapter05/synthetic.bookings.dirty.parquet |

### II. Commands

#### ➤ Automating Data Preparation and Analysis with AWS Glue DataBrew

##### Verifying the Results

```
TARGET=<PASTE COPIED S3 URL>
aws s3 cp $TARGET bookings.csv


head bookings.csv
```

#### ➤ Preparing ML Data with Amazon SageMaker Data Wrangler

##### Transforming the Data

```
df = df.filter(df.children >= 0)
expression = df.booking_changes > 0
df = df.withColumn('has_booking_changes', expression)
```

##### Verifying the Results

```
mv * /tmp 2>/dev/null


S3_PATH=<PASTE S3 URL>
aws s3 cp $S3_PATH/ . --recursive


ls -R


head */default/*.csv
```
