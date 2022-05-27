# read words_nltk.txt and return words with meaning
def load_words():
    dictionary = dict()
    with open('data/words_nltk.txt') as word_file:
        data = word_file.read().split('\n')[:-1]
        word_file.close()
    for line in list(set(data)):
        word, meaning = line.split('||')
        dictionary[word] = meaning
    return dictionary