from database.models import Content
from database import get_db


# Добавить контент
def add_content_db(user_id, body, title):
    db = next(get_db())
    new_content = Content(user_id=user_id, body=body, title=title)
    db.add(new_content)
    db.commit()
    return f'Успешно добавлен: {new_content.id}'


# Получить полностью весь контент
def get_all_content_db():
    db = next(get_db())
    all_post = db.query(Content).all()
    return all_post


# Получить весь контент определённого пользователя
def get_users_content(user_id):
    db = next(get_db())
    exact_content = db.query(Content).filter_by(user_id=user_id).all()
    if exact_content:
        return exact_content
    else:
        return 'Контент не найден'


# Редактировать определённый контент пользователя
def edit_users_content(id, new_text, new_title):
    db = next(get_db())
    exact_content = db.query(Content).filter_by(id=id).first()
    if exact_content:
        exact_content.body = new_text
        exact_content.title = new_title
        db.commit()
        return 'Текст изменен.'
    else:
        return 'Контент не найден'


# Удалить определённый контент
def delete_users_content(id):
    db = next(get_db())
    exact_content = db.query(Content).filter_by(id=id).first()
    if exact_content:
        db.delete(exact_content)
        db.commit()
        return 'Контент успешно удалён'
    else:
        return 'Пост не найден'
