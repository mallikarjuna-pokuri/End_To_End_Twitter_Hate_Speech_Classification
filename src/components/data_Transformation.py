import os
from src.utils.common import get_size
from src.entity.config_entity import DataTransformationConfig
from pathlib import Path
from logger import logging
import tensorflow as tf
import nltk
from nltk.corpus import stopwords
import pandas as pd
from src.utils.common import transformed_text,tokenized_text
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np
import joblib
import keras

nltk.download('punkt')
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    def transform_data(self):
        try:
            print("started")
            nltk.download('stopwords')
            stop_words = stopwords.words('english')
            with open(os.path.join(self.config.root_dir,"stopwords.txt"),"w"):
                f.write(stop_words)
            df = pd.read_csv(self.config.local_data_file)
            logging(f"Twitter data read successfully of shape {df.shape}")
            df['processed_text'] = df.tweet.apply(lambda x :transformed_text(x))
            logging("Removed stop words and punctuations")
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(df.processed_text)
            with open(os.path.join(self.config.root_dir,"tokenizer.pkl"),"wb") as f:
                joblib.dump(tokenizer,f)
            vocab_size = len(tokenizer.word_index)+1
            logging(f"Vocabulary size of tokenizer is {vocab_size}")
            tokenized_text = tokenizer.texts_to_sequences(df.processed_text)
            max_len = max(len(seq) for seq in tokenized_text)
            padded_tokenized_text = pad_sequences(tokenized_text, maxlen = max_len,padding = 'post')
            labels = to_categorical(df['class'], num_classes=3)
            df2 = pd.DataFrame([padded_tokenized_text,labels])
            train,test= train_test_split(df2)
            train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False,Header = False)
            test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index = False,Header = False)
        except Exception as e:
            raise Exception