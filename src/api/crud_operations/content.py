from datetime import datetime as dt
from typing import Literal

from sqlalchemy import update, insert

from src.api.schemas.content.base_schemas import (
    ContentPatchSchema,
    ContentPostSchema
)
from src.api.crud_operations.base_crud_operations import ModelOperation
from src.api.models.content import ContentModel
from src.api.crud_operations.utils.base_crud_utils import QueryExecutor

from src.api.crud_operations.utils.content import (
    build_query,
    check_input_content_data_for_patch,
    check_input_content_data_for_post
)

func_type = Literal['min'] | Literal['max'] | Literal['avg']


class ContentOperation(ModelOperation):
    def __init__(self, db):
        self.model = ContentModel
        self.model_name = 'ore_concentrate_content'
        self.db = db

    async def find_all_by_params(self, **kwargs) -> list[ContentModel] | list[None]:
        """
        Searches all contents by parameters
        :param kwargs: content parameters
        :return: Found list of `ContentModel` or list of None.
        """
        from_dt: dt = kwargs.get('from_dt')
        to_dt: dt = kwargs.get('to_dt')
        iron: float = kwargs.get('iron')
        silicon: float = kwargs.get('silicon')
        aluminum: float = kwargs.get('aluminum')
        calcium: float = kwargs.get('calcium')
        sulfur: float = kwargs.get('sulfur')
        ore_concentrate_id: int = kwargs.get('ore_concentrate_id')
        offset: int = kwargs.get('offset')
        limit: int = kwargs.get('limit')
        query = await build_query(self, from_dt, to_dt, iron, silicon,
                                  aluminum, calcium, sulfur, ore_concentrate_id,
                                  offset, limit
                                  )
        return await QueryExecutor.get_multiple_result(query, self.db)

    @check_input_content_data_for_patch
    async def patch_obj(self, id_: int, new_data: ContentPatchSchema) -> bool:
        """
        Updates content values into db with new data;
        :param id_: content id;
        :param new_data: new data to update.
        :return: True or raise exception if content is not found.
        """
        query = (update(self.model)
                 .where(self.model.id == id_)
                 .values(**new_data.dict(exclude_unset=True))
                 )
        return await QueryExecutor.patch_obj(query, self.db, self.model_name)

    @check_input_content_data_for_post
    async def add_obj(self, new_data: ContentPostSchema) -> bool:
        """
        Adds new content into db;
        :param new_data: content data.
        :return: True or raise exception if content cannot be added.
        """
        max_obj_id: int = await self.get_max_id()
        new_obj_data: dict = dict(id=max_obj_id + 1, **new_data.dict())

        query = insert(self.model).values(new_obj_data)
        return await QueryExecutor.add_obj(query, self.db, self.model_name)
