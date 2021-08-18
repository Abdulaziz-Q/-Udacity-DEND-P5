# Udacity-DEND-P5

### Project: Data Pipelines with Airflow
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines 
and come to the conclusion that the best tool to achieve this is Apache Airflow.


### Project Overview
This project will introduce the core concepts of Apache Airflow. To complete the project, we will need to create your custom operators to perform tasks such as staging the data, 
filling the data warehouse, and running checks on the data as the final step. 

The DAG will be as shown below:

![DAG](example-dag.png)

### Project Datasets
I'll be working with two datasets that reside in S3. Here are the S3 links for each:

- Song data: s3://udacity-dend/song_data
- Log data: s3://udacity-dend/log_data

### Projects files

- **dags** folder has code file for the imports and tasks.
- **operators** folder has all operators. 
> 1. **Stage Operator** is expected to be able to load any JSON formatted files from S3 to Amazon Redshift.
> 2. **Fact and Dimension Operators** are expected to run data transformations.
> 3. **Data Quality Operator** is used to run checks on the data quality.
- **helpers** for the SQL transformations
