from crewai.flow import Flow, listen, start
from multi_agent.crews.dev_crew.dev_crew1 import DevCrew

class DevFlow(Flow):
    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
            inputs={
                "problem":"write ab additon function in python",

            }
        )
        return output.raw
    
def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)
