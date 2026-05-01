# Desperate Gamblers

Веб-приложение на Flask для ведения истории матчей, игроков и результатов в приватном игровом клубе.

## Что внутри

- регистрация и вход пользователей
- сессии и базовая защита паролей (`werkzeug.security`)
- профиль игрока
- создание матчей: игра, участники, очки, победители
- главная страница с карточками сыгранных партий
- адаптивный интерфейс на Jinja2 + CSS

## Стек

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PostgreSQL
- HTML, Jinja2 templates, CSS, немного JS

## Быстрый старт

### 1. Клонирование и окружение

```bash
git clone <your-repo-url>
cd desperate_gamblers
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell
```

### 2. Установка зависимостей

```bash
pip install flask flask-sqlalchemy flask-migrate psycopg2-binary werkzeug
```

### 3. Настройка БД

Сейчас параметры подключения лежат в `app/config.py`. Для деплоя на Vercel их нужно вынести в переменные окружения.

Для production нужны переменные:

```text
SECRET_KEY=<long-random-secret>
DATABASE_URL=<postgresql-connection-url>
```

Также поддерживаются `POSTGRES_URL` и `POSTGRES_PRISMA_URL`, если их автоматически создаст Marketplace-интеграция.

Локально приложение использует `postgresql://postgres:1984@localhost:5432/postgres`, если `DATABASE_URL` не задан.

### 4. Миграции

```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

### 5. Запуск

```bash
python app.py
```

После запуска приложение доступно на `http://127.0.0.1:5000`.

## Основные маршруты

- `/` - главная страница для авторизованных пользователей
- `/login` - вход
- `/register` - регистрация
- `/logout` - выход
- `/profile/<name_user>` - профиль пользователя
- `/create_match` - создание матча

## Структура проекта

```text
desperate_gamblers/
├─ app.py
├─ README.md
└─ app/
   ├─ __init__.py
   ├─ config.py
   ├─ Amodels.py
   ├─ index.py
   ├─ login.py
   ├─ logout.py
   ├─ profile.py
   ├─ register.py
   ├─ create_match.py
   ├─ static/
   │  └─ style.css
   └─ templates/
      ├─ index.html
      ├─ login.html
      ├─ register.html
      ├─ profile.html
      ├─ create_match.html
      └─ notification.html
```
