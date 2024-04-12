from pydantic import BaseModel
from typing import List


class UserRegister(BaseModel):
    name: str
    mobile_no: str
    email: str
    password: str
    genres: List[str]
    languages: List[str]


class UserLogin(BaseModel):
    email: str
    password: str
