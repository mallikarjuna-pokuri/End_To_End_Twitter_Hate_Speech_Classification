import os
import logger
import pandas as pd
from src.config.configuration import ModelEvaluateConfig
import joblib


class ModelEvaluate:
    def __init__(self,config:ModelEvaluateConfig) -> None:
        self.config = config
    def run(self):
        try:
            test_df = pd.read_csv(self.config.test_data_path,index = False,header=False)
            X_test = test_df[:,0]
            y_test = test_df[:,1]
            model = joblib.load(self.config.model_path)
            result = model.evaluate(X_test,y_test)
            logger(f"model evaluated with accuracy {result[0]} and loss {result[1]}")
        except Exception as e:
            raise e