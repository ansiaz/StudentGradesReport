#!/usr/bin/env python3
"""
Основной скрипт для генерации отчетов по успеваемости студентов.
"""

import argparse
import sys
from typing import List, Dict, Any
from tabulate import tabulate

from reports.student_performance import generate_student_performance_report
from utils.file_reader import read_csv_files


def parse_arguments():
    """Парсинг аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description="Генерация отчетов по успеваемости студентов"
    )

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV файлам с данными об успеваемости",
    )

    parser.add_argument(
        "--report",
        choices=["student-performance"],
        required=True,
        help="Тип отчета для генерации",
    )

    return parser.parse_args()


def display_report(report_data: List[Dict[str, Any]], report_type: str):
    """Отображение отчета в консоли."""
    if report_type == "student-performance":
        headers = ["Студент", "Средняя оценка"]
        table_data = [
            [row["student_name"], row["average_grade"]] for row in report_data
        ]
        print(tabulate(table_data, headers=headers, tablefmt="grid", floatfmt=".2f"))


def main():
    """Основная функция."""
    try:
        args = parse_arguments()

        students_data = read_csv_files(args.files)

        if args.report == "student-performance":
            report_data = generate_student_performance_report(students_data)
        else:
            raise ValueError(f"Неизвестный тип отчета: {args.report}")

        display_report(report_data, args.report)

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
