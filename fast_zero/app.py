from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


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
