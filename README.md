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

## 3. Transform the landing customer Table into trusted customer table with AWS Glue Studio:
 From all the Customer data from the Website (Landing Zone), we only store the Customer Records who agreed to share their data for research purposes (Trusted Zone). Thus, creating a Glue Table called customer_trusted. 
  <p align="center" width="100%"> <img width="40%" src="https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/customer_trusted_glue_studio.PNG"> </p>

  * [Python script used to create the trusted customer table](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/customer_landing_to_trusted.py)
  * [Screenshot of the trusted customer table data](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/customer_trusted.PNG)

## 4. transform the landing Accelerometer Table into trusted accelerometer table with AWS Glue Studio:
 After obtaining customer_trusted data, we also need to store Accelerometer Readings from customers who agreed to share their data for research purposes (Trusted Zone) through creating a Glue Table called accelerometer_trusted.
 <p align="center" width="100%"> <img width="60%" src="https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/accelerometer_trusted_glue_studio.PNG"> </p>

  * [Python script used to create the trusted customer table](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/accelerometer_landing_to_trusted.py)
  * [Screenshot of the trusted customer table data](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/accelerometer_trusted.PNG)

## 5. Cutomer data curation:
 Due to a data quality issue with the Customer Data where the serial number that should be unique was used for the same users. Thus we created a Glue Table for the trusted Customer data that only includes customers who have accelerometer data and have agreed to share their data for research called customers_curated.
 
  <p align="center" width="100%"> <img width="60%" src="https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/customer_curated_glue_studio.PNG"> </p>

  * [Python script used to create the trusted customer table](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/customer_trusted_to_curated.py)
  * [Screenshot of the trusted customer table data](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/customer_curated.PNG)

## 6. Transform the landing step_trainer Table into trusted step trainer table with AWS Glue Studio:
 From all the step trainer data from the IoT data stream (Landing Zone), we only store the IoT data stream Records of customers who have agreed to share their data for research purposes and who have accelerometer data (Curated Zone).
 
  <p align="center" width="100%"> <img width="50%" src="https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/step_trainer_trusted_glue_studio.PNG"> </p>

  * [Python script used to create the trusted customer table](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/step_trainer_landing_to_trusted.py)
  * [Screenshot of the trusted customer table data](https://github.com/UsernameNotFoundError/UdacitySTEDIHumanBalanceAnalyticProject/blob/master/step_trainer_trusted.PNG)
