# 🏢 Employee Management System

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

**Современная система управления сотрудниками с веб-интерфейсом**

</div>

## 📋 О сервисе

Демонстрация простейшей full-stack разработки. Позволяет просматривать, искать и управлять данными сотрудников компании.

## 🚀 Быстрый старт

### Предварительные требования
- Установленный Docker
- Установленный Docker Compose
- Запущенный Docker Desktop

### Установка и запуск

1. **Скачайте проект**
```bash
git clone https://github.com/XAM30ID/employees_api.git
cd <папка-проекта>
```

2. **Запустите все сервисы одной командой**
```bash
docker-compose up --build
```

3. **Откройте в браузере:**
   - 📱 **Фронтенд**: http://localhost:3000
   - ⚙️ **Бэкенд API**: http://localhost:8000
   - 📖 **Документация API**: http://localhost:8000/docs

## 🗄️ Настройка базы данных

### 1. Инициализация базы данных

Перед началом работы необходимо создать базу данных:

```bash
# Метод 1: Через документацию Swagger
# Перейдите на http://localhost:8000/docs
# Найдите эндпоинт POST /setup_database и выполните его

# Метод 2: Через командную строку
curl -X POST "http://localhost:8000/setup_database"
```

⚠️ **Важно**: Этот эндпоинт полностью пересоздает базу данных, удаляя все существующие данные!

### 2. Добавление тестовых данных

После инициализации добавьте тестовых пользователей:

```bash
# Добавить 5 тестовых пользователей автоматически
# Перейдите на http://localhost:8000/docs
# Найдите эндпоинт POST /users/set и выполните его
# Или
curl -X POST "http://localhost:8000/users/set"

# Или добавьте пользователя вручную:
# Найдите эндпоинт POST /users и выполните его
# Или
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Иван",
    "surname": "Петров",
    "phone": "+7-999-123-45-67",
    "email": "ivan.petrov@company.com",
    "access_date": "2024-01-15T10:00:00",
    "user_pose": "Разработчик",
    "subdivision": "IT отдел",
    "additional": "Отсутствует"
  }'
```

## 📡 API Endpoints

### Управление базой данных
- `POST /setup_database` - Полная пересоздание базы данных

### Работа с пользователями
- `GET /users` - Получить список всех пользователей
- `POST /users` - Создать нового пользователя
- `POST /users/set` - Добавить 5 тестовых пользователей

### Формат данных пользователя
```json
{
  "name": "string",
  "surname": "string",
  "phone": "string",
  "email": "string",
  "access_date": "2024-01-15T10:00:00",
  "user_pose": "string",
  "subdivision": "string",
  "additional": "string"
}
```

## 🛠 Технологии

### Backend
- **FastAPI** - современный Python фреймворк
- **SQLAlchemy** - ORM для работы с базой данных
- **SQLite** - легковесная база данных
- **Pydantic** - валидация данных
- **Uvicorn** - ASGI-сервер

### Frontend
- **React** - пользовательский интерфейс
- **Axios** - HTTP-клиент для API запросов
- **CSS3** - стили и анимации

### Инфраструктура
- **Docker** - контейнеризация приложения
- **Docker Compose** - оркестрация контейнеров

## 🎯 Функциональность

### Frontend
- 📋 Просмотр списка сотрудников
- 🔍 Поиск по имени и фамилии
- 👤 Детальная информация в попап-окне
- ⚡ Быстрый отклик интерфейса

### Backend
- 🔒 CORS настройки для фронтенда
- 📊 Автоматическая документация API
- 🗃️ Миграции базы данных
- 🧪 Генерация тестовых данных

## ⚠️ Важные заметки

- ✅ База данных создается автоматически при первом запуске
- ✅ Данные сохраняются только во время работы контейнеров
- ✅ При перезапуске контейнеров база данных сбрасывается
- ✅ Для постоянного хранения нужно настроить Docker volumes
- ✅ Все API endpoints документированы через Swagger UI
---

<div align="center">

**Готов к работе за 2 минуты! 🚀**

*Для начала работы выполните: `docker-compose up --build`*

</div>
