"""
Тесты для основного скрипта.
"""

import pytest
import sys
import os
from unittest.mock import patch, mock_open

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import parse_arguments, display_report


def test_parse_arguments():
    """Тест парсинга аргументов."""
    test_args = ["--files", "file1.csv", "file2.csv", "--report", "student-performance"]

    with patch("sys.argv", ["main.py"] + test_args):
        args = parse_arguments()
        assert args.files == ["file1.csv", "file2.csv"]
        assert args.report == "student-performance"


def test_display_report_student_performance(capsys):
    """Тест отображения отчета по успеваемости."""
    report_data = [
        {"student_name": "Иванов Иван", "average_grade": 4.75},
        {"student_name": "Петров Петр", "average_grade": 4.50},
    ]

    display_report(report_data, "student-performance")

    captured = capsys.readouterr()
    assert "Иванов Иван" in captured.out
    assert "4.75" in captured.out
    assert "Петров Петр" in captured.out
