# !!! Inserting data into an empty database only !!!
from sqlalchemy import select, insert, func
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from src.db.db_sqlalchemy import BaseModel
from src.api.models.user import UserModel
from src.api.models.ore_concentrate import OreConcentrateModel
from src.api.models.content import ContentModel
from src.utils.db_populating.data_preparation import prepare_data_for_insertion
from src.utils.db_populating.input_data import (
    users_json,
    ore_concentrates_json,
    ore_concentrates_content_json
)


async def insert_data_to_db(async_session: AsyncSession) -> None:
    """Inserts prepared data into an empty database only!"""
    user_count: int = await _get_count(UserModel, async_session)
    ore_concentrates_count: int = await _get_count(OreConcentrateModel, async_session)
    ore_concentrates_content_count: int = await _get_count(ContentModel, async_session)
    total_count = sum([user_count, ore_concentrates_count, ore_concentrates_content_count])

    if total_count == 0:
        prepared_data: dict = prepare_data_for_insertion(users_json,
                                                         ore_concentrates_json,
                                                         ore_concentrates_content_json
                                                         )
        await _insert_full_data_to_db(prepared_data, async_session)
        logger.success("Data has been added to db")
    else:
        logger.info("Data cannot be inserted into the database because the database is not empty")


async def _get_count(model: BaseModel,
                     async_session: AsyncSession
                     ) -> int:
    query = select(func.count(model.id))
    query_result = await async_session.execute(query)
    return query_result.scalar()


async def _insert_full_data_to_db(data: dict,
                                  async_session: AsyncSession
                                  ) -> None:
    for model, data_list in data.items():
        await _insert_data_to_db(data_list, model, async_session)
    await async_session.commit()


async def _insert_data_to_db(data: list,
                             model: BaseModel,
                             async_session: AsyncSession
                             ) -> None:
    insert_query = insert(model).values(data)
    await async_session.execute(insert_query)
