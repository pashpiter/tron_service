# tron_service

#### Стек: Python, FastAPI, uvicorn, sqlalchemy, tronpy, postgresql, asyncpg, pytest

## О проекте
Микросервис, который выводит информацию по адресу в сети трон, его bandwidth, energy, и баланс trx. 


## Запуск проекта

<details>
<summary><b>🐳 Запуск через Docker (рекомендуется)</b></summary>
Для запуска проекта необходимо: 
* Установите Docker согласно инструкции с официального сайта: https://docs.docker.com/
* Клонировать репозиторий
```
git clone git@github.com:pashpiter/tron_service.git
```
* Перейти в папку tron_service
```
cd tron_service
```
* В папке создайте файл `.env` с переменных окружения
```
touch .env
```
* Заполните по примеру своими значениями как в этом [файле](example.env)
* Для запуска проекта введите команду:
```
docker compose up -d
```
или если локально установлен Make:
```
make up
```
> **Тесты.** Проект покрыт тестами, которые выполняются при сборке контейнеров.

</details><details> <summary><b>💻 Локальный запуск (без Docker)</b></summary>
</details>

## Документация
После запуска документация доступна по адресу:
```
127.0.0.1:8000/docs
```

## Энодпоинты API


#### Pavel Drovnin [@pashpiter](http://t.me/pashpiter)