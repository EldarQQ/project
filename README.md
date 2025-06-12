
# 🧵 Проект Django Форум

Простое веб-приложение форум на Django, в котором пользователи могут регистрироваться, публиковать сообщения и оставлять комментарии.

## 🌐 Возможности

- Регистрация и авторизация пользователей  
- Создание, редактирование и удаление постов  
- Комментирование постов  
- Админ-панель Django  
- Профиль с аватаром  
- База данных SQLite (локальная)

## 🚀 Инструкция по запуску локально

### 1. Клонировать репозиторий

```bash
git clone https://github.com/EldarQQ/forum_py.git
cd forum_py
```

### 2. Создать виртуальное окружение и активировать

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# или
source venv/bin/activate      # Mac/Linux
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
# или вручную
pip install django pillow
```

### 4. Применить миграции и запустить сервер

```bash
python manage.py migrate
python manage.py runserver
```

Перейти в браузере по адресу: http://127.0.0.1:8000

## 🔐 Создание суперпользователя (по желанию)

```bash
python manage.py createsuperuser
```

Админ-панель доступна по адресу: http://127.0.0.1:8000/admin

## 📁 Структура проекта

```
blog_project/
├── blog/
├── users/
├── blog_project/
├── db.sqlite3
├── media/
└── manage.py
```

## ⚠️ Рекомендуемый .gitignore

```
*.pyc
__pycache__/
db.sqlite3
media/
venv/
```
