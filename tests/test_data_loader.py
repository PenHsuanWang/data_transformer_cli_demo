"""
Tests for the data_loader module.
"""

import pytest
from src.data_loader import load_data
from src.exceptions import DataLoadError

def test_load_data():
    """Test loading data from a valid file path."""
    data = load_data("tests/data/titanic.csv")
    assert not data.empty

def test_load_data_invalid_file():
    """Test loading data from an invalid file path."""
    with pytest.raises(DataLoadError):
        load_data("invalid/path/to/titanic.csv")

def test_load_data_empty_file(tmp_path):
    """Test loading data from an empty file."""
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")
    with pytest.raises(DataLoadError):
        load_data(empty_file)

def test_load_data_malformed_file(tmp_path):
    """Test loading data from a malformed CSV file."""
    malformed_file = tmp_path / "malformed.csv"
    malformed_file.write_text("Name,Age,Sex\nAlice,30,Female\nBob,not_an_age,Male")
    with pytest.raises(DataLoadError):
        load_data(malformed_file)
