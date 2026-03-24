import sqlite3
from config import DATABASE

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            contenu TEXT,
            auteur TEXT NOT NULL,
            date TEXT,
            categorie TEXT,
            tags TEXT
        )
    ''')
    conn.commit()
    conn.close()