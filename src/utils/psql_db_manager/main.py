from psycopg2.extensions import connection as psycopg2_conn

from src.utils.psql_db_manager.core.base_classes import (
    Database,
    User,
    Role,
    Privilege
)


def create_all(connection: psycopg2_conn,
               db_name: str,
               username: str,
               user_password: str,
               role_name: str,
               ):
    db = Database(connection, db_name)
    user = User(connection, username, user_password)
    role = Role(connection, role_name)
    privilege = Privilege(connection)

    db.create()
    user.create()
    role.create()
    privilege.grant_all_privileges(db.name, role.name)
    role.join_user_to_role(user.name)


def drop_all(connection: psycopg2_conn,
             db_name: str,
             username: str,
             user_password: str,
             role_name: str
             ):
    db = Database(connection, db_name)
    user = User(connection, username, user_password)
    role = Role(connection, role_name)
    privilege = Privilege(connection)

    role.remove_user_from_role(user.name)
    privilege.remove_all_privileges(db.name, role.name)
    db.drop()
    user.drop()
    role.drop()


if __name__ == '__main__':
    from src.config import get_settings
    from src.utils.psql_db_manager.core.utils.connection import get_db_connect

    settings = get_settings()

    with get_db_connect(settings.get_psql_db_connection_data()) as conn:
        create_all(conn,
                   settings.PG_USER_DB,
                   settings.PG_USER,
                   settings.PG_USER_PASSWORD,
                   settings.PG_ROLE
                   )
