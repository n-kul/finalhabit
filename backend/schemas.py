from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str

class HabitCreate(BaseModel):
    habit: str
    date: date

class HabitRead(BaseModel):
    habit: str
    date: date

    class Config:
        orm_mode = True
