### Парсер WB с возможностью ввода данных в строку поиска c последующим сохранением в БД и отображением в Таблице данных и на графиках. ###

Для запуска - склонируйте проект командой git clone https://github.com/ant4p/simple_wb_parser_with_save_and_view_result_in_tables_graphs.git <br/>
Создайте виртуальное окружение.<br/>
Установите в виртуальное окружение файл requirements.txt командой pip install -r requirements.txt<br/>
Файл .env_example замените на .env c вашим SECRET_KEY.<br/>
В корневой папке проекта осуществите миграции командой python manage.py migrate<br/>
Запустите проект на локальном сервере командой python manage.py runserver<br/>

В проекте использованы для:<br/>
парсера - Selenium<br/>
API - DRF<br/>
фильтрации - django-filter<br/>
графиков - plotly<br/>
таблицы данных, полей фильтрации - bootstrap5<br/>


