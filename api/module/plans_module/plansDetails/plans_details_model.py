from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from api.database.database_base import engine
from uuid import uuid4

Base = declarative_base()

class PlansDetailsModel(Base):
    __tablename__ = "plans_details"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name = Column(String, nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, item) -> None:
        self.name = item.name

Base.metadata.create_all(engine)