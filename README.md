# tron_service

#### Стек: Python, FastAPI, uvicorn, sqlalchemy, tronpy, postgresql, asyncpg, pytest

## О проекте
Микросервис, который выводит информацию по адресу в сети трон, его bandwidth, energy, и баланс trx. 


## Запуск проекта

<details>
<summary><b>🐳 Запуск через Docker (рекомендуется)</b></summary>


1. Установите Docker согласно инструкции с официального сайта: https://docs.docker.com/
2. Клонировать репозиторий
```
git clone git@github.com:pashpiter/tron_service.git
```
3. Перейти в папку tron_service
```
cd tron_service
```
4. В папке создайте файл `.env` с переменных окружения
```
touch .env
```
5. Заполните по примеру своими значениями как в этом [файле](example.env)
6. Для запуска проекта введите команду:
```
docker compose up -d
```
или если локально установлен Make:
```
make up
```
> **Тесты.** Проект покрыт тестами, которые выполняются при сборке контейнеров.

</details><details> <summary><b>💻 Локальный запуск (без Docker)</b></summary>

1. Клонировать репозиторий
```
git clone git@github.com:pashpiter/tron_service.git
```
2. Перейти в папку tron_service
```
cd tron_service
```
3. В папке создайте файл `.env` с переменных окружения
```
touch .env
```
4. Заполните по примеру своими значениями как в этом [файле](example.env)
5. Создать и активировать вирутальное окружение
```
python3 -m venv venv
acivate .venv/bin/activate
```
6. Установить зависимости
```
pip install -r requirements.txt
```
7. Запустить приложение
```
uvicorn app.main:app --reload
```
> **Тесты.** Для запуска тестов используйте команду `pytest -v`.
</details>

## Документация
После запуска документация доступна по адресу:
```
{FASAPI_HOST}:{FASAPI_PORT}/docs
{FASAPI_HOST}:{FASAPI_PORT}/redoc
```

## Энодпоинты API
### 1. Получение информации о кошельке TRON
`POST /`

**Описание**:  
Возвращает баланс TRX, bandwidth, energy и другую информацию по указанному адресу в сети TRON.

**Параметры запроса** (JSON):
```
{
  "address": "TQjaZ9FD473QBTdUzMLmSyoGB6Yz1CGpux"
}
```
Пример успешного ответа:
```
{
  "address": "TQjaZ9FD473QBTdUzMLmSyoGB6Yz1CGpux",
  "trx_balance": 89898.03202,
  "bandwidth": 600,
  "energy": 0
}
```
### 2. Получение истории запросов
`GET /`

**Описание**: 
Возвращает историю запросов с пагинацией.
Параметры запроса (query params):
```
offset - Количество пропускаемых элементов (default: 0)
limit - Количество элементов на странице (default: 10)
```
Пример успешного ответа:
```
{
  "items": [
    {
      "address": "TQjaZ9FD473QBTdUzMLmSyoGB6Yz1CGpux",
      "trx_balance": 1250.5,
      "bandwidth": 4900,
      "energy": 950,
      "id": 1,
      "timestamp": "2025-04-22T11:26:50.621134Z"
    }
  ]
}
```
#### Pavel Drovnin [@pashpiter](http://t.me/pashpiter)