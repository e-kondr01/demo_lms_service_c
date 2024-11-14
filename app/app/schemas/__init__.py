from uuid import UUID

from pydantic import BaseModel


class UnitSchema(BaseModel):
    id: UUID
    name: str
