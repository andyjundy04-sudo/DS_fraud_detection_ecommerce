# transformers.py

import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class DateTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, col):
        self.col = col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        tm = pd.to_datetime(X[self.col], errors='coerce')

        X['month'] = tm.dt.month
        X['day'] = tm.dt.dayofweek
        X['hour'] = tm.dt.hour

        return X.drop(columns=[self.col])
