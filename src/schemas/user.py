from pydantic.v1 import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserErrors

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_dog_in_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)