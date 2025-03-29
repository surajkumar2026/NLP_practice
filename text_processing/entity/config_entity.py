from datetime import datetime
import os
import sys
from text_processing.exceptions.exception import NLPException
from text_processing.logging.logger import logging
from text_processing.utils.main_utils.utils import save_object
from text_processing.entity.artifact_entity import ArtifactEntity

from text_processing.constant import text_preprocessing_pipeline

class textpreprocessingconfig:
    def __init__(self, timestamp=datetime.now()):
         timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
         self.artifact_name=text_preprocessing_pipeline.ARTIFACT_NAME   
       
         self.artifact_dir= os.path.join(self.artifact_name,timestamp)
         
class Tokenisation_config:
     def __init__(self):
            processing_config= textpreprocessingconfig()
            self.file_path= os.path.join(processing_config.artifact_dir,text_preprocessing_pipeline.FILE_NAME)

class Stemming_config:
     def __init__(self):
            processing_config= textpreprocessingconfig()
            self.file_path= os.path.join(processing_config.artifact_dir,text_preprocessing_pipeline.FILE_NAME)
     
