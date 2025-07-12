from agents import Agent, Runner, OpenAIChatCompletionsModel,function_tool
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
    
@function_tool
def get_weather(city: str) -> str:
    return f"The current weather in {city} is sunny with a temperature of 25°C."


agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client),
    tools=[get_weather]
)

# query = input("enter your query:")
result = Runner.run_sync(agent,"what is the weather in lahore") 
    
print(result.final_output)
