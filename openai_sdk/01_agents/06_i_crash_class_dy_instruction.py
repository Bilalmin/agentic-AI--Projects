from agents import Agent, Runner, OpenAIChatCompletionsModel,function_tool,set_tracing_disabled
from openai import AsyncClient
from dotenv import load_dotenv
import os
# from agents import enable_verbose_stdout_logging
# enable_verbose_stdout_logging()

load_dotenv()

set_tracing_disabled(disabled=True)

google_api_key = os.getenv("GEMINI_API_KEY")


client = AsyncClient(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
    

def get_system_prompt(context,agent):
    print("[context]:", context),
    print("[agent]:", agent)
    return"you are helpful assistant that can anser the question and help with task"

agent = Agent(
    name="Assistant", 
    instructions=get_system_prompt,
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client),

)

# query = input("enter your query:")
result = Runner.run_sync(agent,"hi") 
    
print(result.final_output)
