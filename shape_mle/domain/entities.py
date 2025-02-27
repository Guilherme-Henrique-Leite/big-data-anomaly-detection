"""
Domain entities for application.
"""

from typing import(
    Any,
    Dict,
)
import numpy as np
from pydantic import BaseModel, Field


class PipelineConfig(BaseModel):
    """Configuration for a machine learning pipeline."""
    steps: Dict[str, Any] = Field(..., description="Pipeline steps configuration")
    
    def model_path(self) -> str:
        """Get the path to the model file."""
        return self.steps.get("model", "")


class PredictionResult(BaseModel):
    """Result of a model prediction."""
    predictions: np.ndarray = Field(..., description="Model predictions")

    @property
    def model_shape(self) -> tuple:
        """Get the shape of the predictions array."""
        return self.predictions.shape