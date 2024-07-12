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
