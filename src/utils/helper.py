import streamlit as st
from google_auth_oauthlib.flow import InstalledAppFlow


# Function to handle Gmail Authentication
def authenticate_gmail():
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", ["https://www.googleapis.com/auth/gmail.readonly"]
        )
        creds = flow.run_local_server(port=0)
        st.session_state["gmail_creds"] = creds
        st.success("✅ Successfully authenticated with Gmail!")
        st.session_state["auth_status"] = True  # Store authentication status
    except Exception as e:
        st.error(f"Authentication failed: {e}")