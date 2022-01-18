from app import app
from hello_db.models_manager import UserManager


@app.cli.command('init_db')
def init_db() -> None:
    print('Start of initialization')

    user_manager = UserManager()

    try:
        user_manager.init_table()
    except Exception as error:
        raise error

    print('The database was successfully initialized')


@app.cli.command('drop_db')
def drop_db() -> None:
    print('Start of dropping')

    user_manager = UserManager()

    try:
        user_manager.drop_table()
    except Exception as error:
        raise error

    print('The database was successfully dropped')


