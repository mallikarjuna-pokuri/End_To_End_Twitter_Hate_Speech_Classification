from nltk.corpus import stopwords
from keras.models import load_model
from keras.utils import pad_sequences
import os
import joblib
from src.utils.common import predict_tweet


stop_words = set(stopwords.words('english'))
model = load_model(os.path.join("artifacts","model.h5"))
tokenizer = joblib.load(os.path.join("artifacts","tokenizer.pkl"))


def predicted_tweet_type(tweet):
    tweet = str(tweet)
    val = predict_tweet(tweet,model,tokenizer,stop_words)
    if val==0:
            return "Hate Speech"
    elif val==1:
        return "Offensive Language"
    else:
        return "Neither"
