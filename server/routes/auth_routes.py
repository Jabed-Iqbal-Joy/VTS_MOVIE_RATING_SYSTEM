from fastapi import APIRouter, status
from database import SessionLocal, engine
from schemas import SignUpModel, LoginModel
from models import User
from fastapi.exceptions import HTTPException


auth_router = APIRouter()

session = SessionLocal(bind=engine)


# @auth_router.get("/")
# async def hello():
#     return {"message": "hello"}


#
@auth_router.post("/signup", response_model=SignUpModel, status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):
    exists_user = session.query(User).filter(User.email == user.email).first()
    if exists_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    new_user = User(
        name=user.name,
        phone=user.phone,
        password=user.password,
        email=user.email
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user: LoginModel):
    db_user = session.query(User).filter(User.email == user.email).first()
    if db_user and db_user.password == user.password:
        return {"Message": "Login Successfull!!"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Useremail or Password")
