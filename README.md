# API Work Out


### Instalações necessárias:
1. Crie um ambiente virtual com `pyenv` para o Python 3.11.4:

`pyenv virtualenv 3.11.4 workoutapi`

2. Ative o ambiente virtual recém-criado:

`pyenv activate workoutapi`

3. Instale as dependencias necenssárias usando `pip`:

`pip install fastapi uvicorn sqlalchemy pydantic`

- fastapi: É um framework web moderno e rápido para construir APIs com Python 3.7+.
- uvicorn: É um servidor ASGI de alta performance, utilizado com o FastAPI para servir a aplicação web.
- sqlalchemy: É uma biblioteca popular de mapeamento objeto-relacional (ORM) em Python, usada para trabalhar com bancos de dados relacionais de forma mais abstrata.
- pydantic: É uma biblioteca de validação de dados em Python, usada no FastAPI para validar dados de entrada e saída das APIs.

4. Intalar alembic

`pip install alembic`


### Rodando migrations
Para subir o banco de dados:

`make run-docker`

Criando uma migration nova:

`make create-migrations d="nome_da_migration"`

Para criar o banco de dados:

`make run-migrations`


### Rodando o projeto
`uvicorn workout_api.main:app --reload`

Ou se preferir usar o arquivo makefile: `make run`

acesse: [http://localhost:8000/docs]


### Requerimentos
Instalando:

`pip install -r requirements.txt`

Para trazer requerimentos:

`pip freeze > requirements.txt`


### Documentações
- FastApi: [https://fastapi.tiangolo.com]

- Pydantic: [https://docs.pydantic.dev/latest/]

- SQLAlchemy: [https://docs.sqlalchemy.org/en/20/]

- Alembic: [https://alembic.sqlalchemy.org/en/latest/]

- Fastapi-pagination: [https://uriyyo-fastapi-pagination.netlify.app/]