from dataclasses import dataclass
from typing import Optional


@dataclass
class Mentor:
    id: Optional[int] = None
    name: str
    speciality: str


@dataclass
class Student:
    id: Optional[int] = None
    name: str
    mentor_id: Optional[int] = None
