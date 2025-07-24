from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    habits = relationship("Habit", back_populates="user")

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    habit = Column(String)
    date = Column(Date)

    user = relationship("User", back_populates="habits")
    __table_args__ = (UniqueConstraint("user_id", "habit", "date", name="unique_habit_per_day"),)
