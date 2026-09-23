# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC #Read csv file into dataframe using pyspark

# COMMAND ----------

# DBTITLE 1,#Formate1:
df = spark.read.csv(path='/Volumes/tri/tri/tri_files/INPUT/BigMart Sales.csv',header= True)
display(df)
df.printSchema()



# COMMAND ----------

# DBTITLE 1,Formate2:
df = spark.read.format('csv') \
    .options(header='true', inferSchema='true') \
    .load('/Volumes/tri/tri/tri_files/INPUT/BigMart Sales.csv')
display(df)
df.printSchema()

# COMMAND ----------

#read all csv files from one folder(no other files)
#we already see particluar file
df = spark.read.csv(path='/Volumes/tri/tri/tri_files',header= True)
display(df)
df.printschema()


# COMMAND ----------

#read multiple csv files from different folders:-
df = spark.read.csv(path=['dbfs:/filestore/data/employ1.csv','dbfs:/filestore/data/employ2.csv'], header= true)
display(df)
df.printschema()


# COMMAND ----------

#read all csv files :- (different files also there along with json files)

df3= spark.read.csv('dbfs:/filestore/data/*.csv')
df.printschema()
df3.show()


# COMMAND ----------

# MAGIC %md
# MAGIC **write date frame into csv file using pyspark**

# COMMAND ----------

/Volumes/tri/tri/tri_files/OUTPUT/

# COMMAND ----------

data = [(1,'jhansi'),(2,'jhanu')]
schema = ['id','name']
df = spark.createDataFrame(data = data,schema = schema)


df.write.csv(path='/Volumes/tri/tri/tri_files/OUTPUT/',header=True,mode = 'overwrite')
display(spark.read.csv(path='/Volumes/tri/tri/tri_files/OUTPUT/',header=True))


# COMMAND ----------

# MAGIC %md
# MAGIC **#we can use mode = ignore /overwrite/append/error**

# COMMAND ----------

df.write.csv(path='dbfs:/tmp/emps',header=true,mode = 'error')#-data there it gives
df.write.csv(path='dbfs:/tmp/emps',header=true,mode = 'overwrite')#-overwrite existing data
df.write.csv(path='dbfs:/tmp/emps',header=true,mode = 'ignore')#-throw error data there
df.write.csv(path='dbfs:/tmp/emps',header=true,mode = 'append')#-it will add data
