from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    '''
        Схема добавления сторудника
    '''
    name: str = Field()
    surname: str = Field()
    phone: str = Field()
    email: str = Field()
    access_date: datetime = Field(default=datetime.now())
    user_pose: str = Field()
    subdivision: str = Field()
    additional: str = Field(default='Отсутствует')
    
