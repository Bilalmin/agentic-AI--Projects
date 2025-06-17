from fastapi import FastAPI
from pydantic import BaseModel


class MessageInput(BaseModel):
    role: str
    content: str

class ChatInput(BaseModel):
    #[{"role": "user", "content": "hello world"}]
    messages: list[dict]


#create the instance of the FastAPI class

app = FastAPI()

@app.get("/chat")
def hello_message():
    # print("hello world")
    return {"message":"online class data science"}



@app.post("/health")
def health_check(input: ChatInput):
    # print("data received", input)
    #buisnes logic
    #business logic
    
    return {"data receiver": input}
