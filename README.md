**Простое веб-приложение электронной коммерции с использованием Flask**

---

Это простое веб-приложение электронной коммерции, разработанное с использованием Flask - легковесного веб-фреймворка на Python. Приложение позволяет пользователям просматривать продукты, добавлять их в корзину, а также выполнять различные административные задачи, такие как управление продуктами и просмотр журналов ошибок.

**Установка и запуск:**
1. Сначала склонируйте репозиторий на свой компьютер:
    ```
    git clone <url_репозитория>
    ```
2. Перейдите в каталог с проектом:
    ```
    cd <название_каталога>
    ```
3. Установите все необходимые зависимости, включая Flask и SQLAlchemy:
    ```
    pip install Flask flask-SQLAlchemy
    ```
4. Запустите приложение, указав `python main.py` в командной строке.

**Требования:**
- Python 3.x
- Flask
- SQLAlchemy

**Структура проекта:**
- `main.py`: Основной файл приложения.
- `templates/`: HTML-шаблоны для отображения страниц.
- `static/`: Статические ресурсы, такие как изображения и таблицы стилей.
- `main.db`: База данных SQLite для хранения продуктов и журналов ошибок.

**Заметки по разработке:**
- Приложение использует токен для сессии и базу данных SQLite, указанную в `SQLALCHEMY_DATABASE_URI`.
- Администраторский доступ: логин - "admin", пароль - "ober".
- Для добавления продуктов используется изображение, которое сохраняется в `static/img/products`.

**Автор:**
tg - Oberrrr   ds - ober11

**Лицензия:**
Распространяется свободно

---