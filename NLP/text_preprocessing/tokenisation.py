import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import sys



from text_processing.entity.artifact_entity import ArtifactEntity
from text_processing.logging import logger
from text_processing.exceptions.exception import NLPException
from text_processing.utils.main_utils.utils import load_object, save_object
from text_processing.entity.config_entity import textpreprocessingconfig,Tokenisation_config

class TokenisationComponent:
    def __init__(self):
        try:
            self.tokenisation_config= Tokenisation_config()
        except Exception as e:
            raise NLPException(e, sys) from e
          
    def tokenise_sentences(self, text):
        sentences_token = sent_tokenize(text)
        return sentences_token
    
    def tokenise_words(self, text):
        words_token = word_tokenize(text)
        return words_token
        







    def initiate_tokenisation(self):
        #enter the try block
        logger.logging.info("Enter the try block")
        # take test from user as a input
        raw_text= input("Enter the text:")
        # save the text in the file
        save_object(self.tokenisation_config.file_path, raw_text)
        
        raw_text_path= self.tokenisation_config.file_path
        text = load_object(raw_text_path)
        sentences_token = self.tokenise_sentences(text)
        words_token = self.tokenise_words(text)
        tokeningestionartifact= ArtifactEntity(sentence_token=sentences_token, word_token=words_token)
        return tokeningestionartifact     