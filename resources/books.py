from flask_restplus import Resource
from flask import request

from resources.api import api as book_api

@book_api.route("/")
@book_api.doc("list of Books")
class Books(Resource):
  def get(self):
    return "welcome to the Book List"
