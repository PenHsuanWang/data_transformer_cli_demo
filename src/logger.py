"""
Logging configuration for the Titanic data processing project.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("titanic_project.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
