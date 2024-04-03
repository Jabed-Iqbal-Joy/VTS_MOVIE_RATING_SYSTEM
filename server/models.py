from sqlalchemy import Column, Integer, String, ForeignKey, Float,DATE
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String)
    password = Column(String)
    email = Column(String, unique=True, index=True)

    # Relationship: One-to-Many (User to Ratings)
    ratings = relationship("Rating", back_populates="user")

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    genre = Column(String)
    rating = Column(String)
    release_date = Column(String)

    # Relationship: One-to-Many (Movie to Ratings)
    ratings = relationship("Rating", back_populates="movie")

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    rating = Column(Float)

    # Relationships: Many-to-One (Ratings to User and Movie)
    user = relationship("User", back_populates="ratings")
    movie = relationship("Movie", back_populates="ratings")