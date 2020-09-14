import os
import json
import pandas as pd
from nltk import sent_tokenize
from word_store.parse import get_sentence_words


def doc_stream(documents_path):
    doc_paths = [
        os.path.join(documents_path, f) for f in os.listdir(documents_path)
        if os.path.isfile(os.path.join(documents_path, f))
    ]
    for doc_path in doc_paths:
        yield doc_path, open(doc_path, 'r').read()


def batch_update_word_store(store, documents_path):
    for doc_id, doc_string in doc_stream(documents_path):
        store.add_document(doc_id, doc_string)
    return store


class WordStore(object):
    '''
    Class to parse documents and store their counts, occurring documents and sentences.
    Example code:

    >>> from word_store.store import WordStore
    >>> word_store = WordStore()
    >>> word_store.add_document(
    ...         document_id='1234',
    ...         document_string='This is a document. Another document may follow, with more interesting words.'
    ...     )
    >>> word_store.get_word('document')
    {'count': 2, 'documents': ['1234'],
    'sentences': ['This is a document.', 'Another document may follow, with more interesting words.']}

    '''
    def __init__(self, source_path=None):
        self.data = {'ALL_DOCUMENTS': []}
        if source_path is None:
            pass
        else:
            self._load_from_file(source_path)

    def _load_from_file(self, source_path):
        try:
            with open(source_path, 'r') as source:
                self.data = json.loads(source.read())
            source.close()
        except FileNotFoundError:
            print('JSON store {source_path} does not exist, empty store loaded'.format(
                source_path=source_path
            ))

    def get_word(self, word):
        return self.data.get(word.lower(), None)

    def get_documents(self):
        return self.data['ALL_DOCUMENTS']

    def add_document(self, document_id, document_string):
        if document_id not in self.data['ALL_DOCUMENTS']:
            self.data['ALL_DOCUMENTS'].append(document_id)
            for sentence in sent_tokenize(document_string):
                interesting_words = get_sentence_words(sentence)
                for word in interesting_words:
                    self.update_word(word, sentence, document_id)

    def update_word(self, word, sentence, document):
        word = word.lower()
        if not self.data.get(word):
            self._init_word(word)
        if document not in self.data[word]['documents']:
            self.data[word]['documents'].append(document)
        self.data[word]['count'] += 1
        self.data[word]['sentences'].append(sentence)

    def _init_word(self, word):
        self.data[word] = {'count': 0, 'documents': [], 'sentences': []}

    def save(self, filepath):
        open(filepath, 'w').write(json.dumps(self.data))

    def to_pandas(self):
        copy = self.data.copy()
        copy.pop('ALL_DOCUMENTS')
        table = pd.DataFrame(copy).T.reset_index()
        return table.rename({'index': 'word'}, axis=1)
