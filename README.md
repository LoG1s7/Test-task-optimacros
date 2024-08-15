# Тестовое задание для optimacros
Тестовое задание - интеграция с API сервиса DaData для получения геолокационных данных
## Описание ТЗ
    1. Получить координату (долгота и широта) на странице с HTML-формой.
    2. Используя API DaData https://dadata.ru/api/geolocate/, получить полный адрес по координатам из справочника "data".
    3. Разбить адрес из поля "unrestricted_value" на составляющие части.
    4. Презентовать результат на другой HTML-странице в виде карточки объекта.

## Используемые технологии

- python 3.11
- fastapi
- jinja2
- pre-commit
- flake8
- black
- dadata
- pydantic-settings

### Рекомендации. Poetry<a id="poetry"></a>
Poetry - инструмент для управления зависимостями и виртуальными окружениями, также может использоваться для сборки
пакетов.

- <details>
    <summary>
      Как скачать и установить?
    </summary>

  - Установите poetry следуя [инструкции с официального сайта](https://python-poetry.org/docs/#installation).
  - <details>
      <summary>
      Команды для установки
      </summary>

      > Для UNIX-систем и Bash on Windows вводим в консоль следующую команду:
      > ```shell
      > curl -sSL https://install.python-poetry.org | python -
      > ```
      >
      > Для WINDOWS PowerShell:
      > ```shell
      > (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
      > ```
    </details>
    <br>

  - После установки - перезапустите оболочку и введите команду:
    ```shell
    poetry --version
    ```

    Если установка прошла успешно, вы получите ответ в формате `Poetry (version 1.3.2)`

  - Для дальнейшей работы создайте виртуальное окружение:
    ```shell
    poetry config virtualenvs.in-project true
    poetry install
    ```
    Результатом выполнения команды станет создание в корне проекта папки .venv.
    Зависимости для создания окружения берутся из файлов poetry.lock (приоритетнее) и pyproject.toml

  - Для добавления новой зависимости в окружение необходимо выполнить команду
    ```shell
    poetry add <package_name>
    ```

  - Также poetry позволяет разделять зависимости необходимые для разработки, от основных.
    Для добавления зависимости необходимой для разработки и тестирования необходимо добавить флаг `--group dev`
    ```shell
    poetry add <package_name> --group dev
    ```
    Если добавили новые зависимости, то выгружаем из в requirements.txt для docker контейнера
    ```shell
    poetry export --without-hashes --format=requirements.txt > requirements.txt
    ```
</details>

- <details>
    <summary>
      Порядок работы после настройки
    </summary>

    <br>

  - Чтобы активировать виртуальное окружение, введите команду:
    ```shell
    poetry shell
    ```

  - Доступен стандартный метод работы с активацией окружения в терминале.

</details>

### Pre-commit <a id="pre-commit"></a>
Pre-commit - инструмент автоматического запуска различных проверок перед выполнением коммита.

Установите pre-commit командой:
```shell
pre-commit install
```
Теперь при каждом коммите у вас будет автоматическая проверка линтером,
а так же, автоматическое форматирование кода.

## Запуск проекта
1. Установите зависимости:
С помощью poetry
```shell
poetry install 
```
Либо с помощью pip
```shell
pip install requirements.txt 
```
2. Создайте файл ".env" из файла ".env.example":

3. Запустите сервер:
```shell
uvicorn main:app --reload
```
4. Откройте браузер и перейдите по адресу: `http://127.0.0.1:8000/`

## Тестирование
Для запуска тестов выполните:
```shell
python -m unittest discover tests
```