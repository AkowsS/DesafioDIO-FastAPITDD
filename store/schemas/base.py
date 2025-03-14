
from datetime import datetime
from decimal import Decimal
from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_validator


class BaseSchemaMixin(BaseModel):
  class Config:
    from_attributer=True

class OutMixin(BaseModel):
  id: UUID4 = Field()
  created_at: datetime = Field()
  updated_at: datetime = Field()

  @model_validator(mode = "before")
  def set_schema(cls, data):
    for key, value in data.items():
      if isinstance(value, Decimal):
        data[key] = Decimal128(str(value))
    return data