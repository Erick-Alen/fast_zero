FROM python:3.12.3-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry

RUN chmod +x /app/entrypoint.sh
## Set the max number of workers to 10 when installing dependencies
RUN poetry config installer.max-workers 10

## Install dependencies without interaction and output colors
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 fast_zero.app:app
