from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse

from fast_zero.schemas import UserDB, UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def main():
    return """
      <html>
        <head>
          <title> Olá mundo!</title>
        </head>
        <body>
          <h1> Olá mundo! </h1>
        </body>
      </html>"""


database = []


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_w_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_w_id)
    return user_w_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_w_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_w_id
    return user_w_id
    return 'Usuário criado com sucesso!', HTTPStatus.CREATED


@app.delete(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_class=JSONResponse
)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    del database[user_id - 1]
    return {'Message': 'User Deleted'}
