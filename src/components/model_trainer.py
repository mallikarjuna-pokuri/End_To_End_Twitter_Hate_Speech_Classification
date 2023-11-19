import os
import logger
import pandas as pd
from src.config.configuration import ModelTrainerConfig,ModelTrainerParmas
from keras.layers import Embedding,Dense,Flatten,BatchNormalization,Dropout,GRU
from keras import Sequential
import joblib

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig,params:ModelTrainerParmas):
        self.config = config
        self.params =params
    def run(self):
        try:
            train_df = pd.read_csv(self.config.train_data_path,header = False,index = False)
            logger(f"Loaded training data Successfully with shape {train_df.shape}")
            model = Sequential([
                    # embedding layer is like idk
                    Embedding(self.params.vocab_size, 300, input_length=self.params.maxlen),
                    # GRU for xxx
                    GRU(64, dropout=0.3, recurrent_dropout=0.3),
                    #normalize to prevent overfitting and faster trainign
                    BatchNormalization(),
                    # dense to connect the previous output with current layer
                    Dense(128, activation="relu"),
                    # dropout to prevent overfitting
                    Dropout(0.5),
                    # this is output layer, with 3 class (0, 1, 2)
                    Dense(3, activation="softmax"),
])

            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            X_train = train_df[:,0]
            y_train = train_df[:,1]
            model.compile(loss = 'binary_crossentropy',optimizer = 'adam',metrics = ['accuracy'])
            history = model.fit(X_train,y_train,epochs = 1,batch_size = 32)
            logger(f"model trained successfully with accuracy {history.history[accuracy]} and loss {history.history['loss']}")
            with open(self.config.model_path,"wb") as f:
                joblib.dump(model,f)
            logger(f"model saved to path {self.config.model_path}")
        except Exception as e:
            raise e