"""
Module to centralize all configuration parameters
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = BASE_DIR.parent

DATA_DIR = PROJECT_ROOT / "data"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
LOGS_DIR = PROJECT_ROOT / "logs"

os.makedirs(LOGS_DIR, exist_ok=True)

PIPELINE_FILE_PATH = ARTIFACTS_DIR / "pipeline.jsonc"
DATA_FILE_PATH = DATA_DIR / "dataset.parquet"
LOG_FILE_PATH = LOGS_DIR / "failure.log"

FEATURE_COLUMNS = ["vibration_x", "vibration_y", "vibration_z"]