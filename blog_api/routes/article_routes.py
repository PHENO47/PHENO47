from flask import Blueprint
from controllers.article_controller import *

bp = Blueprint("articles", __name__)

bp.route("/api/articles", methods=["POST"])(create)
bp.route("/api/articles", methods=["GET"])(get_all)
bp.route("/api/articles/<int:id>", methods=["GET"])(get_one)
bp.route("/api/articles/<int:id>", methods=["PUT"])(update)
bp.route("/api/articles/<int:id>", methods=["DELETE"])(delete)
bp.route("/api/articles/search", methods=["GET"])(search)