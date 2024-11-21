import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from app.db import async_session_factory
from app.models import ServiceCUnit


async def generate_units(session: AsyncSession):
    for i in range(1, 101):
        name = f"Задание {i}"
        unit = ServiceCUnit(name=name)
        session.add(unit)
        await session.commit()


async def main():
    async with async_session_factory() as session:
        await generate_units(session)


asyncio.run(main())
