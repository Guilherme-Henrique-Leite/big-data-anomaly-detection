"""
Map of pipeline step names to their classes
"""

from sklearn.preprocessing import (
    StandardScaler,
    QuantileTransformer,
    PolynomialFeatures
)


TRANSFORMER_MAP = {
    "StandardScaler": StandardScaler,
    "QuantileTransformer": QuantileTransformer,
    "PolynomialFeatures": PolynomialFeatures,
}