"""
Module to run the prediction pipeline
"""

import os
import json

from anomaly_mle.config import (
    PIPELINE_FILE_PATH, 
    DATA_FILE_PATH, 
    FEATURE_COLUMNS, 
    PROJECT_ROOT
)

from anomaly_mle.ml.model import load_model
from anomaly_mle.ml.predictor import predict
from anomaly_mle.ml.pipeline import load_pipeline

from anomaly_mle.data.loader import load_parquet_data
from anomaly_mle.utils.results import save_results

from anomaly_mle.infrastructure.logging import logger, setup_logger

def get_model_path():
    """
    Extract the model path from the pipeline configuration file
    
    :return: path to the model file
    """
    try:
        with open(PIPELINE_FILE_PATH, 'r') as f:
            content = '\n'.join(f.readlines()[3:])
        
        config = json.loads(content)
        model_path = config.get("steps", {}).get("model", "")
        
        if not model_path:
            raise ValueError("Model path not found in pipeline configuration")
        
        if not os.path.isabs(model_path):
            model_path = os.path.join(PROJECT_ROOT, model_path)
            
        return model_path
        
    except Exception as e:
        logger.error(f"Failed to get model path: {str(e)}")
        raise

def main():
    """
    Main function to run the prediction pipeline
    
    This function:
    - Loads the data from the parquet file
    - Loads the preprocessing pipeline from the configuration
    - Loads the trained model
    - Makes predictions on the data
    - Reports the results
    - Saves the results to a file
    
    :return: predictions as numpy array
    """
    setup_logger()
    
    try:
        logger.info(f"Loading data from {DATA_FILE_PATH}...")
        data = load_parquet_data(
            file_path=str(DATA_FILE_PATH), 
            columns=FEATURE_COLUMNS
        )
        logger.info(f"Loaded data with shape: {data.shape}")
        
        logger.info(f"Loading pipeline from {PIPELINE_FILE_PATH}...")
        pipeline = load_pipeline(str(PIPELINE_FILE_PATH))
        logger.info(f"Pipeline loaded with {len(pipeline.steps)} steps")
        
        model_path = get_model_path()
        logger.info(f"Loading model from {model_path}...")
        model = load_model(model_path)
        
        logger.info("Making predictions...")
        predictions = predict(data, pipeline, model)
        anomalies = sum(predictions == -1)
        normal = sum(predictions == 1)
        
        logger.info(f"Results: {len(predictions)} total predictions")
        logger.info(f"- Normal samples: {normal} ({normal/len(predictions)*100:.2f}%)")
        logger.info(f"- Anomalies detected: {anomalies} ({anomalies/len(predictions)*100:.2f}%)")
        
        save_results(predictions)
        
        return predictions
        
    except Exception as e:
        logger.error(f"Application failed: {str(e)}")
        raise

if __name__ == "__main__":
    main() 