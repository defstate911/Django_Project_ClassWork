# Django_Project_ClassWork
 
# README.md

## Описание проектов

Этот репозиторий содержит два Django-приложения.

1. **Фильмы** (movie_project) — сайт для добавления и просмотра фильмов с рецензиями.
2. **Комнатные растения** (MyApp) — сайт с информацией о комнатных растениях и возможностью добавления новостей о цветах.

Каждое приложение имеет свою структуру, модели, представления и шаблоны. Ниже приведено краткое описание функционала и структуры каждого из них.

---

## 1. Приложение "Фильмы"

### Функционал
- Просмотр списка фильмов с кратким описанием и рецензиями.
- Добавление нового фильма через форму (название, описание, рецензия, дата публикации).

### Структура
- **Модели**:
  - `News_post`: Хранит информацию о фильмах (название, описание, рецензия, дата публикации).
- **Представления**:
  - `index`: Отображает список всех фильмов.
  - `add_film`: Форма для добавления нового фильма.
- **Шаблоны**:
  - `base.html`: Базовый шаблон с навигацией.
  - `index.html`: Страница со списком фильмов.
  - `add_film.html`: Форма для добавления фильма.

### Как использовать
- На главной странице отображаются все добавленные фильмы.
- Для добавления нового фильма перейдите по ссылке "Добавить фильм" и заполните форму.

---

## 2. Приложение "Комнатные растения"

### Функционал
- Просмотр информации о популярных комнатных растениях (цикламен, толстянка, кактус).
- Добавление новостей о растениях через форму (заголовок, краткое описание, текст, дата публикации).

### Структура
- **Модели**:
  - `News_post`: Хранит информацию о новостях (заголовок, описание, текст, дата публикации, автор).
- **Представления**:
  - `home`: Главная страница с информацией о растениях.
  - `flower_ciklamen`, `flower_tolstyanka`, `flower_kaktus`: Страницы с описанием конкретных растений.
  - `add_news`: Форма для добавления новости.
- **Шаблоны**:
  - `layoute.html`: Базовый шаблон с навигацией.
  - `home.html`: Главная страница с описанием растений.
  - `flower_ciklamen.html`, `flower_tolstyanka.html`, `flower_kaktus.html`: Страницы с информацией о растениях.
  - `add_news.html`: Форма для добавления новости.

### Как использовать
- На главной странице представлены ссылки на популярные растения.
- Для добавления новости перейдите по ссылке "Добавить новость" и заполните форму.


## Требования

- Python 3.9+
- Django 4.x
- SQLite (встроенная база данных Django)
- Bootstrap 5 (для фронтенда)
---

## Установка и запуск

1. Клонируйте репозиторий.
2. Создайте виртуальное окружение и активируйте его.
3. Установите зависимости.
4. Примените миграции.
5. Запустите сервер.