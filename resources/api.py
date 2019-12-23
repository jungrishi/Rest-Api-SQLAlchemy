from http import HTTPStatus
from flask_restplus import Api

api = Api(
  version= "2",
  title= "API-v2",
  description="REST API v2",
  prefix = "/api/v2",
)
