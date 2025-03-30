import nltk
import sys

from nltk.stem import PorterStemmer
from nltk.stem import snowball

from text_processing.entity.artifact_entity import ArtifactEntity,StemmingArtifactEntity
from text_processing.logging import logger
from text_processing.exceptions.exception import NLPException
from text_processing.utils.main_utils.utils import load_object, save_object
from text_processing.entity.config_entity import (textpreprocessingconfig,Tokenisation_config,Stemming_config)

class StemmingComponent:
    def __init__(self,tokenisation_artifact: ArtifactEntity):
        try:
            self.stemming_config= Stemming_config()
            self.tokenisation_artifact= tokenisation_artifact
       
        except Exception as e:
            raise NLPException(e, sys) from e
        
 
        

    def stemming_porter(self, words):
        ps = PorterStemmer()
        stemmed_words = [ps.stem(word) for word in words]
        return stemmed_words

    def initiate_stemming(self):
        logger.logging.info("Enter the try block")
        raw_text_path= self.stemming_config.file_path
        text = load_object(raw_text_path)
        words_token= []
        words_token = self.tokenisation_artifact.word_token
        stemmed_words = self.stemming_porter(words_token)
        stemmingartifact= StemmingArtifactEntity(stemmed_words=stemmed_words)
        return stemmingartifact