"""
Module for handling prediction results
"""

import os
import pandas as pd
from datetime import datetime

from anomaly_mle.config import PROJECT_ROOT
from anomaly_mle.infrastructure.logging import logger

def save_results(predictions, output_file=None):
    """
    Save prediction results to a file
    
    :param predictions: numpy array with predictions
    :param output_file: path to output file
    :return: path to the saved file
    """
    results_dir = os.path.join(PROJECT_ROOT, "results")
    os.makedirs(results_dir, exist_ok=True)
    
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(results_dir, f"results_{timestamp}.csv")
    
    results_df = pd.DataFrame({
        'prediction': predictions,
        'label': ['normal' if prediction == 1 else 'anomaly' for prediction in predictions]
    })
    
    anomalies = sum(predictions == -1)
    normal = sum(predictions == 1)
    total = len(predictions)
    
    results_df.to_csv(output_file, index=False)

    stats_file = output_file.replace('.csv', '_stats.txt')
    with open(stats_file, 'w') as f:
        f.write(f"Total predictions: {total}\n")
        f.write(f"Normal samples: {normal} ({normal/total*100:.2f}%)\n")
        f.write(f"Anomalies detected: {anomalies} ({anomalies/total*100:.2f}%)\n")
    
    logger.info(f"Results saved to {output_file}")
    logger.info(f"Statistics saved to {stats_file}")
    
    return output_file 