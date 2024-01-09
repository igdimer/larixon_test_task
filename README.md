# Тестовое задания для Larixon

### Стэк

- Python 3.11
- Django 4.2
- Django Rest Framework 3.14
- PostgreSQL
- Docker


Также в проекте используются pytest, isort, flake8, mypy.

### Запуск проекта

Склонируйте репозиторий и в папке с проектом выполните команду ```docker-compose up```. После этого проект доступен на ```http://0.0.0.0:8000```

### Список эндпоинтов

```GET /api/advert-list``` получение списка объявлений

```GET /api/advert/<advert-id>``` получение информации об объявлении по переданному id
