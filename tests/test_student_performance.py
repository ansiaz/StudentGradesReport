"""
Тесты для генерации отчета по успеваемости.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reports.student_performance import generate_student_performance_report
from models.student import Grade


def test_generate_student_performance_report():
    """Тест генерации отчета по успеваемости."""
    grades = [
        Grade("Иванов Иван", "Математика", "Петров П.П.", "2023-10-10", 5),
        Grade("Иванов Иван", "Физика", "Сидоров С.С.", "2023-10-12", 4),
        Grade("Петров Петр", "Математика", "Петров П.П.", "2023-10-10", 4),
        Grade("Петров Петр", "Физика", "Сидоров С.С.", "2023-10-12", 5),
    ]

    report = generate_student_performance_report(grades)

    assert len(report) == 2
    assert report[0]["student_name"] == "Иванов Иван"
    assert report[0]["average_grade"] == 4.5
    assert report[1]["student_name"] == "Петров Петр"
    assert report[1]["average_grade"] == 4.5


def test_empty_grades():
    """Тест с пустым списком оценок."""
    report = generate_student_performance_report([])
    assert report == []
