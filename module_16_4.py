from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel


'''
Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
'''

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post("/user/{user_name}/{age}", response_model=str)
async def create_user(user: User, user_name: Annotated[str, Path(min_length=4, max_length=20, description="Enter username", example="Vladimir")],
        age: int = Path(ge=18, le=120, description="Enter age", example=56)) -> str:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=user_name, age=age)
    users.append(new_user)
    return new_user
    return  f"User {new_id} is registered"


@app.put("/user/{user_id}/{user_name}/{age}")
async def update_user(user_name: Annotated[str, Path(min_length=4, max_length=20, description="Enter username", example="Igor")],
        age: int = Path(ge=18, le=120, description="Enter age", example=56),
        user_id: int = Path(ge=0)) -> str:
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.username = user_name
            existing_user.age = age
            return f"The user {user_id} is updated."
    raise HTTPException(status_code=404, detail="Пользователь не найден.")


@app.delete("/user/{user_id}", response_model=str)
async def delete_user(user_id: int = Path(ge=0)) -> str:
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users.pop(index)
            return f"Пользователь с ID {user_id} удален."

    raise HTTPException(status_code=404, detail="Пользователь не найден.")

# uvicorn module_16_4:app --reload