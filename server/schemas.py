from pydantic import BaseModel
from typing import Optional
from  datetime import  date


class SignUpModel(BaseModel):
    name: str
    phone: str
    password: str
    email: str

    class Config:
        orm_mode = True


class Settings(BaseModel):
    authjwt_secret_key: str = 'SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'


class LoginModel(BaseModel):
    email: str
    password: str

class MovieFindSchema(BaseModel):
    id:int
    name: str
    genre: str
    rating: str
    release_date: str
    avg_rating: float

class MovieSchema(BaseModel):
    name: str
    genre: str
    rating: str
    release_date: str

    class Config:
        orm_mode = True

class RatingSchema(BaseModel):
    user_id: int
    movie_id: int
    rating: float

    class Config:
        orm_mode = True