from agents import Agent, Runner, OpenAIChatCompletionsModel,set_tracing_disabled
from openai import AsyncClient
from dotenv import load_dotenv
import os
from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()
load_dotenv()
# set_tracing_disabled(disabled=True)

google_api_key = os.getenv("GEMINI_API_KEY")


client = AsyncClient(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    
    
)
    
agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)
)

# query = input("enter your query:")
result = Runner.run_sync(agent,"who is the president of Pakistan?") 
    
print(result)
