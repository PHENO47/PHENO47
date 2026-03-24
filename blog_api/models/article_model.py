from database.db import get_db
import datetime

def create_article(data):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO articles (titre, contenu, auteur, date, categorie, tags)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["titre"],
        data.get("contenu"),
        data["auteur"],
        str(datetime.datetime.now()),
        data.get("categorie"),
        ",".join(data.get("tags", []))
    ))

    conn.commit()
    article_id = cursor.lastrowid
    conn.close()
    return article_id


def get_articles():
    conn = get_db()
    articles = conn.execute("SELECT * FROM articles").fetchall()
    conn.close()
    return [dict(a) for a in articles]


def get_article(id):
    conn = get_db()
    article = conn.execute("SELECT * FROM articles WHERE id = ?", (id,)).fetchone()
    conn.close()
    return dict(article) if article else None


def update_article(id, data):
    conn = get_db()
    conn.execute("""
        UPDATE articles
        SET titre=?, contenu=?, categorie=?, tags=?
        WHERE id=?
    """, (
        data.get("titre"),
        data.get("contenu"),
        data.get("categorie"),
        ",".join(data.get("tags", [])),
        id
    ))
    conn.commit()
    conn.close()


def delete_article(id):
    conn = get_db()
    conn.execute("DELETE FROM articles WHERE id=?", (id,))
    conn.commit()
    conn.close()


def search_articles(query):
    conn = get_db()
    articles = conn.execute("""
        SELECT * FROM articles
        WHERE titre LIKE ? OR contenu LIKE ?
    """, (f"%{query}%", f"%{query}%")).fetchall()
    conn.close()
    return [dict(a) for a in articles]