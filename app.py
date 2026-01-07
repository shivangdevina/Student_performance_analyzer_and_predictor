from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys


if __name__ == "__main__":
    logging.info("the execution has been started") # for testing of logger

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception") # for testing of logger
        raise CustomException(e,sys) # for testing of exception
        