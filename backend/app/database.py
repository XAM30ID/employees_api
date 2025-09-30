from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.sql import func


DATABASE_URL='sqlite+aiosqlite:///employees'
engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]


class Base(DeclarativeBase):
    pass

class EmployeesModel(Base):
    '''
        Модель пользователей
    '''
    __tablename__ = 'Employees'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    access_date = Column(Date, nullable=False)
    user_pose = Column(String, nullable=False)
    subdivision = Column(String, nullable=False)
    additional = Column(String, nullable=True, default='Отстутствует')



async def setup_database():
    '''
        Функция созданя базы данных
    '''
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()