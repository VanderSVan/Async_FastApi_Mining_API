from typing import NoReturn

from sqlalchemy.ext.asyncio import AsyncSession

from src.api.crud_operations.ore_concentrate import OreConcentrateOperation


async def check_ore_concentrate_existence(ore_concentrate_id: int,
                                          async_session: AsyncSession
                                          ) -> NoReturn:
    ore_concentrate_crud = OreConcentrateOperation(async_session)
    await ore_concentrate_crud.find_by_id_or_404(ore_concentrate_id)
