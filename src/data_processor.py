"""
Module for processing Titanic data.
"""

import pandas as pd
from .exceptions import DataProcessingError, InvalidDataError
from .logger import logger

def validate_data(data: pd.DataFrame) -> None:
    """Validates the Titanic data.

    :param data: A pandas DataFrame containing the Titanic data.
    :type data: pd.DataFrame
    :raises InvalidDataError: If the data is invalid.
    """
    logger.debug("Validating data")
    required_columns = {'Age', 'Embarked', 'Sex'}
    if not required_columns.issubset(data.columns):
        logger.error("Data validation failed: Missing required columns")
        raise InvalidDataError("Data validation failed: Missing required columns")
    logger.info("Data validation passed")

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Processes the Titanic data.

    Fills missing values and encodes categorical features.

    :param data: A pandas DataFrame containing the Titanic data.
    :type data: pd.DataFrame
    :raises DataProcessingError: If there is an error processing the data.
    :raises InvalidDataError: If the data is invalid.
    :return: A pandas DataFrame with the processed data.
    :rtype: pd.DataFrame
    """
    try:
        logger.debug("Starting data processing")
        validate_data(data)
        data['Age'].fillna(data['Age'].median(), inplace=True)
        data['Embarked'].fillna('S', inplace=True)
        data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)
        logger.info("Data processed successfully")
        return data
    except InvalidDataError as ide:
        logger.warning(f"Invalid data error: {ide}")
        raise
    except Exception as e:
        logger.critical(f"Critical error processing data: {e}")
        raise DataProcessingError(f"Critical error processing data: {e}") from e
