
<p align="center">
  <img align="center" width="280" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/VK_Compact_Logo_%282021-present%29.svg/1024px-VK_Compact_Logo_%282021-present%29.svg.png"/>
</p>

# VKParser

Этот скрипт на Python получает список участников заданной группы ВКонтакте, фильтрует их по возрастному диапазону и экспортирует ссылки на их профили в CSV файл. Проект использует библиотеку `vk_api` для взаимодействия с API ВКонтакте.

## Особенности

-   Получение всех участников указанной группы ВКонтакте.
-   Фильтрация участников по возрасту на основе их даты рождения.
-   Сохранение отфильтрованных ссылок на профили в CSV файл.
-   Логирование для отслеживания прогресса и ошибок.

## Требования

Перед использованием скрипта убедитесь, что у вас установлены следующие зависимости:

-   Python 3.x
-   Библиотека `vk_api` для взаимодействия с VK API.
-   Библиотека `tqdm` для отображения прогресса при фильтрации.
-   `csv` для записи результатов в файл.

### Установка зависимостей

Используйте `poetry` для установки необходимых библиотек:

```bash
poetry install
```

## Настройка и запуск

1. **Клонирование репозитория:**

    ```bash
    git clone https://github.com/ваш-username/VKParser.git
    cd VKParser 
    ```

2. **Настройка переменных:**

    - В файле `parser.py` замените строки `token` и `group_id` на ваш токен и ID группы.
    - Пример:
        ```python
        token = "ваш_токен_вк"
        group_id = "id_группы"
        ```

3. **Запуск скрипта:**

    Выполните команду для запуска:

    ```bash
    python parser.py
    ```

## Аргументы

-   `token`: Токен для доступа к VK API.
-   `group_id`: ID группы ВКонтакте, чьих участников нужно получить.
-   `min_age`: Минимальный возраст участников (по умолчанию 14).
-   `max_age`: Максимальный возраст участников (по умолчанию 21).
-   `output_file`: Имя файла, в который будут сохранены результаты (по умолчанию `<group_id>.csv`).

## Пример использования

1. Замените переменные в `parser.py`:

    ```python
    token = "ваш_токен_вк"
    group_id = "123456789"  # пример ID группы
    ```

2. Запустите скрипт:
    ```bash
    python parser.py
    ```

После выполнения скрипта, отфильтрованные ссылки на профили будут сохранены в указанный CSV файл.