from database.models import Site
from database import get_db


# Создание шаблона страницы
def create_site_template_db(creator_id, site_name, site_code):
    db = next(get_db())
    new_site = Site(creator_id=creator_id, site_name=site_name, site_code=site_code)
    if not creator_id:
        return "Пользовактель не найден"
    db.add(new_site)
    db.commit()
    return f'Успешно добавлен: {new_site.site_id}'


# Получение списка шаблонов
def get_site_templates_db():
    db = next(get_db())
    all_sites = db.query(Site).all()
    return all_sites


# Получение деталей шаблона страницы
def get_site_template_by_id_db(site_id):
    db = next(get_db())
    exact_site = db.query(Site).filter_by(site_id=site_id).first()
    if exact_site:
        return exact_site
    else:
        return 'Шаблон не найден'


# Редактирование шаблона страницы
def edit_site_template_db(site_id, site_name_new, site_code_new):
    db = next(get_db())
    exact_site = db.query(Site).filter_by(site_id=site_id).first()
    if exact_site:
        exact_site.site_name = site_name_new
        exact_site.site_code = site_code_new
        db.commit()
        return 'Текст шаблона изменен.'
    else:
        return 'Шаблон не найден'


# Удаление шаблона страницы
def delete_site_template_db(site_id):
    db = next(get_db())
    exact_site = db.query(Site).filter_by(site_id=site_id).first()
    if exact_site:
        db.delete(exact_site)
        db.commit()
        return 'Шаблон успешно удалён'
    else:
        return 'Шаблон не найден'
