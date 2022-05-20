# read words_alpha.txt and return list of words
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return list(valid_words)