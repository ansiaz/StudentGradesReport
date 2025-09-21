"""
Тесты для чтения CSV файлов.
"""

import pytest
import sys
import os
from unittest.mock import mock_open, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.file_reader import read_csv_files
from models.student import Grade


def test_read_csv_files():
    """Тест чтения CSV файлов."""
    csv_content = """student_name,subject,teacher_name,date,grade
Иванов Иван,Математика,Петров П.П.,2023-10-10,5
Петров Петр,Физика,Сидоров С.С.,2023-10-12,4"""

    with patch("builtins.open", mock_open(read_data=csv_content)):
        grades = read_csv_files(["test.csv"])

        assert len(grades) == 2
        assert grades[0].student_name == "Иванов Иван"
        assert grades[0].grade == 5
        assert grades[1].student_name == "Петров Петр"
        assert grades[1].grade == 4


def test_read_multiple_files():
    """Тест чтения нескольких файлов."""
    csv_content_1 = """student_name,subject,teacher_name,date,grade
Иванов Иван,Математика,Петров П.П.,2023-10-10,5"""

    csv_content_2 = """student_name,subject,teacher_name,date,grade
Петров Петр,Физика,Сидоров С.С.,2023-10-12,4"""

    mock_files = {"file1.csv": csv_content_1, "file2.csv": csv_content_2}

    def mock_file_open(filename, *args, **kwargs):
        return mock_open(read_data=mock_files[filename])(filename, *args, **kwargs)

    with patch("builtins.open", mock_file_open):
        grades = read_csv_files(["file1.csv", "file2.csv"])

        assert len(grades) == 2
        assert grades[0].student_name == "Иванов Иван"
        assert grades[1].student_name == "Петров Петр"


def test_file_not_found():
    """Тест обработки отсутствующего файла."""
    with pytest.raises(FileNotFoundError):
        read_csv_files(["nonexistent.csv"])


def test_invalid_csv_format():
    """Тест обработки некорректного CSV формата."""
    csv_content = """invalid,header,format
data1,data2,data3"""

    with patch("builtins.open", mock_open(read_data=csv_content)):
        with pytest.raises(ValueError, match="не содержит все необходимые колонки"):
            read_csv_files(["test.csv"])
