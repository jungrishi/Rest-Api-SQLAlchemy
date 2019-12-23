# from __future__ import annotations
from typing import TYPE_CHECKING, Mapping, Type, List

from sqlalchemy import inspect, PrimaryKeyConstraint, Column
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Query, Mapper
from sqlalchemy.sql import ColumnCollection

if TYPE_CHECKING:
  from models.base_model import BaseModel


class APIQuery(Query):
  @property
  def _model_cls(self):
    from models.base_model import BaseModel

    if not self. _primary_entity:
      raise InvalidRequestError(
          "No primary mapper set up for this Query."
      )

    if not issubclass(self._primary_entity.type, BaseModel):
      cls = self._primary_entity.type.__name__
      raise InvalidRequestError(f"'{cls}' is not a subclass of 'BaseModel'")

    return self._primary_entity.type

  def fetch(self, params: Mapping) -> "APIQuery":
    print(self)
    print(params)
    print("...........")
    return (self
            .filter_params(params)
            .order_params(params)
            .limit_params(params))

  def limit_params(self, params: Mapping) -> "APIQuery":
    query = self

    if params.get("limit"):
      limit = int(params.get("limit"))
      offset = int(params.get("offset", 0))
      query = query.limit(limit)
      query = query.offset(offset)

    return query

  def filter_params(self, params: Mapping) -> "APIQuery":
    query = self

    for param_name in params:
      mapper: Mapper = inspect(self._model_cls)
      param_val = params.get(param_name)

      if param_name in mapper.columns:
        if isinstance(params.get(param_name), list) and params.get(param_name):
          query = query.filter(getattr(self._model_cls, param_name)).in_(param_val)
        else:
          query = query.filter(getattr(self._model_cls, param_name) == param_val)

      elif param_name in mapper.relationships:
        if isinstance(param_val, str):
          relationship = mapper.relationships[param_name]
          remote_primary_key: PrimaryKeyConstraint = relationship.target.primary_key
          remote_primary_key_col: List[Column] = remote_primary_key.columns.values()
          query: APIQuery = query.filter(remote_primary_key_col[0] == param_val)
          query = query.join(relationship.class_attribute)

        else:
          relations_params = params.get(param_name)
          for relation_param in params.get(param_name):
            query = query.filter(relations_params.get(relation_param))

    return query

  def order_params(self, params: Mapping) -> "APIQuery":
    order_on = (
      params.get("order_on") if params.get("order_on") in inspect(self._model_cls).columns else "id"
    )
    order_by = params.get("order_by") if params.get("order_by") else "ASC"

    query = self
    if order_on in inspect(self._model_cls).columns:
      query = (
        query.order_by(getattr(self._model_cls, order_on).desc()) if order_by == "DESC" else query.order_by(getattr(self._model_cls, order_on).asc())
      )
    return query
