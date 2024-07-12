"""
Exception classes for the Titanic data processing project.
"""

class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class DataLoadError(CustomError):
    """Raised when there is an error loading data."""
    pass

class DataProcessingError(CustomError):
    """Raised when there is an error processing data."""
    pass
