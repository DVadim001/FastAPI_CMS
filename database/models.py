from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import func


# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    phone_number = Column(Integer)
    role = Column(String)
    contents = relationship("Content", back_populates="creator")


# Таблица контента
class Content(Base):
    __tablename__ = 'contents'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    create_at = Column(DateTime)
    creator = relationship("User", back_populates="contents")


# Таблица Шаблонов страниц
class Site(Base):
    __tablename__ = 'sites'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    template_code = Column(Text)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
