from fastapi import FastAPI
import uvicorn
import joblib
from src.config.configuration import ConfigurationManager
from src.utils.common import transformed_text

config = ConfigurationManager()
model_evaluate_config = config.model_evaluate_config()

app = FastAPI()
model = joblib.load(model_evaluate_config.model_path)

@app.get('/',tags = ["index"])
def welcome():
    return {"data":"Welcome to Twitter Hate Speech Classification"}

@app.post('/predict/{tweet}',tags=["predict"])

def predict(tweet:str):
    processed_tweet = transformed_text(tweet)
    result = model.predict(processed_tweet)
    return {"result":result}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)