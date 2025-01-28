from pydantic.v1 import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=2)
    title: str

    # @validator('id')
    # def check_then_id_is_less_then_two(cls, value):
    #     if value > 2:
    #         raise ValueError('Id is not less then two')
    #     else:
    #         return value
