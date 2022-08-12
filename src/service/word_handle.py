# read words_alpha.txt and return words
def load_words():
    dictionary = dict()
    with open('src/data/words_alpha.txt') as word_file:
        data = set(word_file.read().split())
        word_file.close()
    for word in data:
        dictionary[word] = ""
    return dictionary