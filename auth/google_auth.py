import os
import requests
import streamlit as st
from google_auth_oauthlib.flow import Flow
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
REDIRECT_URI = "https://hdl-chatbot-bhasphanikarindra3.streamlit.app/"# this is used by me for deploying

#REDIRECT_URI = "http://localhost:8501/"# this is for the local machine

def google_login():
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": client_id,
                "client_secret": client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [REDIRECT_URI],
            }
        },
        scopes=[
            "openid",
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
        ],
        redirect_uri=REDIRECT_URI,
    )

    # ---------------------------
    # STEP 1: Redirect to Google
    # ---------------------------
    if "code" not in st.query_params:
        auth_url, _ = flow.authorization_url(
            access_type="offline",
            prompt="consent",
        )
        return auth_url, None

    # ---------------------------
    # STEP 2: Handle Google redirect
    # ---------------------------
    auth_code = st.query_params["code"]

    # Build full redirect URL manually
    authorization_response = f"{REDIRECT_URI}?code={auth_code}"

    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    # 🔥 CRITICAL: clear query params immediately
    st.query_params.clear()

    userinfo = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {credentials.token}"},
        timeout=10,
    ).json()

    return None, {
        "email": userinfo["email"],
        "name": userinfo.get("name", ""),
        "picture": userinfo.get("picture", ""),
    }
