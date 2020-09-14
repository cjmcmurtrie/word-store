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

To get a Pandas DataFrame:
```python
>>> word_store.to_pandas().head()
          word count documents                                          sentences
0     document     2    [1234]  [This is a document., Another document may fol...
1       follow     1    [1234]  [Another document may follow, with more intere...
2         more     1    [1234]  [Another document may follow, with more intere...
3  interesting     1    [1234]  [Another document may follow, with more intere...
4        words     1    [1234]  [Another document may follow, with more intere...
```


To run tests:
```bash
$ py.test -s tests/
```