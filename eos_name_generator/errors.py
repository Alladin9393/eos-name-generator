"""
Provide errors for BaseGenerator interface.
"""


class ValidationDataError(Exception):
    """
    Name generation data contains invalid characters or does not match the name length error.
    """

    def __init__(self, message):
        self.message = message
