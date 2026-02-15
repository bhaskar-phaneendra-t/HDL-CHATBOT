from sqlalchemy import text
from db.database import engine

with engine.connect() as conn:
    conn.execute(text("ALTER TABLE messages ADD COLUMN chat_id INT;"))
    conn.commit()

print("✅ chat_id column added successfully")
