from fastapi import APIRouter
from database.contentservice import (add_content_db,
                                     get_all_content_db,
                                     get_users_content,
                                     edit_users_content,
                                     delete_users_content)
from content import PublicContentValidator, EditContentValidator

content_router = APIRouter(prefix='/content', tags=['Работа с контентом'])


# Добавить контент
@content_router.post('/add-content')
async def add_content(data: PublicContentValidator):
    result = add_content_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Контент не найден"}


# Получить полностью весь контент
@content_router.get('/all-content')
async def get_all_content():
    result = get_all_content_db()
    return {'message': result}


# Получить весь контент определённого пользователя
@content_router.get('/user-content')
async def get_content(user_id):
    result = get_users_content(user_id)
    if result:
        return {'message': result}
    else:
        return {'message': "Контента нет."}


# Редактировать определённый контент пользователя
@content_router.put('/edit-content')
async def edit_content(data: EditContentValidator):
    result = edit_users_content(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Ошибка при изменении"}


# Удалить определённый контент
@content_router.delete('/delete-content')
async def delete_content(id):
    return delete_users_content(id)
