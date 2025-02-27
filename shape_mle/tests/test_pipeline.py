"""
Module for testing pipeline loading
"""

import unittest
from unittest.mock import patch, MagicMock

from shape_mle.ml.pipeline import load_pipeline


class TestPipeline(unittest.TestCase):
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open')
    @patch('json.loads')
    def test_load_pipeline(self, mock_json_loads, mock_open, mock_exists):
        """Test loading a pipeline from configuration file"""
        mock_exists.return_value = True
        mock_json_loads.return_value = {
            "steps": {
                "stdscaler": {
                    "StandardScaler": {
                        "with_mean": True
                    }
                }
            }
        }
        
        pipeline = load_pipeline('test.jsonc')
        
        self.assertIsNotNone(pipeline)


if __name__ == '__main__':
    unittest.main()