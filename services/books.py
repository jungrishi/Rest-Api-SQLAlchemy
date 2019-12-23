from models.books import Book
from services.base_service import BaseService

class BookService(BaseService):
  model = Book
