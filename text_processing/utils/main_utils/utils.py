
import os
import sys
from text_processing.exceptions.exception import NLPException
from text_processing.logging.logger import logging


def load_object(file_path: str, ) -> str:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rt",) as file_obj:
            print(file_obj)
            return file_obj.read()
          
    except Exception as e:
        raise NLPException(e, sys) from e
    
def save_object(file_path: str, obj) -> None:
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file_obj:
            file_obj.write(obj)
        logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        raise NLPException(e, sys) from e
