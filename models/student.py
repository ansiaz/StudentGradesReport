"""
Модель данных студента.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Grade:
    """Модель оценки студента."""

    student_name: str
    subject: str
    teacher_name: str
    date: str
    grade: int


@dataclass
class Student:
    """Модель студента с оценками."""

    name: str
    grades: List[Grade]

    @property
    def average_grade(self) -> float:
        """Вычисление средней оценки студента."""
        if not self.grades:
            return 0.0
        return sum(grade.grade for grade in self.grades) / len(self.grades)
