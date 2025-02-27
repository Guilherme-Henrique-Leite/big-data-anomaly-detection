"""
Module to load data
"""

from typing import (
    List,
    Optional,
)

import pandas as pd

from shape_mle.config import DATA_FILE_PATH
from shape_mle.infrastructure.logging import logger
from shape_mle.utils.get_session_spark import get_spark_session


def load_parquet_data(
    file_path: str = str(DATA_FILE_PATH),
    columns: Optional[List[str]] = None,
    use_spark: bool = True
) -> pd.DataFrame:
    """
    Load data from a parquet file
    
    :param file_path: path to parquet file
    :param columns: columns to load
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