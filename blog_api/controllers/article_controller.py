from flask import request, jsonify
from models.article_model import *

def create():
    data = request.json

    if not data.get("titre") or not data.get("auteur"):
        return jsonify({"error": "Titre et auteur obligatoires"}), 400

    article_id = create_article(data)
    return jsonify({"message": "Article créé", "id": article_id}), 201


def get_all():
    return jsonify(get_articles())


def get_one(id):
    article = get_article(id)
    if not article:
        return jsonify({"error": "Not found"}), 404
    return jsonify(article)


def update(id):
    update_article(id, request.json)
    return jsonify({"message": "Article modifié"})


def delete(id):
    delete_article(id)
    return jsonify({"message": "Article supprimé"})


def search():
    query = request.args.get("query", "")
    return jsonify(search_articles(query))