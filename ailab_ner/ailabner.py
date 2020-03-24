from lenerbr.ner_model import NERModel
from lenerbr.config import Config
import pandas as pd
from nltk import word_tokenize
from nltk import data
from nltk.tokenize.punkt import PunktSentenceTokenizer
import sys

def entity_treatment(input_document: str) -> str:
    ''' Receives an input string document with and
        returns a string with the choosen entity types
        replaced by tokens or deleted from the original text.
    '''
    tokenizer.train(input_document)
    doc_sentences = tokenizer.tokenize(input_document)
    replaced_sentences = []
    for sentence in doc_sentences:
        token_sentence = word_tokenize(sentence, language='portuguese')
        preds = model.predict(token_sentence)
        for index, word in enumerate(token_sentence):
            ''' Removendo sufixo de tipo de entidades'''
            if preds[index][0:2] in ['B-', 'I-', 'E-', 'S-']:
                preds[index] = preds[index][2:]
            if preds[index] == 'PESSOA':
                replaced_sentences.append('PESSOA_IDENTIFICADA')
            elif preds[index] == 'LOCAl':
                replaced_sentences.append('LOCALIDADE_IDENTIFICADA')
            else:
                replaced_sentences.append(word)
    replaced_doc = " ".join(replaced_sentences)
    return replaced_doc


# create instance of config
config = Config()

# build model

model = NERModel(config)
model.build()
model.restore_session(config.dir_model)
tokenizer = PunktSentenceTokenizer()
