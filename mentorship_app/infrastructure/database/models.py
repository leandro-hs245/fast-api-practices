from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), onupdate=func.now()
    )


class MentorModel(Base, TimestampMixin):
    __tablename__ = "mentors"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    speciality: Mapped[str] = mapped_column(String(75))


class StudentModel(Base, TimestampMixin):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    mentor_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("mentors.id"), nullable=True
    )
    mentor: Mapped[Optional[MentorModel]] = relationship()
