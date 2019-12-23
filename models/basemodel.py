from sqlalchemy.orm import Query
from typing import Mapping
from sqlalchemy import inspect, DateTime, Column, func

from models.db import session
from models.query import APIQuery

class BaseModel:
  def __repr__(self):
    return "<%s %r>" % (type(self).__name__, self.id)

  def _asdict(self):
    return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

  @classmethod
  def query(cls) -> Query:
    return Query(cls, session)

  @classmethod
  def fetch_(cls, params: Mapping, query: APIQuery = None):
    if not query:
      query = session.query(cls)
    print("query")
    print(query)

    return query.all()

  @classmethod
  def fetch_one(cls, params: Mapping, query: APIQuery = None):
    if not query:
      query =  session.query(cls)

    query = (query
            .filter_params(params)
            .order_params(params)
            .limit(1))

    return query.all()

  @classmethod
  def fetch_by_id(cls, id):
    query = session.query(cls)
    return query.filter(getattr(cls, "id") == id).first()

  @classmethod
  def create(cls, payload):
      session.add(payload)

  @classmethod
  def save(cls, object):
      session.add(object)

  @classmethod
  def update(cls, data):
      session.add(data)

  @classmethod
  def delete(cls, object):
      session.delete(object)

  @classmethod
  def delete_all(cls, params: Mapping, query: APIQuery = None):
    if not query:
      query = session.query(cls)

    query = query.filter_params(params)
    query.delete()
