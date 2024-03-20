from database.models import User
from database import get_db
from database.security import create_access_token


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    get_all_users = db.query(User).all()
    return get_all_users


# Получить определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(user_id=user_id).first()
    if checker:
        return f'Пользователь найден. {checker.user_id}'
    else:
        return 'Пользователь не обнаружен'


# Регистрация пользователя
def register_user_db(username, phone_number, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return 'Такой номер телефона уже есть в базе'
    else:
        new_user = User(username=username, phone_number=phone_number, password=password)
        db.add(new_user)
        db.commit()
        return f'Успешно зарегистрирован: {new_user.user_id}'


# Логин
def login_user_db(username, password):
    db = next(get_db())
    login = db.query(User).filter_by(username=username, password=password).first()
    if login:
        token_data = {"user_id": login.user_id}
        access_token_data = create_access_token(token_data)
        return {"access_token": access_token_data, "token_type": "Bearer", "status": "Success"}
    else:
        return 'Неверный номер телефона или пароль'


#  Удаления пользователя
def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return f'Пользователь с ID {user_id} удален.'
    else:
        return 'Пользователь не найден.'


# Изменения данных пользователя
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        if edit_info == 'username':
            exact_user.username = new_info
        elif edit_info == 'surname':
            exact_user.surname = new_info
        db.commit()
        return 'Данные успешно изменены!'
    else:
        return 'Пользователь не найден'
