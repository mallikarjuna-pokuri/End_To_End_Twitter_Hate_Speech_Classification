import os
import logger
import pandas as pd
from src.config.configuration import ModelTrainerConfig,ModelTrainerParmas
from tensorflow.keras.layers import Embedding,Dense,Flatten,BatchNormalization,Dropout,LSTM
from tensorflow.keras import Sequential

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig,params:ModelTrainerParmas):
        self.config = config
        self.params =params
    def run(self):
        try:
            train_df = pd.read_csv(self.config.train_data_path,header = False,index = False)
            logger(f"Loaded training data Successfully with shape {train_df.shape}")
            model = Sequential([
                    Embedding(self.params.vocab_size+1,100,input_length = self.params.max_len,mask_zero = True),
                    LSTM(256),
                    Dense(1,activation = 'sigmoid')
                ])
            X_train = train_df[:,0]
            y_train = train_df[:,1]
            model.compile(loss = 'binary_crossentropy',optimizer = 'adam',metrics = ['accuracy'])
            history = model.fit(X_train,y_train,epochs = 10,batch_size = 32)
            logger(f"model trained successfully with accuracy {history.history[accuracy]} and loss {history.history['loss']}")
            
        except Exception as e:
            raise e