from agents import Agent, Runner, OpenAIChatCompletionsModel,function_tool,set_tracing_disabled,ModelSettings
from openai import AsyncClient
from dotenv import load_dotenv
import os
from agents import enable_verbose_stdout_logging

# enable_verbose_stdout_logging()
load_dotenv()
set_tracing_disabled(disabled=True)

google_api_key = os.getenv("GEMINI_API_KEY")


client = AsyncClient(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
    
@function_tool
def get_weather(city: str) -> str:
    return f"The current weather in {city} is sunny with a temperature of 25°C."
@function_tool
def get_weather_karachi(city: str) -> str:
    return f"Weather in {city} Sunshine and gentle breeze Nature's warm embrace."
@function_tool
def supports_information(city:str) -> str:
    return "This tool provides information about the current weather{city} in a specified city."

agent = Agent(
    name="Assistant", 
    instructions="you are helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client),
    tools=[get_weather, get_weather_karachi,supports_information],
    #restricted the behavior of the agent to use only one tool at a time
    # tool_use_behavior="stop_on_first_tool",
    # model_settings=ModelSettings(tool_choice="auto")
    # model_settings=ModelSettings(tool_choice="required",)
    # model_settings=ModelSettings(tool_choice="none")
    model_settings=ModelSettings(parallel_tool_calls=False,)

)

# query = input("enter your query:")
result = Runner.run_sync(agent, "what is the weather in karachi and lahore and related to supports information",max_turns=3)
    
print(result.final_output)
