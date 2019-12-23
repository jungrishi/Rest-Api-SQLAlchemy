from flask import Flask, Response

from config import Config
from resources.api import api
from models.db import db

def simple_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  return app

def create_app() -> Flask:
  app = simple_app()
  api.init_app(app)
  db.init_app(app)
  return app

if __name__ == '__main__':
  application = create_app()
  application.run(host=application.config.get("HOST"),port=application.config.get("port"), debug=True)
