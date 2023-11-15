import os
from src.utils.common import get_size
from src.entity.config_entity import DataTransformationConfig
from pathlib import Path
import logger
import tensorflow as tf
import nltk
from nltk.corpus import stopwords
import pandas as pd
from src.utils.common import transformed_text,tokenized_text
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import numpy as np


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    def transform_data(self):
        try:
            config = self.config.data_transformation
            nltk.download('stopwords')
            stop_words = stopwords.words('english')
            df = pd.read_csv(config.local_data_file)
            logger(f"Twitter data read successfully of shape {df.shape}")
            df['text'] = df.text.apply(lambda x: transformed_text(x))
            logger("Removed stop words and punctuations")
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(df['text'])
            vocab_size = len(tokenizer.word_index)
            logger(f"Vocabulary size of tokenizer is {vocab_size}")
            word_index = tokenizer.word_index
            df['text2'] = df.text.apply(lambda x: tokenized_text(x,word_index))
            max_len = 0
            for i in df.text2.tolist():
                if len(i)>max_len:
                    max_len = len(i)
            text2 = df.text2.tolist()
            text2 = np.array(text2)
            text2 = tf.keras.utils.pad_sequences(text2,maxlen = max_len,padding = 'post')
            df2 = pd.DataFrame([text2,df['target']])
            train,test= train_test_split(df2)
            train.to_csv(os.path.join(config.root_dir,"train.csv"),index = False,Header = False)
            test.to_csv(os.path.join(config.root_dir,"test.csv"),index = False,Header = False)
        except Exception as e:
            raise Exception