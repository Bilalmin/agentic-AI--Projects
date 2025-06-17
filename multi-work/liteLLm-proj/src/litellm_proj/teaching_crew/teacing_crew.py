from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew


@CrewBase
class TeachingCrew:
    #1. agent
    agent_config = "config/agents.yaml"
    task_config = "config/tasks.yaml"
    @agent
    def sir_zia_agent(self) -> Agent:
        return Agent(
            config = self.agent_config["sir_zia"]

        )
    #2. task
    @task
    def describe_topic_task(self) -> Task:
        return Task(
            config=self.task_config["describe_topic"]
        )
    # 3 crew
    @crew
    def teaching_crew(self) ->Crew:
        return Crew(
            agents=[self.sir_zia_agent()],
            tasks=[self.describe_topic_task()],
            verbose=True
            
        )