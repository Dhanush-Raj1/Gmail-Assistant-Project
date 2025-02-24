from src.main import GmailAssistant
from agno.utils.pprint import pprint_run_response

agent = GmailAssistant.setup_gmail_agent()

response = GmailAssistant.perform_task(agent=agent, task="Give me the summary of my latest email in under 50 words")
print(response)