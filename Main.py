# Databricks notebook source
from transformations import add_metadata

# COMMAND ----------

df = spark.createDataFrame([{'a': 1, 'b': 2, 'c': 3}])

# COMMAND ----------

display(df)

# COMMAND ----------

display(add_metadata(df))

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------

# MAGIC %scala
# MAGIC 
# MAGIC package se.folksam.y73
# MAGIC 
# MAGIC case class Test(a: Int, b: Int, c: Int)

# COMMAND ----------

# MAGIC %scala
# MAGIC 
# MAGIC import se.folksam.y73.Test
# MAGIC 
# MAGIC Test(1, 2, 3)
