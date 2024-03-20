from pydantic import BaseModel


class RegisterValidator(BaseModel):
    username: str
    phone_number: int
    password: str


class EditUserValidator(BaseModel):
    user_id: int
    edit_info: str
    new_info: str
