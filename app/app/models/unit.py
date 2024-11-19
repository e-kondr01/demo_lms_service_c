from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class ServiceCUnit(Base):
    name: Mapped[str] = mapped_column(String(255), index=True)
