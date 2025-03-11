"""
Pipeline loading functionality
"""

import json
from pathlib import Path

from sklearn.pipeline import Pipeline

from anomaly_mle.infrastructure.logging import logger
from anomaly_mle.utils.transformer_map import TRANSFORMER_MAP

def load_pipeline(file_path: str) -> Pipeline:
    """
    Build a pipeline from a jsonc file
    
    :param file_path: path to the jsonc pipeline file
    :return: scikit-learn pipeline
    """
    if not file_path or not Path(file_path).exists():
        raise ValueError(f"Pipeline file not found: {file_path}")
    
    logger.info(f"Loading pipeline from {file_path}")
    
    try:
        with open(file_path, 'r') as f:
            content = '\n'.join(f.readlines()[3:])
        
        config = json.loads(content)
        steps_config = config.get("steps", {})
        
        steps = []
        for step_name, step_config in steps_config.items():
            if step_name == "model":
                continue
                
            for transformer_name, params in step_config.items():
                if transformer_name in TRANSFORMER_MAP:
                    transformer = TRANSFORMER_MAP[transformer_name](**params)
                    steps.append((step_name, transformer))
        
        return Pipeline(steps)
        
    except Exception as e:
        logger.error(f"Failed to load pipeline: {str(e)}")
        raise RuntimeError(f"Failed to load pipeline: {str(e)}")