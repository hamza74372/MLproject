import sys
from src.logger import logger

def error_message_detail(error, error_detail: tuple):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: [{file_name}] at line number: [{exc_tb.tb_lineno}] error message: [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: tuple):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        # Log the exception
        logger.error(self.error_message, exc_info=True)

    def __str__(self):
        return self.error_message

# Test divide by zero
try:
    1 / 0
except Exception:
    raise CustomException("Divide by zero occurred", sys.exc_info())
