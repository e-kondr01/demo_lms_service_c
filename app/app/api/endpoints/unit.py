from uuid import UUID

from fastapi import APIRouter
from fastapi_sqlalchemy_toolkit import comma_list_query, get_comma_list_values
from sqlalchemy import select

from app.api.deps import Session
from app.models import Unit
from app.schemas import UnitSchema

router = APIRouter()


@router.get("")
async def get_units(
    session: Session,
    ids: comma_list_query,
    name: str | None = None,
    limit: int = 20,
) -> list[UnitSchema]:
    stmt = (
        select(Unit).where(Unit.id.in_(get_comma_list_values(ids, UUID))).limit(limit)
    )
    if name:
        stmt = stmt.where(Unit.name.icontains(f"%{name}%"))
    return (await session.execute(stmt)).scalars().all()  # type: ignore


@router.get("/ids")
async def get_unit_ids(
    session: Session,
    ids: comma_list_query,
    name: str | None = None,
) -> list[UUID]:
    ids_list = get_comma_list_values(ids, UUID)
    if not ids:
        return ids_list
    stmt = select(Unit.id).where(Unit.id.in_(ids_list))
    if name:
        stmt = stmt.where(Unit.name.icontains(f"%{name}%"))
    return (await session.execute(stmt)).scalars().all()  # type: ignore