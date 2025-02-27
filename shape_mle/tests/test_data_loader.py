"""
Module for testing data loader
"""

import unittest
import pandas as pd
from unittest.mock import patch

from shape_mle.data.loader import load_parquet_data


class TestDataLoader(unittest.TestCase):
    """
    Test class for data loader
    """
    @patch('shape_mle.data.loader.pd.read_parquet')
    def test_load_data_without_spark(self, mock_read_parquet):
        """Test loading data without using Spark"""
        mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        mock_read_parquet.return_value = mock_df
        
        result = load_parquet_data(file_path='test.parquet', use_spark=False)
        self.assertEqual(result.shape, (2, 2))


if __name__ == '__main__':
    unittest.main()