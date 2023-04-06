from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from api.database.database_base import engine
import uuid

Base = declarative_base()

class CompanyModel(Base):
    __tablename__ = "company"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    company_name = Column(String, nullable=False)
    logo_url = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

Base.metadata.create_all(engine)
