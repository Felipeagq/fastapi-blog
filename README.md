# FastAPI Blog
API de un CRUD de blogs y migraciones a base de datos

## Comandos para migración
- alembic current
- alembic revision --autogenerate -m "first m"
- alembic upgrade head
##postgresql
- docker-compose-postgres.yml
```
version: '3.8'
services:
  db:
    image: postgres:14.1-alpine
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - '5432:5432'
    volumes:
      - /var/lib/postgresql/data
```
- docker-compose -f docker-compose-postgres.yml up -d

## pendiente
- Autenticación.