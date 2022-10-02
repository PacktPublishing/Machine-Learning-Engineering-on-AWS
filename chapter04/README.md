## Machine Learning Engineering on AWS

<a href="https://www.packtpub.com/product/machine-learning-engineering-on-aws/9781803247595"><img src="https://static.packt-cdn.com/products/9781803247595/cover/smaller" alt="Book Name" height="100px" align="left"></a>

**Chapter 4: Serverless Data Management on AWS** <br />
This chapter presents several severless solutions available such as Amazon Redshift Serverless and AWS Lake Formation when managing and querying data on AWS.

<br />

### I. Links

| Shortened              | Original                                                                                                                           |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| https://bit.ly/3L6FsRg | https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-Engineering-on-AWS/main/chapter04/synthetic.bookings.100000.csv |

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
SELECT * FROM dev.public.bookings;


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

##### Unloading data to S3

```
UNLOAD ('SELECT * FROM dev.public.bookings;') 
TO 's3://<INSERT BUCKET NAME>/unloaded/'
IAM_ROLE 'arn:aws:iam::<ACCOUNT ID>:role/service-role/<ROLE NAME>'
FORMAT AS CSV DELIMITER ',' 
PARALLEL ON
HEADER;


BUCKET_NAME=<INSERT BUCKET NAME>
aws s3 ls s3://$BUCKET_NAME/unloaded/


mv * /tmp


aws s3 cp s3://$BUCKET_NAME/unloaded/ . --recursive


ls


head *
```

#### ➤ Setting up Lake Formation

##### Running SQL queries using Athena

```
SELECT * FROM "AwsDataCatalog"."mle-ch4-db"."unloaded" limit 10;


SELECT COUNT(*) FROM "AwsDataCatalog"."mle-ch4-db"."unloaded" WHERE is_cancelled=0;


SELECT * 
FROM "AwsDataCatalog"."mle-ch4-db"."unloaded" 
WHERE is_cancelled=1 AND previous_cancellations > 0 
LIMIT 100;


SELECT * 
FROM "AwsDataCatalog"."mle-ch4-db"."unloaded" 
WHERE is_cancelled=1 AND days_in_waiting_list > 50 
LIMIT 100;


SELECT booking_changes, has_booking_changes, * 
FROM "AwsDataCatalog"."mle-ch4-db"."unloaded" 
WHERE 
(booking_changes=0 AND has_booking_changes=true) 
OR 
(booking_changes>0 AND has_booking_changes=false)
LIMIT 100;


SELECT total_of_special_requests, has_special_requests, *  
FROM "AwsDataCatalog"."mle-ch4-db"."unloaded" 
WHERE 
(total_of_special_requests=0 AND has_special_requests=true) 
OR 
(total_of_special_requests>0 AND has_special_requests=false)
LIMIT 100;


CREATE OR REPLACE VIEW data_integrity_issues AS
SELECT * 
FROM "AwsDataCatalog"."mle-ch4-db"."unloaded" 
WHERE
(booking_changes=0 AND has_booking_changes=true) 
OR 
(booking_changes>0 AND has_booking_changes=false)
OR
(total_of_special_requests=0 AND has_special_requests=true) 
OR 
(total_of_special_requests>0 AND has_special_requests=false);


SELECT booking_changes, has_booking_changes, 
total_of_special_requests, has_special_requests 
FROM data_integrity_issues 
LIMIT 100;
```
