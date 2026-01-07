import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #gives name to the files
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #name and the path of the "log" folder

os.makedirs(log_path,exist_ok=True) #creating the "log" folder as it doesn't exist
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE) #defining the path of the file(not folder)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
