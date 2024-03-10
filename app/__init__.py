from fastapi import FastAPI
from pydantic import BaseModel

from .services import analyze_input
from .chat import chatbot
from .db import get_user_history, save_user_history

app = FastAPI()



# ** API to chat with the model **
class Query(BaseModel):
    question: str

@app.post("/api/chat/{uid}")
def chat(uid: int, question: Query):
    # Get the history for the user, or an empty list if it's their first message
    # history = user_histories.get(uid, [])
    history = get_user_history(uid)

    result = chatbot(question.question, history)

    new_chat = []

    new_chat.append({
        "role": "user",
        "parts": [question.question]
    })
    new_chat.append({
        "role": "model",
        "parts": [result]
    })


    # Store the updated history back in the dictionary
    save_user_history(uid, new_chat)

    return {"userID": uid, "response": result}


# ** API to get user history **

@app.get("/api/history/{uid}")
def user_history(uid: int):
    history = get_user_history(uid)
    return history

# ** API to get user sentiment record**

@app.get("/api/user_sentiment/{uid}")
def user_sentiment(uid: int):
    history = get_user_history(uid)
    sentiment_record = []
    for chat in history:
        while chat['role'] == 'user':
            sentiment = analyze_input(chat['parts'][0])
            sentiment_record.append(sentiment['sentiment'])
            break
    
    return sentiment_record


