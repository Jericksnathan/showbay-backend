from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    external_summary = Column(Text)
