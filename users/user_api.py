
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from users import RegisterValidator, EditUserValidator
from database.userservice import (register_user_db,
                                  login_user_db,
                                  get_all_users_db,
                                  get_exact_user_db,
                                  edit_user_info_db,
                                  delete_user_db)

# Создать компонент
user_router = APIRouter(prefix='/users', tags=['Управления с пользователями'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# Регистрация пользователя
@user_router.post('/register')
async def register_user(data: RegisterValidator):
    result = register_user_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Такой пользователь уже имеется'}


# Получение всех пользователей
@user_router.get('/all-user')
async def get_all_users():
    return get_all_users_db()


# Получения определенного пользователя
@user_router.get('/one-user')
async def get_user(user_id: int):
    exact_user = get_exact_user_db(user_id)
    return exact_user


# Изменение информации о пользователе
@user_router.put('/edit-user')
async def edit_user_db(data: EditUserValidator):
    change_data = data.model_dump()
    result = edit_user_info_db(**change_data)
    print(result)
    return result


# Запрос для логина
@user_router.post('/login-user')
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = login_user_db(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail='Неверный номер или пароль')
    else:
        return user


# Удаления пользователя
@user_router.delete('/delete-user')
async  def delete_user(user_id):
    return delete_user_db(user_id)
