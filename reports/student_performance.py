"""
Генерация отчета по успеваемости студентов.
"""

from typing import List, Dict, Any
from collections import defaultdict
from models.student import Grade, Student


def generate_student_performance_report(grades: List[Grade]) -> List[Dict[str, Any]]:
    """
    Генерация отчета по успеваемости студентов.

    Args:
        grades: Список оценок студентов

    Returns:
        List[Dict]: Отсортированный список студентов с средними оценками
    """
    students_grades = defaultdict(list)
    for grade in grades:
        students_grades[grade.student_name].append(grade)

    students = [
        Student(name=name, grades=grades_list)
        for name, grades_list in students_grades.items()
    ]

    sorted_students = sorted(students, key=lambda x: x.average_grade, reverse=True)

    report_data = [
        {"student_name": student.name, "average_grade": round(student.average_grade, 2)}
        for student in sorted_students
    ]

    return report_data
