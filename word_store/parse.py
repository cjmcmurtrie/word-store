from nltk import word_tokenize, pos_tag


INTERESTING_POS_TAGS = {
    'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'JJ',
    'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'FW'
}


def get_sentence_words(sentence):
    '''
    Get interesting words in sentence by part of speech tags.
    Interesting words here are defined as any of:
        - verbs
        - nouns
        - adjectives
        - adverbs
        - foreign words
    :param sentence: str
    :return: list(str)
    '''
    tokens = word_tokenize(sentence)
    tagged_words = pos_tag(tokens)
    interesting_words = [
        word for (word, tag) in tagged_words
        if tag in INTERESTING_POS_TAGS
    ]
    return interesting_words
