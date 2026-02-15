import streamlit as st
from rag.query_engine import ask_question
from auth.google_auth import google_login
from db.crud import rename_chat

from db.database import SessionLocal
from db.crud import (
    get_or_create_user,
    create_chat,
    get_user_chats,
    get_chat_messages,
    save_message
)

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="HDL Chatbot", page_icon="🤖")
st.title("🤖 HDL Chatbot")

# -------------------------
# LOGIN
# -------------------------
if "user" not in st.session_state:
    login_url, user = google_login()

    if user:
        st.session_state.user = user
        st.query_params.clear()
        st.rerun()

    st.subheader("Login to continue")
    st.markdown(f"[🔐 Login with Google]({login_url})")
    st.stop()

# -------------------------
# DB + USER INIT
# -------------------------
db = SessionLocal()
user = st.session_state.user

user_db = get_or_create_user(
    db,
    email=user["email"],
    name=user.get("name", "")
)

st.session_state.user_id = user_db.id

# -------------------------
# SIDEBAR – CHAT LIST
# -------------------------
st.sidebar.title("💬 Your Chats")

chats = get_user_chats(db, user_db.id)

# New Chat Button
if st.sidebar.button("➕ New Chat", key="new_chat"):
    new_chat = create_chat(db, user_db.id)
    st.session_state.chat_id = new_chat.id
    st.session_state.messages = []
    st.rerun()

# Existing Chats
for chat in chats:
    if st.sidebar.button(chat.title, key=f"chat_{chat.id}"):
        st.session_state.chat_id = chat.id
        history = get_chat_messages(db, chat.id)
        st.session_state.messages = [
            {"role": m.role, "content": m.content}
            for m in history
        ]
        st.rerun()

# Ensure at least one chat exists
if "chat_id" not in st.session_state:
    first_chat = create_chat(db, user_db.id)
    st.session_state.chat_id = first_chat.id
    st.session_state.messages = []

# -------------------------
# USER HEADER
# -------------------------
col1, col2 = st.columns([1, 8])

with col1:
    if user.get("picture"):
        try:
            st.image(user["picture"], width=50)
        except:
            st.markdown("👤")
    else:
        st.markdown("👤")

with col2:
    st.success(f"Logged in as {user['email']}")

# -------------------------
# CHAT HISTORY DISPLAY
# -------------------------
if "messages" not in st.session_state:
    history = get_chat_messages(db, st.session_state.chat_id)
    st.session_state.messages = [
        {"role": m.role, "content": m.content}
        for m in history
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# CHAT INPUT
# -------------------------
user_input = st.chat_input("Ask an HDL question...")

if user_input is not None and user_input.strip() != "":
    user_input = user_input.strip()

    # -------------------------
    # SAVE USER MESSAGE
    # -------------------------
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    save_message(
        db,
        st.session_state.user_id,
        st.session_state.chat_id,
        "user",
        user_input
    )

    # -------------------------
    # AUTO-RENAME (only once)
    # -------------------------
    current_chat = next(
        (c for c in chats if c.id == st.session_state.chat_id),
        None
    )

    if current_chat and current_chat.title == "New Chat":
        title = user_input.split("?")[0][:40]
        rename_chat(db, current_chat.id, title)

    # -------------------------
    # ASSISTANT RESPONSE
    # -------------------------
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask_question(user_input)
            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    save_message(
        db,
        st.session_state.user_id,
        st.session_state.chat_id,
        "assistant",
        answer
    )

# -------------------------
# LOGOUT
# -------------------------
st.sidebar.markdown("---")
if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.rerun()
