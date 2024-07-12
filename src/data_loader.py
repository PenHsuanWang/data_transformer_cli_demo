"""
Module for loading Titanic data from a CSV file.
"""

import pandas as pd
from src.exceptions import DataLoadError
from src.logger import logger

def load_data(file_path: str) -> pd.DataFrame:
    """Loads data from a CSV file.

    :param file_path: The path to the CSV file.
    :type file_path: str
    :raises DataLoadError: If there is an error loading the data.
    :return: A pandas DataFrame containing the loaded data.
    :rtype: pd.DataFrame
    """
    try:
        data = pd.read_csv(file_path)
        if data.empty:
            raise DataLoadError(f"No data found in file {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise DataLoadError(f"Error loading data: {e}")
