import sqlite3

conn = sqlite3.connect("interview_data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_name TEXT,
    role TEXT,
    question TEXT,
    answer TEXT,
    score TEXT,
    feedback TEXT
)
""")

conn.commit()

def save_interview(candidate_name, role, question, answer, score, feedback):
    cursor.execute("""
    INSERT INTO interviews
    (candidate_name, role, question, answer, score, feedback)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (candidate_name, role, question, answer, score, feedback))

    conn.commit()