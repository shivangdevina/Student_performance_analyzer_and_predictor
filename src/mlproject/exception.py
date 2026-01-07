import sys # Importing the sys module to handle system-specific parameters and functions
from src.mlproject.logger import logging # Importing the logging configuration from the local logger module

# Function to capture and format detailed error information
def error_message_detail(error,error_detail:sys):
    # exc_info returns (type, value, traceback). We only need the traceback (exc_tb)
    _,_,exc_tb=error_detail.exc_info()
    
    # Extracting the file name where the exception occurred from the traceback
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    # Formatting a custom error message with file name, line number, and error message
    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message # Returning the detailed error message

# Custom Exception class inheriting from the built-in Exception class
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        # Initializing the base Exception class with the error message
        super().__init__(error_message)
        
        # Generating a detailed error message using the helper function
        self.error_message=error_message_detail(error_message,error_details)
    
    def __str__(self):
        # Returning the detailed error message when the exception object is printed or converted to a string
        return self.error_message
