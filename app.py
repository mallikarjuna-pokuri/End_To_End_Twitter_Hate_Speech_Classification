from fastapi import FastAPI, Request
import uvicorn
from src.config.configuration import ConfigurationManager
from main import predicted_tweet_type
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


config = ConfigurationManager()
model_evaluate_config = config.model_evaluate_config()


app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_form(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define the route to handle form submission
@app.post("/predict")
async def submit_text(textInput: str):
    # Perform any processing with the submitted text here
    # For demonstration purposes, just printing the text
    print(f"Submitted Text: {textInput}")
    result = predicted_tweet_type(textInput)
    return {"result":result}
'''
@app.get('/',tags = ["index"])
def welcome():
    return {"data":"Welcome to Twitter Hate Speech Classification"}

@app.post('/predict/{tweet}',tags=["predict2"])

def predict2(tweet:str):
    result = predicted_tweet_type(tweet)
    return {"result":result}
'''
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)