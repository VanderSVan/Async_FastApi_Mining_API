from datetime import datetime as dt

from src.utils.auth.password_cryptograph import PasswordCryptographer
from src.api.models.user import UserModel
from src.api.models.ore_concentrate import OreConcentrateModel
from src.api.models.content import ContentModel


def prepare_data_for_insertion(users: list,
                               ore_concentrates: list,
                               ore_concentrates_content: list
                               ) -> dict:
    """Main function."""
    users: list[dict] = encode_user_passwords(users)
    ore_concentrates_content: list[dict] = process_dt_objects(ore_concentrates_content)
    return {
        UserModel: users,
        OreConcentrateModel: ore_concentrates,
        ContentModel: ore_concentrates_content
    }


def encode_user_passwords(users: list[dict]):
    for user in users:
        user_password = user.get('password')
        user_hashed_password = user.get('hashed_password')

        if user_password:
            hashed_password = PasswordCryptographer.bcrypt(user_password)
            user['hashed_password'] = hashed_password
            del user['password']

        elif user_hashed_password:
            pass

        else:
            raise ValueError('user_json should have password field')

    return users


def process_dt_objects(data: list[dict]) -> list[dict]:
    return [_process_single_dt_object(obj) for obj in data]


def _process_single_dt_object(obj_dt: dict) -> dict:
    if isinstance(obj_dt.get('datetime'), str):
        obj_dt['datetime'] = dt.strptime(obj_dt['datetime'], '%Y-%m-%dT%H:%M:%S')
    return obj_dt
