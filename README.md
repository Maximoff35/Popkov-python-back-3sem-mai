# Python Backend

## Course Service

Сервис курса на FastAPI.

### Установка зависимостей

``` bash
cd course-service
uv sync
```

### Настройка окружения

Создайте файл `.env` в директории `course-service`:

``` env
APP__HOST=127.0.0.1
APP__PORT=8888
APP__LOG_LEVEL=info
```

### Запуск

``` bash
uv run uvicorn src.main:app --host 127.0.0.1 --port 8888 --env-file ".env" --workers 1 --log-level info --no-access-log --log-config log-config.yaml
```

После запуска доступны:

-   `http://127.0.0.1:8888/service`
-   `http://127.0.0.1:8888/docs`
-   `http://127.0.0.1:8888/openapi.json`

### Тесты

``` bash
uv run pytest
```

### Проверка качества кода

``` bash
uv run pylint ./src --rcfile pyproject.toml
uv run mypy ./src --config-file pyproject.toml
uv run ruff check ./src --config pyproject.toml
uv run black --check ./src
uv run radon hal src
uv run radon cc src -s
uv run radon mi src -s
uv run isort ./src --check
```
