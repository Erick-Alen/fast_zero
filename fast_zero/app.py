from fastapi import FastAPI

from http import HTTPStatus

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def main():
    return '''
    <html>
      <head>
        <title> Olá mundo!</title>
      </head>
      <body>
        <h1> Olá mundo! </h1>
      </body>
    </html>
    '''
