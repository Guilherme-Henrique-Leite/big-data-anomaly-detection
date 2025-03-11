"""
Module to make predictions
"""

import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline

from anomaly_mle.infrastructure.logging import logger

def predict(data: pd.DataFrame, pipeline: Pipeline, model) -> np.ndarray:
    """
    Make predictions using the preprocessing pipeline and model
    
    :param data: input data as a dataframe
    :param pipeline: preprocessing pipeline
    :param model: trained model
    :return: predictions as a numpy array
    """
    if data.empty:
        logger.warning("Empty data provided for prediction")
        return np.array([])
    
    logger.info(f"Making predictions on {len(data)} samples")
    
    try:
        logger.info("Applying preprocessing pipeline")
        X_transformed = pipeline.fit_transform(data)
        
        logger.info("Running model prediction")
        predictions = model.predict(X_transformed)
        
        logger.info(f"Generated {len(predictions)} predictions")
        return predictions
        
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise RuntimeError(f"Prediction failed: {str(e)}")