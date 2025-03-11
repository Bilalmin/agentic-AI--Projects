from crewai.flow import Flow, listen, start
from litellm import completion



class litellm1(Flow):
    @start()
    def start_function(self):
        output = completion(
            model = "gemini/gemini-1.5-flash",
            messages=[
                {
                "role": "user",
                "content": "who is the founder of pakistan"
            }
            
        ])
        return output['choices'][0]['message']['content']

def run_litellm_flow():
    flow = litellm1()
    result = flow.kickoff()
    print(result)