# Visualize Volume Data
# Created by: Apoorba Bibeka
# Date: April 4, 2019


#Load the library for accessing and writing files to s3 bucket
library("aws.s3")
#Connect to the TTI bucket
Sys.setenv("AWS_ACCESS_KEY_ID"="abibeka","AWS_SECRET_ACCESS_KEY"=.rs.api.askForPassword("Password"))
#Get the list objects in our bucket


fi="s3://prod-sdc-tti-911061262852-us-east-1-bucket/abibeka/Vol_dat.csv"
aws.s3::s3read_using(read.csv,object=fi)