# Fast Zero

A tutorial-based FastAPI project for practicing an API beyond basic CRUD: user accounts, token authentication, personal to-dos, database migrations, and automated tests. The code is a learning project; it is not presented as a deployed product.

## What is implemented

- Create, list, update, and delete users.
- Authenticate with a password and issue/refresh JWT access tokens.
- Create, list, update, and delete to-dos scoped to the authenticated user.
- Persist data with SQLAlchemy and PostgreSQL; manage schema changes with Alembic.
- Exercise routes and database behavior with Pytest, factories, and test containers.

## Stack and structure

| Area | Tools |
| --- | --- |
| API and validation | Python 3.12.3, FastAPI, Pydantic |
| Persistence | SQLAlchemy, PostgreSQL, Alembic |
| Authentication | Passlib, PyJWT |
| Quality | Pytest, pytest-cov, Ruff, Taskipy |
| Local infrastructure | Docker Compose |

The `fast_zero/` package holds the API and application code. `migrations/` holds Alembic revisions; `tests/` holds automated tests.

## Development commands

The repository uses Poetry and Taskipy. After configuring PostgreSQL and the environment variables described below:

```bash
poetry install
poetry run task dev
poetry run task lint
poetry run task test
```

The `dev` task runs `fastapi dev fast_zero/app.py`. The test task runs Pytest with coverage. The repository also defines `format` and `post_test` tasks.

## Configuration

`fast_zero/settings.py` requires these environment variables:

| Variable | Purpose |
| --- | --- |
| `DATABASE_URL` | SQLAlchemy connection string for PostgreSQL |
| `SECRET_KEY` | Key used to sign access tokens |
| `ALGORITHM` | JWT signing algorithm |
| `ACCESS_TOKEN_EXPIRES_AT` | Access-token lifetime setting |

The settings class reads a local `.env` file. Use a development secret and keep it out of version control. The Compose file defines a PostgreSQL service, but its app service currently passes only `DATABASE_URL`; the other required settings must also be supplied before relying on the full Compose stack.

## What this project demonstrates

The repository shows how authentication, data ownership, migrations, and tests fit together in a small API. It also keeps quality checks in repeatable commands rather than relying only on manual route testing.
