## Libs Used in this project
- Alembic
- Docker
- Factory-boy
- FastAPI
- Freezegun
- Poetry
- PostgreSQL
- Pyenv
- Pytest
- Ruff
- SQLAlchemy
- Taskipy
- Ignr
- Gh

### Project tools and most used command while developing:
### Taskipy:

`poetry run task lint` = 'ruff check . && ruff check . --diff'

ruff check --diff: Mostra o que precisa ser alterado no código para que as boas práticas sejam seguidas

ruff check: Mostra os códigos de infrações de boas práticas

**&&**: O duplo & faz com que a segunda parte do comando só seja executada se a primeira não der erro. Sendo assim, enquanto o --diff apresentar erros, ele não executará o check

- `poetry run task format` = 'ruff check . --fix && ruff format .'

ruff check --fix: Faz algumas correções de boas práticas automaticamente

ruff format: Executa a formatação do código em relação as convenções de estilo de código

- `poetry run task dev` = 'fastapi dev fast_zero/app.py'

run: executa o servidor de desenvolvimento do FastAPI


- `poetry run task pre_test` = 'task lint'

pre_test: executa a camada de lint antes de executar os testes


- `poetry run task test` = 'pytest -s -x --cov=fast_zero -vv'

test: executa os testes com pytest de forma verbosa (-vv) e adiciona nosso código como base de cobertura

- `poetry run task post_test` = 'coverage html'
Mostra umam página HTML ilustrando resumo da cobertura frente os testes realizados

### Alembic:
 Initiate the already existent migrations
 `alembic init migrations`
 Generate the migration with a message
 `alembic revision --autogenerate -m "message"`
 Apply the migration generated to the database
 `alembic upgrade head`

### Sqlite:
Open the sqlite database
 `sqlite3 database.db`
View the database schemas created
 `.schema`

### Ignr:
add .gitignore into python propject with the files and folders needed
 `ignr -p python > .gitignore`

### gh:
add project into your github repo by an interactive CLI
  `ignr -p python > .gitignore`

###fac

- poetry shell ativa o ambiente virtual para que seja enxergue as dependencias  do projeto
- poetry install instala as dependencias do projeto
