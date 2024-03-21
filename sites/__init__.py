from pydantic import BaseModel


class PublicSiteValidator(BaseModel):
    site_name: str
    site_code: str
    creator_id: int


class EditSiteValidator(BaseModel):
    site_id: int
    site_name_new: str
    site_code_new: str
