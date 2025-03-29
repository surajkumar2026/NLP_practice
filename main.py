from text_processing.components.tokenisation import TokenisationComponent
from text_processing.components.stemming import StemmingComponent
from text_processing.logging import logger
from text_processing.exceptions.exception import NLPException
from text_processing.utils.main_utils.utils import save_object
from text_processing.entity.artifact_entity import ArtifactEntity
from text_processing.entity.config_entity import textpreprocessingconfig,Tokenisation_config
from datetime import datetime


import sys
import os


if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        tokenisation= TokenisationComponent()
        tokeningestionartifact= tokenisation.initiate_tokenisation()
        print(tokeningestionartifact)

        stemming= StemmingComponent(tokeningestionartifact)
        stemmingartifact= stemming.initiate_stemming()
        print(stemmingartifact)
    except Exception as e:
        raise NLPException(e,sys) from e