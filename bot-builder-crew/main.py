from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import BotTasks
from agents import BotAgents

tasks = BotTasks()
agents = BotAgents()

print("## Welcome to the Bot Crew")
print('-------------------------------')
bot = input("What is the Discord Bot you would like to build?\n")

# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
code_bot = tasks.code_task(senior_engineer_agent, bot)
review_bot = tasks.review_task(qa_engineer_agent, bot)
approve_bot = tasks.evaluate_task(chief_qa_engineer_agent, bot)

# Create Crew responsible for Copy
crew = Crew(
	agents=[
		senior_engineer_agent,
		qa_engineer_agent,
		chief_qa_engineer_agent
	],
	tasks=[
		code_bot,
		review_bot,
		approve_bot
	],
	verbose=True
)

game = crew.kickoff()


# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the Bot:")
print(bot)
