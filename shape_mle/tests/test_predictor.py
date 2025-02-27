"""
Module for testing prediction functionality
"""

import unittest
import numpy as np
import pandas as pd
from unittest.mock import MagicMock

from shape_mle.ml.predictor import predict


class TestPredictor(unittest.TestCase):
    
    def test_predict_empty_dataframe(self):
        """Test prediction with empty dataframe"""
        empty_df = pd.DataFrame()
        pipeline = MagicMock()
        model = MagicMock()
        
        result = predict(empty_df, pipeline, model)
        
        self.assertEqual(len(result), 0)
    
    def test_predict_with_data(self):
        """Test prediction with sample data"""
        test_df = pd.DataFrame({'feature1': [1, 2], 'feature2': [3, 4]})
        pipeline = MagicMock()
        model = MagicMock()
        
        transformed_data = np.array([[1, 2], [3, 4]])
        expected_predictions = np.array([1, -1])
        
        pipeline.fit_transform.return_value = transformed_data
        model.predict.return_value = expected_predictions
        
        result = predict(test_df, pipeline, model)
        
        self.assertEqual(len(result), 2)
        np.testing.assert_array_equal(result, expected_predictions)


if __name__ == '__main__':
    unittest.main()
