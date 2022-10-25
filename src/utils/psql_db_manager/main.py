from dataclasses import dataclass

from psycopg2.extensions import connection as psycopg2_conn

from src.utils.psql_db_manager.core.base_classes import (
    Database,
    User,
    Role,
    Privilege
)


@dataclass
class SQLOperation:
    connection: psycopg2_conn
    db_name: str | None = None
    username: str | None = None
    user_password: str | None = None
    role_name: str | None = None

    def create_all(self):
        self._create_db()
        self._create_role()
        self._create_user()
        self._grant_privileges_to_role()
        self._join_user_to_role()
        self._grant_privileges_to_user()

    def drop_all(self):
        self._remove_user_from_role()
        self._remove_privileges_from_role()
        self._remove_privileges_from_user()
        self._drop_user()
        self._drop_role()
        self._drop_db()

    def _create_db(self):
        if self.db_name:
            Database(self.connection, self.db_name).create()

    def _drop_db(self):
        if self.db_name:
            Database(self.connection, self.db_name).drop()

    def _create_user(self):
        if self.username:
            User(self.connection, self.username, self.user_password).create()

    def _drop_user(self):
        if self.username:
            User(self.connection, self.username, self.user_password).drop()

    def _create_role(self):
        if self.role_name:
            Role(self.connection, self.role_name).create()

    def _drop_role(self):
        if self.role_name:
            Role(self.connection, self.role_name).drop()

    def _grant_privileges_to_role(self):
        if self.role_name and self.db_name:
            Privilege(self.connection).grant_all_privileges(self.db_name, self.role_name)

    def _remove_privileges_from_role(self):
        if self.role_name and self.db_name:
            Privilege(self.connection).remove_all_privileges(self.db_name, self.role_name)

    def _grant_privileges_to_user(self):
        if self.username and self.db_name and not self.role_name:
            Privilege(self.connection).grant_all_privileges(self.db_name, self.username)

    def _remove_privileges_from_user(self):
        if self.username and self.db_name and not self.role_name:
            Privilege(self.connection).remove_all_privileges(self.db_name, self.username)

    def _join_user_to_role(self):
        if self.role_name and self.username:
            Role(self.connection, self.role_name).join_user_to_role(self.username)

    def _remove_user_from_role(self):
        if self.role_name and self.username:
            Role(self.connection, self.role_name).remove_user_from_role(self.username)


if __name__ == '__main__':
    from src.config import get_settings
    from src.utils.psql_db_manager.core.utils.connection import get_db_connect

    settings = get_settings()

    with get_db_connect(settings.get_psql_db_connection_data()) as conn:
        SQLOperation(conn,
                     settings.PG_USER_DB,
                     settings.PG_USER,
                     settings.PG_USER_PASSWORD,
                     settings.PG_ROLE
                     ).drop_all()
