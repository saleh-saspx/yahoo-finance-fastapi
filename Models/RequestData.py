from pydantic import BaseModel, Field, validator
from typing import List

class DataModel(BaseModel):
    items: List[str] = Field(..., title="Selected Symbols", description="List of symbols (strings)")

    @validator('items', each_item=True)
    def check_item_format(cls, v):
        if not (isinstance(v, str)):
            raise ValueError('Each item must be a string of 11 digits.')
        return v
