from sqlalchemy.orm import Session
from db.models import User, Chat, Message

# -------------------------
# USER
# -------------------------
def get_or_create_user(db: Session, email: str, name: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        user = User(email=email, name=name)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


# -------------------------
# CHATS
# -------------------------
def create_chat(db: Session, user_id: int, title: str = "New Chat"):
    chat = Chat(user_id=user_id, title=title)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def get_user_chats(db: Session, user_id: int):
    return (
        db.query(Chat)
        .filter(Chat.user_id == user_id)
        .order_by(Chat.created_at.desc())
        .all()
    )

def rename_chat(db, chat_id: int, new_title: str):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if chat:
        chat.title = new_title[:50]  # limit length
        db.commit()

# -------------------------
# MESSAGES
# -------------------------
def get_chat_messages(db: Session, chat_id: int):
    return (
        db.query(Message)
        .filter(Message.chat_id == chat_id)
        .order_by(Message.created_at)
        .all()
    )


def save_message(db: Session, user_id: int, chat_id: int, role: str, content: str):
    msg = Message(
        user_id=user_id,
        chat_id=chat_id,
        role=role,
        content=content
    )
    db.add(msg)
    db.commit()
