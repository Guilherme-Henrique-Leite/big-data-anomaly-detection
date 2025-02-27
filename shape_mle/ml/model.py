"""
Module to load models
"""

import pickle
from typing import Any

from shape_mle.infrastructure.logging import logger


def load_model(model_path: str) -> Any:
    """
    Load a model from a pickle file
    
    :param model_path: path to the pickle file
    :return: the loaded model object
    """
    try:
        logger.info(f"Loading model from {model_path}")
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        if not hasattr(model, 'predict'):
            raise AttributeError('Model does not have a predict function')
            
        return model
    
    except Exception as e:
        logger.error(f"Failed to load model from {model_path}: {str(e)}")
        raise RuntimeError(f"Failed to load model from {model_path}: {str(e)}")