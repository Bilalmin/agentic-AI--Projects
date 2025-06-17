from fastapi import FastAPI
from pydantic import BaseModel

class MessageInput(BaseModel):
    role: str
    content: str
class ChatInput(BaseModel):
    # message: str
    #[{"role": "user", "content": "Hello, how are you?"}]
    # message: list[dict]
    messages: list[MessageInput]

app = FastAPI()


@app.get("/")
def hello_message():
    print("Hello world")
    return {"message":"hello"}


@app.post("/chat/start")
def start_chat(input: ChatInput):
    print("Data received", input)
    #business logic
    #agentic logic
    return {"message:": "pydantic data validation"}

