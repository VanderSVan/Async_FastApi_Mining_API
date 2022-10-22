from sqlalchemy import select, and_, desc
from sqlalchemy.sql.selectable import Select

from src.api.models.content import ContentModel
from src.api.schemas.content.base_schemas import (
    ContentPatchSchema,
    ContentPostSchema,
)
from src.api.crud_operations.utils.ore_concentrate import check_ore_concentrate_existence
from src.utils.exceptions.base import CRUDException


async def build_query(self, from_dt, to_dt, iron, silicon,
                      aluminum, calcium, sulfur, ore_concentrate_id,
                      offset, limit
                      ) -> Select:
    """
    Builds complex query.
    """
    return (
            select(self.model)
            .where(
                   and_(
                        (ContentModel.datetime >= from_dt
                         if from_dt is not None else True),
                        (ContentModel.datetime <= to_dt
                         if to_dt is not None else True),
                        (ContentModel.iron_percent >= iron
                         if iron is not None else True),
                        (ContentModel.silicon_percent <= silicon
                         if silicon is not None else True),
                        (ContentModel.aluminum_percent <= aluminum
                         if aluminum is not None else True),
                        (ContentModel.calcium_percent <= calcium
                         if calcium is not None else True),
                        (ContentModel.sulfur_percent <= sulfur
                         if sulfur is not None else True),
                        (ContentModel.ore_concentrate_id == ore_concentrate_id
                         if ore_concentrate_id is not None else True),
                        )
            )
            .order_by(desc(self.model.datetime))
            .offset(offset)
            .limit(limit)
            )


def check_input_content_data_for_patch(func):
    async def wrapper(
            self,
            id_: int,
            new_data: ContentPatchSchema,
            *args,
            **kwargs
    ):
        """
        Checks input data for patch `ore concentrate content` object.
        """
        old_obj: ContentModel = await self.find_by_id_or_404(id_)
        old_data: ContentPatchSchema = ContentPatchSchema(**old_obj.__dict__)
        data_to_update: dict = new_data.dict(exclude_unset=True)
        merged_data: ContentPatchSchema = old_data.copy(update=data_to_update)

        await check_ore_concentrate_existence(merged_data.ore_concentrate_id, self.db)
        await _check_datetime_duplicate(self, merged_data)

        return await func(self, id_, new_data, *args, **kwargs)

    return wrapper


def check_input_content_data_for_post(func):
    async def wrapper(
            self,
            new_data: ContentPostSchema,
            *args,
            **kwargs
    ):
        """
        Checks input data for post `content` object.
        """
        await check_ore_concentrate_existence(new_data.ore_concentrate_id, self.db)
        await _check_datetime_duplicate(self, new_data)

        return await func(self, new_data, *args, **kwargs)

    return wrapper


async def _check_datetime_duplicate(
        self,
        new_data: ContentPatchSchema | ContentPostSchema
) -> None:
    """
    Searches for existing data, if found then raise an exception.
    """
    duplicate: ContentModel | None = await self.find_all_by_params(
        from_dt=new_data.datetime,
        to_dt=new_data.datetime,
        ore_concentrate_id=new_data.ore_concentrate_id,
    )
    if duplicate:
        CRUDException.raise_duplicate_err(self.model_name)
