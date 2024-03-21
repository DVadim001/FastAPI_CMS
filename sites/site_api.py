from fastapi import APIRouter
from database.siteservice import (create_site_template_db,
                                  get_site_templates_db,
                                  get_site_template_by_id_db,
                                  edit_site_template_db,
                                  delete_site_template_db)
from sites import PublicSiteValidator, EditSiteValidator

site_router = APIRouter(prefix='/site', tags=['Работа с шаблонами'])


# Создание шаблона страницы
@site_router.post('/add-site')
async def create_site_template(data: PublicSiteValidator):
    result = create_site_template_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Шаблон не найден"}


# Получение списка шаблонов
@site_router.get('/all-site')
async def get_site_templates():
    result = get_site_templates_db()
    return {'message': result}


# Получение деталей шаблона страницы
@site_router.get('/one-site')
async def get_site_template_by_id(site_id):
    result = get_site_template_by_id_db(site_id)
    if result:
        return {'message': result}
    else:
        return {'message': "Контента нет."}


# Редактирование шаблона страницы
@site_router.put('/edit-site')
async def edit_site_template(data: EditSiteValidator):
    result = edit_site_template_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Ошибка при изменении"}


# Удаление шаблона страницы
@site_router.delete('/delete-site')
async def delete_site_template(site_id):
    return delete_site_template_db(site_id)
