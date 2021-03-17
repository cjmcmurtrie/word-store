## WordStore

Store interesting words to a table in Python.

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
```
```text
       word count                                          documents                                          sentences
0      good    13  [tests/fixtures/documents/doc6.txt, tests/fixt...  [ Good morning., Fortunately, however, we've m...
1   morning     2                [tests/fixtures/documents/doc6.txt]  [ Good morning., Outstanding career officials ...
2   senator    12  [tests/fixtures/documents/doc6.txt, tests/fixt...  [As some of you know, Senator Lugar and I rece...
3     lugar     5  [tests/fixtures/documents/doc6.txt, tests/fixt...  [As some of you know, Senator Lugar and I rece...
4  recently     2  [tests/fixtures/documents/doc6.txt, tests/fixt...  [As some of you know, Senator Lugar and I rece...
```

To save to file:
```python
>>> word_store.save('word_store.json')
```

Then a previous instance can be loaded.
```python
>>> word_store = WordStore('word_store.json')
```

To run tests:
```bash
$ py.test -s tests/
```
