
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> str:
    return (f'Главная страница')


@app.get('/user/admin')
async def administrator() -> str:
    return (f'Вы вошли как администратор')


@app.get('/user/{user_id}')
async def user_number(user_id: int):
    return (f'Вы вошли как пользователь № {user_id}')


@app.get('/user')
async def user_info(username: str, age: int):
    return (f'Информация о пользователе. Имя: {username}, Возраст: {age}')