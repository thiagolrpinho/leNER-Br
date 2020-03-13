# leNER-Br: a Dataset for Named Entity Recognition in Brazilian Legal Text

This page holds the named entity recognition for Brazilian legal documents proposed in the paper "leNER-Br: a Dataset for Named Entity Recognition in Brazilian Legal Text". We also provide the code used for the training and evaluation of the LSTM-CRF model described in the paper, which achieved an average f1-score of 92.53% on the test set. The following sections describe the requirements and the dataset and model files.

## Requirements
1. [Python 3](https://www.python.org/downloads/)	
3. [pip](https://pip.pypa.io/en/stable/installing/)

## leNER-Br Dataset

The directory structure is as follows:
* the train, test and dev folders hold space separated text files where the first column are the words and the second column are the correspondent named entity tags. Sentences are separeted by empty lines. In addition, each folder has a file that is the concatenation of all the other conll files of the same folder (train.conll, dev.conll and test.conll).
* metadata holds json files with additional information from each annotated document.
* raw_text holds the source txt files that originated the conll files.
* scripts hold an abbreviation list used for sentence segmentation and the script that generated the conll files. To use the script:
```
python textToConll.py path/to/txtfile
```


## Model

The model code is adapted from [this repo](https://github.com/guillaumegenthial/sequence_tagging) and implements a NER model using Tensorflow (LSTM + CRF + chars embeddings). All code files modified are marked as such at the beginning.
The section below summarizes the use of the model. For more in depth explanations of how to use the model and change its configurations refer to the README of the original implementation.

###Evaluation

* To install the required python packages, run from the model folder:
```
pip install -r requirements.txt
```

* To obtain the f1 scores for each class on each part of the dataset:
```
python classScores.py train
python classScores.py dev
python classScores.py test
```
* To tag a raw text file:
```
python evaluateText path/to/txtfile
```

* To tag sentences in a interactive way:
```
python evaluate.py
```
or
```
python evaluateSentence.py
```

* To retrain the model from scratch:
```
python train.py
```