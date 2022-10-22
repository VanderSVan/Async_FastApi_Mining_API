from dataclasses import dataclass
from typing import Any, Literal

from psycopg2 import Error
from psycopg2.extensions import (
    connection as psycopg2_conn,
    cursor as psycopg2_cursor
)
from src.utils.psql_db_manager.core.utils import (
    Messenger,
    handle_exceptions
)
from src.utils.psql_db_manager.core.settings.sql_queries import QUERIES


@dataclass
class SQLOperation:
    def __init__(self,
                 connection: psycopg2_conn,
                 sql_obj: (Literal['db'] |
                           Literal['user'] |
                           Literal['role'] |
                           Literal['privilege']),
                 queries=QUERIES,
                 ) -> None:
        self.connection = connection
        self.sql_obj = sql_obj
        self.queries = queries
        self.messenger = Messenger(self.sql_obj)

    def _positive_action(self, existing: Any, method: str, *args) -> None:
        if existing:
            self.messenger.send_info_msg(method, *args)
        else:
            self._execute_query(method, *args)
            self.messenger.send_success_msg(method, *args)

    def _negative_action(self, existing: Any, method: str, *args) -> None:
        if existing:
            self._execute_query(method, *args)
            self.messenger.send_success_msg(method, *args)
        else:
            self.messenger.send_error_msg(method, *args)

    @handle_exceptions(Error)
    def _check_out(self, method: str, *args) -> Any:
        cursor = self._execute_query(method, *args)
        already_existing, = cursor.fetchone()
        return already_existing

    @handle_exceptions(Error)
    def _execute_query(self, method: str, *args) -> psycopg2_cursor:
        cursor = self.connection.cursor()
        methods: dict = self.queries[self.sql_obj]
        query: str = methods[method].format(*args)
        cursor.execute(query)
        return cursor


class Database(SQLOperation):
    def __init__(self,
                 connection,
                 name: str,
                 sql_obj: Literal['db'] = 'db'
                 ) -> None:
        super().__init__(connection, sql_obj)
        self.name = name

    def create(self) -> None:
        existing: Any = self._check_out('check_existence', self.name)
        self._positive_action(existing, 'create', self.name)

    def drop(self) -> None:
        already_existing: Any = self._check_out('check_existence', self.name)
        self._negative_action(already_existing, 'drop', self.name)


class User(SQLOperation):
    def __init__(self,
                 connection,
                 name: str,
                 password: str,
                 sql_obj: Literal['user'] = 'user'
                 ) -> None:
        super().__init__(connection, sql_obj)
        self.name = name
        self.password = password

    def create(self) -> None:
        existing: Any = self._check_out('check_existence', self.name, self.password)
        self._positive_action(existing, 'create', self.name, self.password)

    def drop(self) -> None:
        already_existing: Any = self._check_out('check_existence', self.name, self.password)
        self._negative_action(already_existing, 'drop', self.name, self.password)


class Role(SQLOperation):
    def __init__(self,
                 connection,
                 name: str,
                 sql_obj: Literal['role'] = 'role'
                 ) -> None:
        super().__init__(connection, sql_obj)
        self.name = name

    def create(self) -> None:
        existing: Any = self._check_out('check_existence', self.name)
        self._positive_action(existing, 'create', self.name)

    def drop(self) -> None:
        already_existing: Any = self._check_out('check_existence', self.name)
        self._negative_action(already_existing, 'drop', self.name)

    def join_user_to_role(self, username: str):
        already_joined: Any = self._check_out('check_membership', username)
        self._positive_action(already_joined,
                              'join_user_to_role',
                              self.name,
                              username
                              )

    def remove_user_from_role(self, username: str):
        already_joined: Any = self._check_out('check_membership', username)
        self._negative_action(already_joined,
                              'remove_user_from_role',
                              self.name,
                              username
                              )


class Privilege(SQLOperation):
    def __init__(self,
                 connection,
                 sql_obj: Literal['privilege'] = 'privilege'
                 ) -> None:
        super().__init__(connection, sql_obj)

    def grant_all_privileges(self, db_name: str, username_or_role_name: str):
        self._execute_query('grant', db_name, username_or_role_name, username_or_role_name)
        self.messenger.send_success_msg('grant', username_or_role_name)

    def remove_all_privileges(self, db_name: str, username_or_role_name: str):
        self._execute_query('remove', db_name, username_or_role_name, username_or_role_name)
        self.messenger.send_success_msg('remove', username_or_role_name)
