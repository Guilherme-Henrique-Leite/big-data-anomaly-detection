"""
Module for getting a Spark session
"""

from pyspark.sql import SparkSession

from shape_mle.infrastructure.logging import logger

def get_spark_session(app_name: str = "ShapeMLE") -> SparkSession:
    """
    Create or get existing Spark session
    
    :param app_name: name of the spark application
    :return: SparkSession object
    """
    spark = (SparkSession.builder
            .appName(app_name)
            .config("spark.sql.execution.arrow.pyspark.enabled", "true")
            .config("spark.driver.memory", "4g")
            .getOrCreate())
    
    spark.sparkContext.setLogLevel("ERROR")
    logger.info("Spark session created successfully")
    
    return spark 