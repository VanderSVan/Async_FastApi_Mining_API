
INFO_MSG = {
    'db': {
        'create': "Database '{}' already exists."
    },
    'user': {
        'create': "User '{}' already exists."
    },
    'role': {
        'create': "Role '{}' already exists.",
        'join_user_to_role': "Role '{}' has already joined the user '{}'."
    }
}
SUCCESS_MSG = {
    'db': {
        'create': "Database '{}' has been created.",
        'drop': "Database '{}' has been successfully dropped."
    },
    'user': {
        'create': "User '{}' has been created",
        'drop': "User '{}' has been successfully dropped."
    },
    'role': {
        'create': "Role '{}' has been created",
        'drop': "Role '{}' has been successfully dropped.",
        'join_user_to_role': "Role '{}' now includes new user '{}'",
        'remove_user_from_role': "Role '{}' no longer includes user '{}'."
    },
    'privilege': {
        'grant': "All privileges have been granted to '{}'",
        'remove': "All privileges have been removed from '{}'"
    }

}
ERROR_MSG = {
    'db': {
        'drop': "Can not drop the db '{}', database does not exists."
    },
    'user': {
        'drop': "Can not drop user '{}', user does not exists."
    },
    'role': {
        'drop': "Can not drop role '{}', role does not exists.",
        'remove_user_from_role': "Role '{}' does not include user '{}'."
    }
}
