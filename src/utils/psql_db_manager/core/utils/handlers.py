import sys
from dataclasses import dataclass

from psycopg2.extensions import connection as psycopg2_conn
from logs.settings import logger

from src.utils.psql_db_manager.core.settings.response_messages import (
    INFO_MSG,
    SUCCESS_MSG,
    ERROR_MSG
)
from src.config import get_settings

setting = get_settings()


@dataclass
class Messenger:
    sql_obj: str
    info_msg = INFO_MSG
    success_msg = SUCCESS_MSG
    error_msg = ERROR_MSG

    def send_success_msg(self, method, *args) -> None:
        logger.success(
            self.success_msg[self.sql_obj][method].format(*args)
        )

    def send_info_msg(self, method, *args) -> None:
        logger.info(
            self.info_msg[self.sql_obj][method].format(*args)
        )

    def send_error_msg(self, method, *args) -> None:
        logger.error(
            self.error_msg[self.sql_obj][method].format(*args)
        )


class SQLExceptionHandler:

    @classmethod
    def print_sql_notices(cls, notices: list):
        pure_notices = cls._process_notices(notices)
        if notices:
            logger.info(f"\n===SQL notices==\n"
                        f"\n{pure_notices}\n"
                        f"\n===End SQL notices===")

    @staticmethod
    def print_sql_error(error: Exception):
        logger.error(f"\n===SQL error===\n"
                     f"\n{error}\n"
                     f"\n===End SQL error===")

    @staticmethod
    def _process_notices(notices: list) -> str:
        if len(notices) > 1:
            pure_notices_list = [
                notice.split(sep=':')[1].lstrip().rstrip() for notice in notices
            ]
            pure_result = "\n".join(pure_notices_list)
        elif len(notices) == 0:
            pure_result = ""
        else:
            pure_result = notices[0].split(sep=':')[1].lstrip().rstrip()
        return pure_result


def print_processed_psycopg2_exception(err):
    err_type, err_obj, traceback = sys.exc_info()  # get details about the exception
    line_num = traceback.tb_lineno  # get the line number when exception occurred
    logger.exception(f"===psycopg2 exception in more detail==="
                     f"psycopg2 ERROR: {err} on line number: {line_num}\n"
                     f"psycopg2 traceback: {traceback} -- type:: {err_type}\n"
                     f"extensions.Diagnostics: {err.diag}\n"
                     f"obj=, {err_obj.args}\n"
                     f"pgerror: {err.pgerror}\n"
                     f"pgcode: {err.pgcode}\n"
                     f"===end psycopg2 exception===\n")


def handle_sql_exceptions(error):
    def outer_wrapper(func):
        def inner_wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)

            except error as err:
                SQLExceptionHandler.print_sql_error(err)

            except Exception as default_err:
                logger.exception(f"Got an exception: {default_err}"
                                 f"Type exception = {type(default_err)}")
            finally:
                if isinstance(self.connection, psycopg2_conn):
                    SQLExceptionHandler.print_sql_notices(self.connection.notices)

        return inner_wrapper

    return outer_wrapper
