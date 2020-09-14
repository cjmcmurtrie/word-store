import pandas as pd
from word_store.store import WordStore, batch_update_word_store


def test_create_store():
    word_store = WordStore()
    assert isinstance(word_store, WordStore)


def test_create_store_no_file():
    word_store = WordStore('file_doesnt_exist.json')
    assert isinstance(word_store, WordStore)


def test_batch_update():
    word_store = WordStore()
    word_store = batch_update_word_store(word_store, documents_path='tests/fixtures/documents/')
    assert len(word_store.data.keys()) > 1


def test_load_store():
    word_store = WordStore('tests/fixtures/test.json')
    assert len(word_store.data.keys()) > 1


def test_get_word():
    word_store = WordStore('tests/fixtures/test.json')
    word_data = word_store.get_word('philosophy')
    assert all(
        key in word_data.keys() for key in ('count', 'documents', 'sentences')
    )


def test_to_pandas():
    word_store = WordStore('tests/fixtures/test.json')
    dataframe = word_store.to_pandas()
    assert isinstance(dataframe, pd.DataFrame)


def test_add_document():
    word_store = WordStore()
    word_store.add_document(
        document_id='1234',
        document_string='This is a document. Another document may follow, with more interesting words.'
    )
    assert word_store.get_word('document')['count'] == 2
