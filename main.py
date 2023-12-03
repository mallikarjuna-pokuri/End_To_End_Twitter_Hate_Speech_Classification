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
            return "Given Tweet is Predicted as Hate Speech"
    elif val==1:
        return "Given Tweet is Predicted as Offensive Language"
    else:
        return "Given Tweet Predicted as neither Hate Speech nor Offensive Language"
