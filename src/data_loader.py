"""
Module for loading Titanic data from a CSV file.
"""

import pandas as pd
from .exceptions import DataLoadError
from .logger import logger

def load_data(file_path: str) -> pd.DataFrame:
    """Loads data from a CSV file.

    :param file_path: The path to the CSV file.
    :type file_path: str
    :raises DataLoadError: If there is an error loading the data.
    :return: A pandas DataFrame containing the loaded data.
    :rtype: pd.DataFrame
    """
    try:
        logger.debug(f"Attempting to load data from {file_path}")
        data = pd.read_csv(file_path)
        if data.empty:
            logger.warning(f"No data found in file {file_path}")
            raise DataLoadError(f"No data found in file {file_path}")
        logger.info(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError as fnf_error:
        logger.error(f"File not found: {file_path} - {fnf_error}")
        raise DataLoadError(f"File not found: {file_path}") from fnf_error
    except pd.errors.ParserError as pe_error:
        logger.error(f"Error parsing file: {file_path} - {pe_error}")
        raise DataLoadError(f"Error parsing file: {file_path}") from pe_error
    except Exception as e:
        logger.critical(f"Critical error loading data: {e}")
        raise DataLoadError(f"Critical error loading data: {e}") from e
