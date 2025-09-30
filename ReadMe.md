Employee Management System
<div align="center">
https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white

Система управления сотрудниками с современным веб-интерфейсом и REST API

</div>
🚀 Быстрый старт
Предварительные требования
Docker

Docker Compose

Установка и запуск
Клонируйте репозиторий

bash
git clone <your-repo-url>
cd <project-directory>
Запустите приложение

bash
docker-compose up --build
Приложение будет доступно по адресам:

Frontend: http://localhost:3000

Backend API: http://localhost:8000

API Documentation: http://localhost:8000/docs

🗄️ Настройка базы данных
1. Инициализация базы данных
Перед началом работы необходимо создать базу данных:

bash
# Метод 1: Через Swagger UI
# Перейдите на http://localhost:8000/docs
# Найдите эндпоинт POST /setup_database и выполните его

# Метод 2: Через curl
curl -X POST "http://localhost:8000/setup_database"
Внимание: Этот эндпоинт удаляет существующую базу данных и создаёт новую!

2. Добавление тестовых данных
После инициализации добавьте тестовых пользователей:

bash
# Добавить 5 тестовых пользователей
curl -X POST "http://localhost:8000/users/set"

# Или добавьте пользователя вручную:
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
🛠 Технический стек
Backend
FastAPI - современный, быстрый веб-фреймворк

SQLAlchemy - ORM для работы с базой данных

SQLite - база данных (для разработки)

Pydantic - валидация данных

Uvicorn - ASGI-сервер

Frontend
React - пользовательский интерфейс

Axios - HTTP-клиент для API-запросов

CSS3 - стилизация

Инфраструктура
Docker - контейнеризация

Docker Compose - оркестрация контейнеров

📡 API Endpoints
Управление базой данных
POST /setup_database - Пересоздание базы данных

Пользователи
GET /users - Получить список всех пользователей

GET /users/{id} - Получить пользователя по ID

POST /users - Создать нового пользователя

POST /users/set - Добавить 5 тестовых пользователей

PUT /users/{id} - Обновить пользователя

DELETE /users/{id} - Удалить пользователя

Формат данных пользователя
json
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
🎯 Функциональность
Frontend
📋 Просмотр списка сотрудников

🔍 Поиск сотрудников по имени/фамилии

👤 Детальная информация о сотруднике (всплывающее окно)

📱 Адаптивный дизайн

⚡ Быстрая загрузка и отклик

Backend
🔒 CORS настройки для фронтенда

📊 Автогенерация документации API (Swagger)

🗃️ Миграции базы данных

🧪 Готовые тестовые данные

🏗️ Структура проекта
text
project/
├── backend/
│   ├── app/
│   │   ├── main.py          # Основное приложение FastAPI
│   │   ├── models.py        # Модели SQLAlchemy
│   │   └── database.py      # Настройки базы данных
│   ├── requirements.txt     # Python зависимости
│   └── Dockerfile          # Конфигурация Docker
├── frontend/
│   ├── src/
│   │   ├── components/      # React компоненты
│   │   ├── api.js          # Настройки Axios
│   │   └── App.js          # Главный компонент
│   ├── public/
│   └── Dockerfile          # Конфигурация Docker
└── docker-compose.yml      # Оркестрация контейнеров
🔧 Разработка
Локальная разработка без Docker
bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend  
cd frontend
npm install
npm start
Переменные окружения
DATABASE_URL=sqlite:///./app.db - URL базы данных

REACT_APP_API_URL=http://localhost:8000 - URL бэкенда для фронтенда

📝 Важные заметки
✅ База данных автоматически создаётся при первом запуске

✅ Данные сохраняются только во время работы контейнеров

✅ При перезапуске контейнеров база данных сбрасывается

✅ Для постоянного хранения данных нужно настроить volumes

✅ Все API endpoints документированы через Swagger UI

🐛 Решение проблем
Проблема: Фронтенд не видит бэкенд
bash
# Проверьте, что оба контейнера запущены
docker-compose ps

# Проверьте логи бэкенда
docker-compose logs backend

# Проверьте доступность API
curl http://localhost:8000/
Проблема: База данных не создаётся
bash
# Выполните инициализацию вручную
curl -X POST "http://localhost:8000/setup_database"
📄 Лицензия
Этот проект предназначен для демонстрационных целей.

<div align="center">
Готов к работе за 2 минуты! 🚀

</div>