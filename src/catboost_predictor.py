import pandas as pd
from catboost import CatBoostClassifier

class CongestionPredictor:

    def __init__(self):
        self.model = CatBoostClassifier(verbose=0)

    def train(self, dataset_path):
        data = pd.read_csv(dataset_path)

        X = data.drop("congestion_label", axis=1)
        y = data["congestion_label"]

        self.model.fit(X, y)

    def predict(self, sample):
        prediction = self.model.predict(sample)
        return prediction
