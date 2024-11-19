from uuid import UUID

from pydantic import BaseModel


class ServiceCUnitSchema(BaseModel):
    id: UUID
    name: str
