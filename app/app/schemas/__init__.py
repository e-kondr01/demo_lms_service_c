from uuid import UUID

from pydantic import BaseModel


class ServiceCUnitSchema(BaseModel):
    id: UUID
    name: str


class UnitIDRequestBodySchema(BaseModel):
    ids: str
    name: str | None = None
