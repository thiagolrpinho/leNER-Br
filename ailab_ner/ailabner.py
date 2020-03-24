from lenerbr.ner_model import NERModel
from lenerbr.config import Config
from nltk import word_tokenize
from nltk import data
from nltk.tokenize.punkt import PunktSentenceTokenizer
from typing import Set
import pandas as pd
import sys


def entity_treatment(
        input_document: str,
        choosen_entities_types: Set[str] = set(["PESSOA", "LOCAL"]),
        remove_entities: bool = False) -> str:
    ''' Receives an input string document with and
        returns a string with the choosen entity types
        replaced by tokens or deleted from the original text.
        The available entity types to choose are:
        PESSOA - For person names.
        TEMPO - for time related terms.
        LOCAL - For locations like countries, cities or states.
        ORGANIZACAO - For enterprise names.
        JURISPRUDENCIA - For jurisprudence related terms.
        LEGISLACAO - For law related terms.
    '''
    tokenizer.train(input_document)
    doc_sentences = tokenizer.tokenize(input_document)
    replaced_sentences = []
    for sentence in doc_sentences:
        token_sentence = word_tokenize(sentence, language='portuguese')
        preds = model.predict(token_sentence)
        for index, word in enumerate(token_sentence):
            ''' Removing entity types sufixes'''
            if preds[index][0:2] in ['B-', 'I-', 'E-', 'S-']:
                preds[index] = preds[index][2:]
            if preds[index] in choosen_entities_types:
                if not remove_entities:
                    replaced_sentences.append("TOKEN_" + str(preds[index]))
            else:
                replaced_sentences.append(word)
    replaced_doc = " ".join(replaced_sentences)
    return replaced_doc


''' Initializing model as one static variable. '''
config = Config()
model = NERModel(config)
model.build()
model.restore_session(config.dir_model)

''' Initializing tokenizer '''
tokenizer = PunktSentenceTokenizer()
