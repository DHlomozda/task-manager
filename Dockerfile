FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH="/opt/venv/bin:$PATH" \
    DJANGO_SETTINGS_MODULE=task_services.settings.prod

WORKDIR /app

# Install dependencies first (layer cached unless pyproject/uv.lock change)
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project

COPY . .

# prod settings read these at import time; dummy values are fine for collectstatic
RUN SECRET_KEY=build-only POSTGRES_DB_PORT=5432 \
    python manage.py collectstatic --no-input

RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --no-input && gunicorn task_services.wsgi:application --bind 0.0.0.0:8000 --workers 3"]
