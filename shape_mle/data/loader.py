"""
Data loading functionality for the application.

This module handles loading and basic preprocessing of data from various sources,
optimized for big data scenarios using PySpark.
"""

from typing import Optional, List
import pandas as pd
from pyspark.sql import SparkSession

from shape_mle.config import DATA_FILE_PATH
from shape_mle.infrastructure.logging import logger


def get_spark_session(app_name: str = "ShapeMLE") -> SparkSession:
    """
    Create or get an existing Spark session.
    
    :param app_name: Name of the Spark application
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


def load_parquet_data(
    file_path: str = str(DATA_FILE_PATH),
    columns: Optional[List[str]] = None,
    use_spark: bool = True
) -> pd.DataFrame:
    """
    Load data from a parquet file.
    
    :param file_path: path to parquet file
    :param columns(Optional): columns to load
    :param use_spark: use spark for loading files
    :return: dataframe with loaded data
    """
    try:    
        logger.info(f"Loading data from {file_path}")   
        if use_spark:
            spark = get_spark_session()
            
            spark_df = spark.read.parquet(file_path)
            
            if columns:
                spark_df = spark_df.select(columns)
                
            logger.info(f"Converting Spark DataFrame to pandas (schema: {spark_df.schema})")
            return spark_df.toPandas()
        
        else:
            return pd.read_parquet(file_path, columns=columns)
            
    except Exception as e:
        logger.error(f"Failed to load data from {file_path}: {str(e)}")
        raise OSError(f"Failed to load data from {file_path}: {str(e)}")