from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from api.database.database_base import engine
import uuid

Base = declarative_base()

class PlansRelationshipModel(Base):
    __tablename__ = "plans_relationship"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    plan_id = Column(UUID(as_uuid=True), ForeignKey("plans.id"), primary_key=True)
    plans_details_id = Column(UUID(as_uuid=True), ForeignKey("plans_details.id"), primary_key=True)
    enabled = Column(Boolean(), default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, item) -> None:
        self.plan_id = item.plan_id
        self.plans_details_id = item.plans_details_id


class PlansModel(Base):
    __tablename__ = "plans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    details = relationship('PlansDetailsModel', secondary = 'plans_relationship')


class PlansDetailsModel(Base):
    __tablename__ = "plans_details"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String, nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, item) -> None:
        self.name = item.name


Base.metadata.create_all(engine)