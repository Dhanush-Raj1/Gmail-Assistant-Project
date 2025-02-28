<h1 align="center"> 📧 Gmail Assistant </h1>
AI-powered Gmail assistant for reading, searching, sending, and managing emails efficiently.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=black&labelColor=white&color=red" />
  <img src="https://img.shields.io/badge/Agno-43B02A?style=for-the-badge&logo=Agno&logoColor=black&labelColor=white&color=yellow" />
  <img src="https://img.shields.io/badge/Groq-234452?style=for-the-badge&logoColor=black&labelColor=white&color=brown" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=black&labelColor=white&color=orange" />
</p>

---

## 🚀 Project Overview
The Gmail Assistant is an AI-driven application that helps users interact with their Gmail accounts using natural language. Built with Agno AI (formerly Phidata), Groq LLM, and Streamlit , it allows users to:

📩 Read emails – Retrieve and summarize recent emails.
🔍 Search emails – Find emails based on keywords, sender, or date.
✉ Send emails – Compose and send emails via Gmail.
📂 Manage emails – Handle spam, categorize emails, and more.
The assistant utilizes Google OAuth 2.0 for authentication and interacts with the Gmail API to fetch and manage emails securely.



## 🎯 How the Project Works
User Authentication:

The user authenticates with Gmail via OAuth 2.0.
The app retrieves an access token to interact with Gmail services.
Query Processing:

The user enters a request (e.g., "Find my latest emails from John").
The input is processed and passed to the Groq-powered LLM.
AI-driven Response:

The AI interprets the query, calls the Gmail API, and retrieves relevant data.
A structured response is generated and displayed in the UI.
Chatbot UI:

The web-based UI (built with Streamlit) allows users to interact seamlessly.
User queries appear on the right, and assistant responses appear on the left, resembling a real chatbot.


## 🛠️ Tech Stack
Technology	Purpose
Python	Backend development
Streamlit	Web UI
Agno AI	AI model framework
Groq LLM	Language model for email processing
Hugging Face	Alternative LLM integration
Google OAuth 2.0	User authentication
Gmail API	Email retrieval and management


## 📂 Project Structure
bash
Copy
Edit
📂 Gmail-Assistant
├── 📂 static                 # Static assets (images, styles)
│   ├── gmail-logo.png         # Logo for UI
├── 📂 rough                   # Research and rough work purpose
    ├── rough.py               # rough python file 
├── 📂 src                     # Source code
│   ├── assistant_builder.py   # Core AI logic for Gmail operations
│   ├── 📂 utils
│   │   ├── exception.py     # Custom exception handling
|   |   ├── helper.py        # Google Oauth authentication
├── Pipfile                  # Dependencies (Pipenv)
├── Pipfile.lock             # Locked dependencies
├── requirements.txt         # List of required libraries, modules, dependencies
├── .env                     # Environment variables (OAuth keys)
├── README.md                # Project documentation



## 🖼️ Screenshots
✨ Authentication Page

✨ Chatbot Interface

✨ Email Summarization



## 🚀 Setup & Installation
### Prerequisites
Gmail API enabled with OAuth 2.0 credentials
Pipenv (for managing dependencies)

### Installation Steps
1️⃣ Clone the repository:

sh
Copy
Edit
git clone https://github.com/your-username/gmail-assistant.git
cd gmail-assistant
2️⃣ Set up a virtual environment:

sh
Copy
Edit
pipenv install
pipenv shell
3️⃣ Configure environment variables:

Create a .env file and add your credentials:
sh
Copy
Edit
GROQ_API_KEY=your_groq_api_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_PROJECT_ID=your_project_id
GOOGLE_REDIRECT_URI=your_redirect_uri
HF_TOKEN_LLAMA=your_huggingface_token
4️⃣ Run the application:

sh
Copy
Edit
streamlit run main.py
🚀 Deployment
To deploy using Docker, follow these steps:

1️⃣ Build the Docker image:

sh
Copy
Edit
docker build -t gmail-assistant .
2️⃣ Run the container:

sh
Copy
Edit
docker run -p 8501:8501 gmail-assistant


## 🤝 Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## 📜 License
This project is licensed under the MIT License.
