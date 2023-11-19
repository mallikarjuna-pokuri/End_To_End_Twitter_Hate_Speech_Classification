import os
from box.exceptions import BoxValueError
import yaml
from logger import logging
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import re
import nltk
from nltk.corpus import stopwords
from keras.models import load_model
from keras.utils import pad_sequences
import numpy as np




@ensure_annotations
def transformed_text(text:str,stop_words:set)-> str:
    """removes unneccassary characters and stop words

    Args:
        text (str): str of the twitter tweet
        stop_words (list): list of all the stop words provided by nltk

    Returns:
        str: transformed text
    """
    text = remove_url(text)
    text = remove_punctuations(text)
    text = remove_entity(text)
    text = remove_stopwords(text,stop_words)
    return text
@ensure_annotations
def tokenized_text(text:str,word_index):
    """removes unneccassary characters and stop words

    Args:
        text (str): str of the twitter tweet
        word_index (list): vocabulary list of tokenizer with indexes

    Returns:
        str: transformed tokenized text
    """
    x = []
    for t in text:
        if t in word_index:
            x.append(word_index[t])
    return x
def remove_user_tag(raw_text):
    regex = r"@([^ ]+)"
    text = re.sub(regex,"", raw_text)
    return text
def remove_url(raw_text):
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)\
    (?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    text = re.sub(url_regex, '', raw_text)

    return text
def remove_entity(raw_text):
    entity_regex = r"&[^\s;]+;"
    text = re.sub(entity_regex, "", raw_text)
    return text
def remove_punctuations(raw_text):
    text = re.sub('[^a-z^A-Z]',' ',raw_text)
    text = re.sub(' \s+',' ',text)
    text = text.lower()
    return text
def remove_stopwords(raw_text,stop_words):
    tokenize = nltk.word_tokenize(raw_text)
    text = [word for word in tokenize if not word in stop_words and len(word)>2]
    text = " ".join(text)
    return text
def predict_tweet(tweet,model,tokenizer,stop_words):
    transformed_tweet = transformed_text(tweet,stop_words) 
    tokenized_tweet = tokenizer.texts_to_sequences([transformed_tweet])
    padded_tokenized_tweet = pad_sequences(tokenized_tweet, maxlen = 24,padding = 'post')
    val = np.argmax(model.predict(padded_tokenized_tweet,verbose = 0)) 
    # 0 hate speech 1 offensive language 2 neither
    return val 
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
