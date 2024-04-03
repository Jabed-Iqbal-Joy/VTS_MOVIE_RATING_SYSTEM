from fastapi import APIRouter, status,Depends
from database import SessionLocal, engine
from schemas import MovieSchema,MovieFindSchema
from models import Movie,Rating
from fastapi.exceptions import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from  database import get_db

movie_router = APIRouter()

session = SessionLocal(bind=engine)


@movie_router.get("/")
async def get_all_movies():
    movies = session.query(Movie).all()
    return movies


@movie_router.post("/", response_model=MovieSchema, status_code=status.HTTP_201_CREATED)
async def add_new_movie(movie: MovieSchema):
    exists_movie = session.query(Movie).filter(Movie.name == movie.name).first()
    if exists_movie:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This Movie already exists in the list")
    new_movie = Movie(
        name=movie.name,
        genre= movie.genre,
        rating= movie.rating,
        release_date= movie.release_date
    )
    session.add(new_movie)
    session.commit()
    return new_movie

@movie_router.get("/{id}", response_model=dict)
async def get_movie_details_with_avg_rating(id: int):
    # Join Movie and Rating tables to calculate average rating
    movie_with_ratings = session.query(Movie, func.avg(Rating.rating)).join(Rating).filter(Movie.id == id).group_by(Movie.id).first()

    if movie_with_ratings is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    movie, avg_rating = movie_with_ratings
    # If there are no ratings for the movie, set average rating to 0
    average_rating = avg_rating or 0

    # Return movie details along with average rating
    return {
        "id": movie.id,
        "name": movie.name,
        "genre": movie.genre,
        "rating": movie.rating,
        "release_date": movie.release_date,
        "average_rating": average_rating
    }