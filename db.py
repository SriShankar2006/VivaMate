import sqlite3

DB_NAME = "data/vivamate.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        question TEXT,
        confidence INTEGER,
        fluency INTEGER,
        clarity INTEGER,
        keywords INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_attempt(subject, question, scores, date):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO attempts
    (subject, question, confidence, fluency, clarity, keywords, date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        subject,
        question,
        scores["Confidence"],
        scores["Fluency"],
        scores["Clarity"],
        scores["Keywords"],
        date
    ))

    conn.commit()
    conn.close()
