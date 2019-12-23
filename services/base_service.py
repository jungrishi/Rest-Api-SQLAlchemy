from typing import Union, TypeVar, Generic, Mapping, List
from sqlalchemy.exc import StatementError
from http import HTTPStatus
from marshmallow import ValidationError
from uuid import UUID

from models.db import session
from models.basemodel import BaseModel

T = TypeVar("T", bound=BaseModel)
ID = Union[UUID, str]


class BaseService(Generic[T]):
  model = None
  model_schema = None

  @classmethod
  def fetch(cls, params: Mapping) -> List[T]:
    try:
      data = cls.model.fetch_(params)
    except StatementError as err:
      raise DatabaseException()
    return data
