# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC #Read csv file into dataframe using pyspark

# COMMAND ----------

# DBTITLE 1,#Formate1:
df = spark.read.csv(path='dbfs:/filestore/data/employ.csv',header= True)
display(df)
df.printSchema()



# COMMAND ----------

# DBTITLE 1,Formate2:
df = spark.read.format('csv') \
    .options(header='true', inferSchema='true') \
    .load('/dbfs/mnt/data/employ.csv')
display(df)
df.printSchema()
