from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Mentor:
    name: str
    speciality: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Student:
    name: str
    id: Optional[int] = None
    mentor_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
