"""
Logging module for application.
"""

import logging
import datetime

from anomaly_mle.config import LOG_FILE_PATH


def setup_logger() -> logging.Logger:
    """
    Configures and returns a basic logger
    
    :return: Configured logger
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s',
        handlers=[logging.StreamHandler()]
    )
    
    logger = logging.getLogger('shape_mle')
    
    return logger


logger = setup_logger()


def log_failure(exception: Exception) -> None:
    """
    Logs a failure with date/time in the log file
    
    :exception: The exception to be logged
    """
    logger.error(f"Failure: {str(exception)}")
    
    with open(LOG_FILE_PATH, 'a') as failure_log:
        failure_log.write(f'{datetime.datetime.now()} - Failure: {str(exception)}\n')