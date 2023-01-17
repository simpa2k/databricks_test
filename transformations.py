from pyspark.sql import DataFrame
from pyspark.sql.functions import lit


def add_metadata(df: DataFrame) -> DataFrame:
    return df.withColumn("metadata_column", lit("this is a metadata column"))