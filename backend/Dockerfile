FROM python:3.13

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /app

ENV PYTHONPATH=/app/app

EXPOSE 8000

CMD ["python", "app/main.py"]