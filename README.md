Парсер WB с возможностью ввода данных в строку поиска c последующим сохранением в БД и отображением в Таблице данных и на графиках.

Для запуска - склонируйте проект командой git clone https://github.com/ant4p/wb_parser_task.git.
Создайте виртуальное окружение.
Установите в виртуальное окружение файл requirements.txt командой pip install -r requirements.txt
Файл .env_example замените на .env c вашим SECRET_KEY.
В корневой папке проекта осуществите миграции командой python manage.py migrate
Запустите проект на локальном сервере командой python manage.py runserver

В проекте использованы для:
парсера - Selenium
API - DRF
фильтрации - django-filter
графиков - plotly
таблицы данных, полей фильтрации - bootstrap5


