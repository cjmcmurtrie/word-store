## WordStore

Store interesting words from a table in Python.

### Setup

Run the following from command line in root:

```bash
$ pip install -r requirements.txt 
$ python setup.py
```

### Example

A single document:

```python
>>> from word_store.store import WordStore
>>> word_store = WordStore()
>>> word_store.add_document(
...         document_id='1234',
...         document_string='This is a document. Another document may follow, with more interesting words.'
...     )
>>> word_store.get_word('document')
{'count': 2, 'documents': ['1234'],
'sentences': ['This is a document.', 'Another document may follow, with more interesting words.']}
```

Batch update:
```python
>>> from word_store.store import WordStore, batch_update_word_store
>>> word_store = WordStore()
>>> word_store = batch_update_word_store(
...    word_store,
...    documents_path='tests/fictures/documents/'
...)
```

To run tests:
```bash
$ py.test -s tests/
```