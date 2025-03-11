"""
Module for testing model loading
"""

import unittest
from unittest.mock import patch, MagicMock

from anomaly_mle.ml.model import load_model


class TestModel(unittest.TestCase):
    
    @patch('builtins.open')
    @patch('pickle.load')
    def test_load_model(self, mock_pickle_load, mock_open):
        """Test loading a model from pickle file"""
        mock_model = MagicMock()
        mock_model.predict = MagicMock()
        mock_pickle_load.return_value = mock_model
        
        model = load_model('test.pkl')
        
        self.assertEqual(model, mock_model)


if __name__ == '__main__':
    unittest.main()
