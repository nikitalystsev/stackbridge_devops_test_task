# Stackbridge DevOps test task

Простое веб-приложение, запущенное в Docker-контейнерах и доступное через nginx reverse proxy.

## Структура проекта

```text
.
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## Используемые технологии

- Python `http.server` — backend-приложение
- Nginx — reverse proxy
- Docker
- Docker Compose

## Как работает схема

```text
Пользователь
    |
    | HTTP :80
    v
Nginx container
    |
    | proxy_pass http://backend:8080
    v
Backend container
```

Backend-приложение слушает порт `8080` внутри Docker-сети `my-net` и не публикуется наружу.
На хост проброшен только порт `80` контейнера `nginx`.

## Запуск проекта

Из корня проекта выполните:

```bash
docker compose up -d --build
```

Команда соберёт backend-образ и запустит два контейнера:

- `backend` — Python HTTP-сервер
- `nginx` — nginx reverse proxy

## Проверка результата

После запуска выполните:

```bash
curl http://localhost
```

Ожидаемый ответ:

```text
Hello from Effective Mobile!
```

## Остановка проекта

```bash
docker compose down
```
