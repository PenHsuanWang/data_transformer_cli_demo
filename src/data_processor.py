"""
Module for processing Titanic data.
"""

import pandas as pd
from src.exceptions import DataProcessingError
from src.logger import logger

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Processes the Titanic data.

    Fills missing values and encodes categorical features.

    :param data: A pandas DataFrame containing the Titanic data.
    :type data: pd.DataFrame
    :raises DataProcessingError: If there is an error processing the data.
    :return: A pandas DataFrame with the processed data.
    :rtype: pd.DataFrame
    """
    try:
        data['Age'].fillna(data['Age'].median(), inplace=True)
        data['Embarked'].fillna('S', inplace=True)
        data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)
        return data
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        raise DataProcessingError(f"Error processing data: {e}")
