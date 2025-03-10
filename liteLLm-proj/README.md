crate flow with crewai crewai create flow <project_name>
change current directory and open this project on cursor ai (IDE) a. cd <project_name> b. cursor . or code .
create src/<project_name>/main1.py
replace <project_name> place holder with your project name.
from crewai.flow import Flow, listen, start
from litellm import completion

class LiteLmmFlow(Flow):

    @start()
    def start_function(self):
        output = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
            {'role':'user',
             'content':'who is the founder of Pakistan?'}
        ])
        return output['choices'][0]['message']['content']

def run_litellm_flow():
    obj = LiteLmmFlow()
    result = obj.kickoff()
    print(result)