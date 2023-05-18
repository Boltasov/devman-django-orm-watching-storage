# Пульт управления охраной

Пульт управления охраной предоставляет интерфейс для отслеживания посещения хранилища по пропускам.

## Требования
Должны быть установлены:
- git, чтобы вы могли скачать код; 
- pip, чтобы установить необходимые библиотеки;
- python3, чтобы запустить код.

## Запуск

Скачайте код с помощью команды в командной строке
```
https://github.com/Boltasov/devman-django-orm-watching-storage
```
Установите необходимые библиотеки командой
```
python pip install -r requirements.txt
```
Создайте в папке `project` файл с названием `.env` и вставьте в него следующие данные:
```
DB_ENGINE='your_db_engine'
DB_HOST='your_db_host'
DB_PORT='your_db_port'
DB_NAME='your_db_name'
DB_USER='your_db_user'
DB_PASSWORD='your_db_password'

SECRET_KEY = 'your_secret_key'
```
Вместо плейсхолдеров вставьте свои значения для подключения к базе данных.

При необходимости вы можете добавить в `.env` следующие значения:
```
DEBUG=False

ALLOWED_HOSTS=[your_list_of_hosts]
```
По умолчанию:
- `DEBUG=True` для безопасного тестового запуска. Если предполагается доступ к сайту пользователей, необходимо отключить режим дебага.
- `ALLOWED_HOSTS=['127.0.0.1']`, чего достаточно для тестового запуска на вашем ПК. Если вы захотите развернуть сайт на другом хосте, его будет необходимо добавить в этот список.

Запустите сайт командой 
```
python manage.py runserver 0.0.0.0:8000
``` 
Cайт можно будет открыть по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
