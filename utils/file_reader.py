"""
Утилиты для чтения CSV файлов.
"""

import csv
from typing import List, Dict, Any
from models.student import Grade


def read_csv_files(file_paths: List[str]) -> List[Grade]:
    """
    Чтение данных из CSV файлов.

    Args:
        file_paths: Список путей к CSV файлам

    Returns:
        List[Grade]: Список объектов оценок

    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если данные некорректны
    """
    all_grades = []

    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                required_columns = [
                    "student_name",
                    "subject",
                    "teacher_name",
                    "date",
                    "grade",
                ]
                if not all(col in reader.fieldnames for col in required_columns):
                    raise ValueError(
                        f"Файл {file_path} не содержит все необходимые колонки"
                    )

                for row in reader:
                    try:
                        grade = Grade(
                            student_name=row["student_name"].strip(),
                            subject=row["subject"].strip(),
                            teacher_name=row["teacher_name"].strip(),
                            date=row["date"].strip(),
                            grade=int(row["grade"]),
                        )
                        all_grades.append(grade)
                    except (ValueError, KeyError) as e:
                        raise ValueError(
                            f"Некорректные данные в файле {file_path}: {e}"
                        )

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не найден")
        except Exception as e:
            raise ValueError(f"Ошибка при чтении файла {file_path}: {e}")

    return all_grades
