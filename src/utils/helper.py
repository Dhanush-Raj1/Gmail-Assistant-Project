import os 
import json, pickle 
import streamlit as st
from google_auth_oauthlib.flow import InstalledAppFlow


# Function to handle Gmail Authentication
def authenticate_gmail():
    try:
        # pick credentials source based on deployment environment
        if "client_id" in st.secrets:
            # build credentials.json structure
            credentials_dict = {
                "installed": {
                    "client_id": st.secrets["client_id"],
                    "project_id": st.secrets["project_id"],
                    "auth_uri": st.secrets["auth_uri"],
                    "token_uri": st.secrets["token_uri"],
                    "client_secret": st.secrets["client_secret"],
                    "redirect_uris": st.secrets["redirect_uris"]
                }
            }
            redirect_uris = st.secrets["redirect_uris"]
            # write to a temporary credentials file
            os.makedirs("credentials", exist_ok=True)        
            cred_path = "credentials/temp_credentials.json"
            with open(cred_path, "w") as f:
                json.dump(credentials_dict, f)
        # if the app runs locally
        else: 
            cred_path = "credentials/credentials.json"


        # choose redirect URI based on environment 
        if "STREAMLIT_RUNTIME" in os.environ:
            chosen_redirect_uri = redirect_uris[1]
        else: 
            chosen_redirect_uri = redirect_uris[0]


        # Start OAuth flow 
        flow = InstalledAppFlow.from_client_secrets_file(
            cred_path, 
            #["https://www.googleapis.com/auth/gmail.readonly"]
            scopes=[
                "https://www.googleapis.com/auth/gmail.readonly",
                "https://www.googleapis.com/auth/gmail.send",
                "https://www.googleapis.com/auth/gmail.modify",
                "https://www.googleapis.com/auth/gmail.compose"
            ], 
            redirect_uri=chosen_redirect_uri,
        )

        # works in both local + Streamlit Cloud with proper redirect
        if "STREAMLIT_RUNTIME" in os.environ:
            creds = flow.run_local_server(port=8501, open_browser=False)
        else:
            creds = flow.run_local_server(port=0)

        # Save credentials
        with open("credentials/gmail_token.json", "w") as token:
            token.write(creds.to_json())

        st.session_state["gmail_creds"] = creds
        st.success("✅ Successfully authenticated with Gmail!")
        st.session_state["auth_status"] = True  # Store authentication status
        
        return creds 
    
    except Exception as e:
        st.error(f"Authentication failed: {e}") 