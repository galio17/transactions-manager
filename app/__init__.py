from flask import Flask, request
from flask_mongoengine import MongoEngine

from .routes import routes


def create_app(config_filename=None):
  app = Flask(__name__)
  app.config['MONGODB_SETTINGS'] = {
      "db": "transactions-cnab",
  }

  if config_filename:
    app.config.update(config_filename)
  
  db = MongoEngine(app)

  app.register_blueprint(routes)

  return app
