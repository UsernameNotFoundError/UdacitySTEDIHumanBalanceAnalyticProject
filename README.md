# UdacitySTEDIHumanBalanceAnalyticProject
Using AWS Glue, AWS S3, Python, and Spark, create or generate Python scripts to build a lakehouse solution in AWS that satisfies these requirements from the STEDI data scientists.

## 1. Create S3 Bucket and load the landing data:

Data source: https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/tree/main/project/starter

data landing location: 
* `https://s3.console.aws.amazon.com/s3/buckets/<your-bucket-name>?region=<your-region>-1&prefix=project/customer/landing/`
* `https://s3.console.aws.amazon.com/s3/buckets/<your-bucket-name>?region=<your-region>-1&prefix=project/accelerometer/landing/`
* `https://s3.console.aws.amazon.com/s3/buckets/<your-bucket-name>?region=<your-region>-1&prefix=project/step_trainer/landing/`
## 2. Create Glue Table with Athena:
  * [SQL script to create customer table](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/customer_landing.sql)
  * [Screenshot of the customer table data](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/customer_landing.PNG)
  * [SQL script to create accelerometer table](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/accelerometer_landing.sql)
  * [Screenshot of the accelerometer table  data](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/accelerometer_landing.PNG)
