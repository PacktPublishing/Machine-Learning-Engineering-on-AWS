## Machine Learning Engineering on AWS

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="100px" align="left"></a>

**Chapter 4: Serverless Data Management on AWS** <br />
This chapter presents several severless solutions available such as Amazon Redshift Serverless and AWS Lake Formation when managing and querying data on AWS.

<br />

### I. Links

### II. Commands

#### ➤ Preparing the Essential Prerequisites

##### Creating an IAM User

```
{
    "Version": "2012-10-17", 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "redshift-serverless:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "sqlworkbench:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "lakeformation:*", 
            "Resource": "*"
        } 
    ]
}
```

#### ➤ Running Analytics at Scale with Amazon Redshift Serverless

##### Uploading the dataset to S3

```
wget https://bit.ly/3L6FsRg -O synthetic.bookings.100000.csv

head synthetic.bookings.100000.csv

BUCKET_NAME=<INSERT BUCKET NAME>
aws s3 mb s3://$BUCKET_NAME

FILE=synthetic.bookings.100000.csv
aws s3 cp $FILE s3://$BUCKET_NAME/input/$FILE
```



##### Querying the Database

```
SELECT COUNT(*) FROM dev.public.bookings WHERE is_cancelled = 0;

SELECT * FROM dev.public.bookings WHERE is_cancelled = 1 AND previous_cancellations > 0;

SELECT * FROM dev.public.bookings WHERE is_cancelled = 1 AND days_in_waiting_list > 50;

SELECT booking_changes, has_booking_changes, *
FROM dev.public.bookings
WHERE
(booking_changes=0 AND has_booking_changes='True')
OR
(booking_changes>0 AND has_booking_changes='False');

SELECT total_of_special_requests,
has_special_requests, *
FROM dev.public.bookings
WHERE
(total_of_special_requests=0 AND has_special_requests='True')
OR
(total_of_special_requests>0 AND has_special_requests='False');

CREATE MATERIALIZED VIEW data_integrity_issues AS
SELECT *
FROM dev.public.bookings
WHERE
(booking_changes=0 AND has_booking_changes='True') 
OR
(booking_changes>0 AND has_booking_changes='False')
OR
(total_of_special_requests=0 AND has_special_requests='True')
OR
(total_of_special_requests>0 AND has_special_requests='False');

SELECT booking_changes, has_booking_changes,
total_of_special_requests, has_special_requests FROM
data_integrity_issues;
```
