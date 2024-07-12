"""
Tests for the data_processor module.
"""

import pandas as pd
import pytest
from src.data_processor import process_data, validate_data
from src.exceptions import DataProcessingError, InvalidDataError

def test_process_data():
    """Test processing valid data."""
    raw_data = pd.DataFrame({
        'Age': [22, 38, 26, 35, None],
        'Embarked': ['S', 'C', 'S', 'S', None],
        'Sex': ['male', 'female', 'female', 'female', 'male'],
        'Survived': [0, 1, 1, 1, 0]
    })
    processed_data = process_data(raw_data)
    assert 'Age' in processed_data.columns
    assert 'Embarked_S' in processed_data.columns
    assert 'Sex_male' in processed_data.columns

def test_process_data_invalid():
    """Test processing invalid data."""
    with pytest.raises(InvalidDataError):
        validate_data(pd.DataFrame())

    with pytest.raises(DataProcessingError):
        process_data(pd.DataFrame())

def test_process_data_missing_columns():
    """Test processing data with missing required columns."""
    incomplete_data = pd.DataFrame({
        'Age': [22, 38, 26, 35],
        'Embarked': ['S', 'C', 'S', 'S']
    })
    with pytest.raises(InvalidDataError):
        validate_data(incomplete_data)

def test_process_data_invalid_age():
    """Test processing data with invalid Age values."""
    invalid_age_data = pd.DataFrame({
        'Age': [22, 'unknown', 26, 35],
        'Embarked': ['S', 'C', 'S', 'S'],
        'Sex': ['male', 'female', 'female', 'female'],
        'Survived': [0, 1, 1, 1]
    })
    with pytest.raises(DataProcessingError):
        process_data(invalid_age_data)
