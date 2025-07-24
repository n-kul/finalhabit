from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud, schemas

app = FastAPI()

origins = ["*"]  # For dev, use exact frontend URL in prod

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.get_or_create_user(db, user.username)

@app.post("/habit/{username}")
def mark(username: str, habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    user = crud.get_or_create_user(db, username)
    return crud.mark_habit(db, user, habit)

@app.get("/habit/{username}", response_model=list[schemas.HabitRead])
def get_habits(username: str, db: Session = Depends(get_db)):
    user = crud.get_or_create_user(db, username)
    return crud.get_user_habits(db, user)

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)
