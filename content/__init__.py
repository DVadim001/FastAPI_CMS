from pydantic import BaseModel


class PublicContentValidator(BaseModel):
    user_id: int
    body: str
    title: str


class EditContentValidator(BaseModel):
    id: int
    new_text: str
    new_title: str
