from typing import Generator
from contextlib import contextmanager

from psycopg2 import connect, OperationalError
from psycopg2.extensions import (
    connection as psycopg2_conn,
    ISOLATION_LEVEL_AUTOCOMMIT
)
from logs.settings import logger

from src.utils.psql_db_manager.core.utils.type_annotations import DatabaseConnectionData
from src.utils.psql_db_manager.core.utils.handlers import print_processed_psycopg2_exception


@contextmanager
def get_db_connect(connection_data: DatabaseConnectionData,
                   isolation_level: int = ISOLATION_LEVEL_AUTOCOMMIT,
                   extra_exc_info: bool = False
                   ) -> Generator[psycopg2_conn, None, None]:
    try:
        connection = connect(**connection_data._asdict())
        connection.set_isolation_level(isolation_level)
        logger.info("POSTGRES CONNECTION OPEN...")
    except OperationalError as err:
        logger.exception("Error: Unable to connect!"
                         "\nInput connection data is probably wrong.\n")
        if extra_exc_info:
            print_processed_psycopg2_exception(err)

    yield connection

    connection.close()
    logger.info("POSTGRES CONNECTION CLOSE.")
