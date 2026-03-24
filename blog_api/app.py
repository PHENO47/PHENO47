from flask import Flask
from routes.article_routes import bp
from database.db import init_db

app = Flask(__name__)

init_db()
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)