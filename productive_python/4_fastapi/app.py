# uvicorn app:app --reload --host 0.0.0.0 --port 2023 --proxy-headers

# curl -v -X POST -H 'Content-Type: application/json' -d '{
#   "name": "Jesus H. Christ"
# }' http://127.1:2023/hello

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.post('/hello')
async def hello(user: User):
    return f'Hello, {user.name}'


@app.get('/users')
async def user_list():
    return [
        User(name='Alex', age=19),
        User(name='Ben', age=89),
    ]
