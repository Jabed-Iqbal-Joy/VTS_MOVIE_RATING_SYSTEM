from fastapi import APIRouter, status
from database import SessionLocal, engine
from schemas import RatingSchema
from models import Rating
from fastapi.exceptions import HTTPException

rating_router = APIRouter()
session = SessionLocal(bind=engine)

@rating_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_new_rating(rate: RatingSchema):
    new_rating = Rating(
       user_id= rate.user_id,
        movie_id= rate.movie_id,
        rating= rate.rating
    )
    session.add(new_rating)
    session.commit()
    session.refresh(new_rating)
    return {"message": "Add rating successful!!"}
