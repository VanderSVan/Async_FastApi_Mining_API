import argparse

from src.config import get_settings
from src.utils.psql_db_manager.main import create_all, drop_all
from src.utils.psql_db_manager.core.utils.connection import get_db_connect

settings = get_settings()


def create_arguments():
    parser = argparse.ArgumentParser(
        prog="Creation or deletion db",
        description="By default info is taken from env variables.",
        epilog="Try '--create_db'"
    )
    parser.add_argument('-d', '--db_name', type=str, metavar="", default=None,
                        help='assign db name')
    parser.add_argument('-u', '--user_name', type=str, metavar="", default=None,
                        help='assign user name')
    parser.add_argument('-p', '--user_password', type=str, metavar="", default=None,
                        help='assign user password')
    parser.add_argument('-r', '--role_name', type=str, metavar="", default=None,
                        help='assign role name')
    parser.add_argument('--create_db', action='store_true', help='create db with params')
    parser.add_argument('--drop_db', action='store_true', help='delete db with all params')
    return parser.parse_args()


def main():
    args = create_arguments()

    with get_db_connect(settings.get_psql_db_connection_data()) as conn:
        parameters = dict(
            connection=conn,
            db_name=args.db_name if args.db_name else settings.PG_USER_DB,
            username=args.user_name if args.user_name else settings.PG_USER,
            user_password=args.user_password if args.user_password else settings.PG_USER_PASSWORD,
            role_name=args.role_name if args.role_name else settings.PG_ROLE
        )
        if args.create_db:
            create_all(**parameters)
        elif args.drop_db:
            drop_all(**parameters)
        else:
            raise ValueError("arguments '--create_db' and '--drop_db' "
                             "cannot be empty at the same time.")
