<h1 align="center"> 📧 Gmail Assistant </h1>
<h3 align="center'> AI-powered Gmail assistant for reading, searching, sending, and managing emails efficiently. </h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=black&labelColor=white&color=red" />
  <img src="https://img.shields.io/badge/Agno-43B02A?style=for-the-badge&logo=Agno&logoColor=black&labelColor=white&color=yellow" />
  <img src="https://img.shields.io/badge/Groq-234452?style=for-the-badge&logoColor=black&labelColor=white&color=brown" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=black&labelColor=white&color=orange" />
</p>

---

## 🚀 Project Overview
- The Gmail Assistant is an AI-driven application that helps users interact with their Gmail accounts using natural language. Built with Agno AI (formerly Phidata), Groq LLM, and Streamlit. 
- The assistant utilizes Google OAuth 2.0 for authentication and interacts with the Gmail API to fetch and manage emails securely.
- It allows users to:
    1. 📩 Read emails – Retrieve and summarize recent emails.
    2. 🔍 Search emails – Find emails based on keywords, sender, or date.
    3. ✉ Send emails – Compose and send emails via Gmail.
    4. 📂 Manage emails – Handle spam, categorize emails, and more.



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
```
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
```


## 🚀 Setup & Installation

### Prerequisites
Gmail API enabled with OAuth 2.0 credentials
Pipenv (for managing dependencies)

## Installation Steps

### 1️⃣ Clone the repository:

```sh
git clone https://github.com/yourusername/Gmail-Assistant-Project.git](https://github.com/Dhanush-Raj1/Gmail-Assistant-Project.git
cd Gmail-Assistant-Project
```

### 2️⃣ Set up a virtual environment:

```sh
pipenv install
pipenv shell
```

### 3️⃣ Configure environment variables:

Create a .env file and add your credentials:
```
GROQ_API_KEY=your_groq_api_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_PROJECT_ID=your_project_id
GOOGLE_REDIRECT_URI=your_redirect_uri
HF_TOKEN_LLAMA=your_huggingface_token
```

### 4️⃣ Run the application:

```
streamlit run main.py
```



## 📝 Usage Guide  

### 🔹 Step 1: Authenticate with Gmail  
- Click on the **"Authenticate with Gmail"** button.  
- Sign in with your **Google account** and grant the necessary permissions.  

### 🔹 Step 2: Perform Actions  

### **Chat with the assistant in natural language*
- Chat with the gmail assistant in natural langugage. Example:
   1. Give me the summary of my latest emails
   2. Find me the emails related to invoice
   3. Send an email to <sender_email id> conveying that I'm free on wednesday at 4.30pm and ready to meet him about the investment.
   4. What is the latest email about AI news? 

#### 📩 **Retrieve Latest Emails**  
- Click **"Fetch Latest Emails"** to get the most recent messages.  
- The assistant will return **Sender, Subject, and Received Time** (converted to IST).  

#### 🔍 **Search Emails**  
- Enter a **keyword, sender email, or date** in the search bar.  
- The assistant will list matching emails from the **Inbox and Spam folders**.  

#### ✉️ **Send an Email**  
- Enter the **recipient’s email**, **subject**, and **message body**.  
- The assistant will send the email with a **structured format and a signature**.  

#### 📂 **Manage Emails**  
- View, organize, and handle emails based on **priority, sender, or time received**.  
- Spam detection and handling for **junk or phishing emails**.  


---


## 🖼️ Screenshots
✨ Authentication Page

✨ Chatbot Interface

✨ Email Summarization



## 🚀 Future Enhancements  

🔹 **Memory-Based Conversations**  
- Store chat history using a vector database (FAISS or PostgreSQL).  

🔹 **Priority-Based Email Sorting**  
- Categorize emails using **AI-driven importance detection**.  

🔹 **Sentiment Analysis for Emails**  
- Analyze email tone (positive, neutral, negative) before responding.  

🔹 **Voice Commands Integration**  
- Allow users to interact via voice instead of text input.  

🔹 **Multi-Account Support**  
- Enable switching between multiple Gmail accounts.  

🔹 **Mobile App Version**  
- Build a **React Native or Flutter app** for better mobile accessibility.  

---

💡 Have an idea? Feel free to contribute or open an issue! 🚀  




## 🤝 Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## 📜 License
This project is licensed under the MIT License.
