from sqlalchemy.orm import Session
from models import User, Habit
from schemas import UserCreate, HabitCreate
from datetime import date

def get_or_create_user(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        user = User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def mark_habit(db: Session, user: User, habit_data: HabitCreate):
    habit = db.query(Habit).filter_by(user_id=user.id, habit=habit_data.habit, date=habit_data.date).first()
    if habit is None:
        habit = Habit(user_id=user.id, habit=habit_data.habit, date=habit_data.date)
        db.add(habit)
        db.commit()
    return habit

def get_user_habits(db: Session, user: User):
    return db.query(Habit).filter_by(user_id=user.id).all()

def get_all_users(db: Session):
    return db.query(User).all()
