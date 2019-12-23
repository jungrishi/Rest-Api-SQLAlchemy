from sqlalchemy import Column, Integer, String, DateTime
from uuid import UUID, uuid4
from sqlalchemy_utils import UUIDType, ChoiceType
from enum import Enum
from sqlalchemy.sql import func
import datetime

from models.db import Base
from models.basemodel import BaseModel

class BookType(Enum):
  FICTION = "fiction"
  NONFICTIONAL = "non-fictional"
  EDUCATIONAL = "educational"

class Book(Base, BaseModel):
  __tablename__ = "books"
  id = Column(UUIDTYPE(), primary_key =  True)
  book_name = Column(String, nullable = False)
  book_type = Column(ChoiceType(BookType), nullable = False)
  published_date = Column(DateTime, nullable = True)
  created_at = Column(DateTime, server_default = func.now())
  last_updated = Column(DateTime, onupdate=func.now())

  def ___init__(self, *, id: UUID = None, book_name: str, book_type: str, published_date: datetime, ):
    if not id:
      id = uuid4()
    self.id = id
    self.book_name = book_name
    self.book_type = book_type
    self.published_date = published_date

  def __repr__(self):
    return f"<Book(name: {self.book_name}, book_type: {self.book_type}, published_date: {self.published_date})>"
