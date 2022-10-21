
QUERIES = {
    'db': {
        'create': "CREATE DATABASE {}",
        'drop': "DROP DATABASE {}",
        'check_existence': "SELECT COUNT(*) = 1 FROM pg_catalog.pg_database WHERE datname = '{}'",
    },
    'user': {
        'create': "CREATE USER {} WITH PASSWORD '{}'",
        'drop': "DROP USER IF EXISTS {}",
        'check_existence': "SELECT COUNT(*)=1 FROM pg_roles WHERE rolname = '{}'",
    },
    'role': {
        'create': "CREATE ROLE {}",
        'drop': "DROP ROLE IF EXISTS {}",
        'check_existence': "SELECT COUNT(*)=1 FROM pg_roles WHERE rolname = '{}'",
        'check_membership': "SELECT COUNT(rolname) = 1 "
                            "FROM pg_authid "
                            "WHERE EXISTS ("
                            "SELECT member FROM pg_auth_members "
                            "WHERE member = pg_authid.oid AND rolname = '{}'"
                            ")",
        'join_user_to_role': "GRANT {} TO {}",
        'remove_user_from_role': "REVOKE {} FROM {}"
    },
    'privilege': {
        'grant': """
                 GRANT ALL ON DATABASE {} TO {};
                 GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {};
                 """,
        'remove': """
                  REVOKE ALL ON DATABASE {} FROM {};
                  REVOKE ALL ON SCHEMA public FROM {};
                  """
    }
}
