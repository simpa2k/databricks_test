import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions.lit

object Transformations {
  def addMetadata(df: DataFrame): DataFrame =
    df.withColumn("metadata_column", lit("this is a metadata column"))
}