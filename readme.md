## Описание
Учебный проект магазина с использованием фреймворка **Django**.
В проекте Django зарегистрировано приложение **catalog**.
Проект на текущий момент имеет две страницы _home.html_ и _contact.html_.
Страницы созданы с использованием BootStrap.
На форме страницы  _contact.html_ предусмотрена отправка данных,
они выводятся в консоль сервера.

## Описание директорий

Директория **static** содержит стили CSS.
В директории catalog находятся файлы приложения **catalog**.
Директория **config** содержит файлы настройки Django.
Директория **media** содержит медиафайлы.В ней лежат файлы скриншотов и папка для хранения фотографий продуктов




## Настройка
- Клонируйте репозиторий на свой компьютер:

```
https://github.com/MichaelGorbunov/web_store/
```


1. Создайте и активируйте виртуальное окружение poetry (рекомендуется)
2. Установите зависимости из pyproject.toml
3. Заполните файл **.env.sample** данными для подключения к серверу PostgreSQL и переименуйте в **.env**
4. Примените миграции к базе данных: ```python manage.py migrate```
5. Заполните базу данных используя кастомную команду **add_catalog**
6. Создайте суперпользователя ```python manage.py createsuperuser```.
7. Через админку http://127.0.0.1:8000/admin/ можно проводить различные манипуляции с данными. 


## Использование
Для запуска приложения используйте команду:

```
 python manage.py runserver

```
