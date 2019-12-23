from flask_restplus import Resource
from flask import request

from resources.api import api as book_api
from services.books import BookService

@book_api.route("/")
@book_api.doc("list of Books")
class Books(Resource):
  def get(self):
    data = BookService.fetch(request.args)
    return data
