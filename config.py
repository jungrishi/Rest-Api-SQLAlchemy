import os
import json
from typing import Type

from dotenv import load_dotenv
load_dotenv(verbose=True)

DEVELOPMENT = "development"

class BaseConfig:
  ROOT = os.path.dirname(os.path.realpath(__file__))
  FLASK_ENV = os.environ.get("FLASK_ENV", DEVELOPMENT)
  HOST = os.environ.get("HOST")
  PORT = int(os.environ.get("PORT", 5000))
  LOG_PATH = os.environ.get("LOG_PATH", "logs/my_api_log.log")
  LOG_LEVEL = os.environ.get("LOG_LEVEL", "ERROR").upper()
  DATABASE_URI = os.environ.get("DATABASE_URI")

  # with open(ROOT + '/version.txt') as f:
  #   VERSION = f.read().strip()

  if not DATABASE_URI:
    raise Exception('"DATABASE_URI" not set')

  DEBUG_SQL =False
  DATABASE_COMMIT_CONTEXT = True
  SQLALCHEMY_DATABASE_URI = DATABASE_URI
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  RESTPLUS_JSON = {}

Config = BaseConfig()




