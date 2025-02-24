import os 
import sys
from typing import List
from textwrap import dedent
from dataclasses import dataclass

from agno.agent import Agent, RunResponse
from agno.models.huggingface import HuggingFace
from agno.models.groq import Groq
from agno.tools.gmail import GmailTools

from src.utils.exception import CustomException

from dotenv import load_dotenv
load_dotenv()

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN_LLAMA")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")


@dataclass
class GmailAssistant():
    """
    Initializes and return a Gmail Assistant
    Executing tasks using the assistant
    """

    def setup_gmail_agent()->Agent:
        try:
            agent = Agent(name="Gmail Agent",
                        model=Groq(id="llama-3.3-70b-versatile",
                                   response_format={"type": "json_object"}),
                        #model=HuggingFace(id="meta-llama/Llama-3.2-3B-Instruct"),
                        tools=[GmailTools()],
                        description=dedent("""\
                                            You are an AI-powered Gmail assistant that can read, search, send, and manage emails.
                                            Your role is to assist users in handling their Gmail efficiently.
                                            Your expertise includes:
                                            1. Reading emails with attention to detail.
                                            2. Sending emails with structured content.
                                            3. Searching emails using keywords, date, or sender.
                                            4. Managing emails effectively."""),
                        # instructions=dedent("""\
                        #                 **Instructions:**
                        #                 - Return email summaries with sender, subject, and date.
                        #                 - When sending emails, include subject, content, and a signature.
                        #                 - Fetch latest emails sorted by date."""),
                        instructions=dedent("""\
                                            Instructions for handling tasks:

                                            1. **Reading Emails**:
                                                - Return details in the format:
                                                  - **Sender Email**: {email of sender}
                                                  - **Summary**: {brief but comprehensive summary}
                                                  - **Received Time**: {converted IST timestamp}
                                                - Convert UTC time to IST (UTC+5:30).

                                            2. **Sending Emails**:
                                                - Ensure the recipient email is valid.
                                                - Format:
                                                  - **Subject**: {clear and brief}
                                                  - **Content**: {all necessary details}
                                                  - **Signature**: "Best Regards"

                                            3. **Searching Emails**:
                                                - Search by:
                                                  - **Email ID**
                                                  - **Email Content**
                                                  - **Date**
                                                - Look in both **Inbox and Spam**.
                                                - Include both received and sent emails.

                                            4. **Fetching Latest Emails**:
                                                - Return a numbered list:
                                                  - **Sender Email**
                                                  - **Brief Summary**
                                                  - **Received Time** (in IST)
                                                - Sort by latest first. 

                                            5. **Fetching Emails from a Specific User**:
                                                - Search all emails from a given sender.
                                                - Convert received time to IST.
                                                - Return a numbered list sorted by date (latest first)."""),
                        add_history_to_messages=False,
                        reasoning=True,
                        structured_outputs=True,
                        show_tool_calls=False,
                        markdown=True,)
            return agent
        
        except Exception as e:
            raise CustomException(e, sys)
    
    
    def perform_task(agent: Agent, task: str)->str:
        try:
            # # Get the streamed response
            # response_stream: Iterator[RunResponse] = agent.run(task, stream=True)
            
            # # Collect and format the streamed content
            # full_response = []
            # for chunk in response_stream:
            #     full_response.append(chunk.content)
            #     # Print each chunk in real-time (for terminal)
            #     pprint_run_response(chunk, markdown=True)
            
            # return "".join(full_response)
            response: RunResponse = agent.run(task)
            return response.content

        except Exception as e:
            raise CustomException(e, sys)
        

