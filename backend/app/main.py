from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import or_, select
import uvicorn
from random import choice

from app.schemes import UserCreate
from app.database import setup_database, SessionDep, EmployeesModel


NAMES = ['Иван', 'Александр', 'Андрей', 'Эмиль', 'Степан']
SURNAMES = ['Алексеев', 'Панкратов', 'Руднин', 'Хакимов', 'Калашников']


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/setup_database', tags=['Настройка'], summary='Создание базы данных', description='Эндпоинт для создания или перезаписи базы данных в целях тестирования')
async def setup_database_url():
    '''
        Создание базы данных
    '''
    await setup_database()
    return {'message': 'Tables created successful!'}


@app.post('/users/set', tags=['Настройка'], summary='Тестовое заполнение базы данных', description='Эндпоинт для автоматического создания пользователей')
async def fill_database_url(session: SessionDep):
    '''
        Заполнение базы данных
    '''
    for _ in range(5):
        session.add(EmployeesModel(
            name=choice(NAMES),
            surname=choice(SURNAMES),
            phone='+7(999)999-99-99',
            email='ivan.ivanov@mail.ru',
            access_date=datetime.now(),
            user_pose='Программист',
            subdivision='Трайб автоматизированных систем контактных центров',
            additional='Разработчики используют текст в качестве заполнителя макта страницы. Разработчики используют текст в качестве заполнителя макта страницы.'
        ))
    await session.commit()
    employees = select(EmployeesModel)
    result = await session.execute(employees)
    return {'message': 'Users was added successfull', 'users': result.scalars().all()}


@app.post('/users', tags=['Настройка'], summary='Добавление пользователя вручную', description='Эндпоинт для создания пользователя')
async def add_user_url(user: UserCreate, session: SessionDep):
    '''
        Добавление пользователя
    '''
    new_user = EmployeesModel(
        name=user.name,
        surname=user.surname,
        phone=user.phone,
        email=user.email,
        access_date=user.access_date,
        user_pose=user.user_pose,
        subdivision=user.subdivision,
        additional=user.additional
    )
    session.add(new_user)
    await session.commit()
    return {'message': 'User was created successfull', 'user_id': new_user.id}

@app.get('/users', tags=['Пользователи'], summary='Получение всех пользователей', description='Эндпоинт для получения пользователей')
async def get_users(session: SessionDep, name_filter=''):
    employees = select(EmployeesModel).filter(or_(EmployeesModel.name.startswith(name_filter), EmployeesModel.surname.startswith(name_filter))).order_by(EmployeesModel.name.asc())
    result = await session.execute(employees)
    return {'users': result.scalars().all()}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,            
        reload=True
        )