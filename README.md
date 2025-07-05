API для управления иерархической сетью по продаже электроники с тремя уровнями: заводы, розничные сети и индивидуальные предприниматели.

## Основные возможности

- Иерархическая структура сети с автоматическим расчетом уровня
- Управление контактами, продуктами и звеньями сети
- Контроль задолженностей между звеньями
- Фильтрация по стране, городу, типу звена
- Авторизация и права доступа


## Технологии

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.10+
- PostgreSQL 10+

## Установка

1. Клонируйте репозиторий:
````
git clone https://github.com/yuliyakuznetsova0102/Attest
````
2. Создайте и активируйте виртуальное окружение:

````
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
````
3. Установите зависимости:
````
pip install -r requirements.txt
````

4. Примените миграции:

````
python manage.py migrate
````
5. Создайте суперпользователя:
````
python manage.py createsuperuser
````
6. Запустите сервер:
````
python manage.py runserver
````
6. Использование
````
API документация: /swagger/ или /redoc/

Админ-панель: /admin/

/api/network/ - звенья сети

/api/contacts/ - контакты

/api/products/ - продукты
````