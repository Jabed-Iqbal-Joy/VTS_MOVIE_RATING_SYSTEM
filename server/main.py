from typing import Union, List
from fastapi import FastAPI
from database import engine,get_db
from routes.auth_routes import auth_router
from routes.movie_routes import movie_router
from routes.rating_routes import rating_router
import  models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
#
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(movie_router, prefix="/movies", tags=["movies"])
app.include_router(rating_router, prefix="/ratings", tags=["ratings"])

#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
