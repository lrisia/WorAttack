import random as rd
from word_handle import load_words

CHARACTERS = {"Cool guy": "😎", "Angry boy": "🤬", "Cowboy": "🤠", "The Clown": "🤡", "Nerd guy": "🤓",
              "Happy demon": "😈", "Angry demon": "👿", "Oni": "👹", "Goblin": "👺", "Ghost": "👻",
              "Alien": "👽", "Alien Monster": "👾", "Robot The Destroyer": "🤖", "Tiger": "🐅",
              "Google Trex": "🦖", "Dragon in my Jeans": "🐉", "My Anaconda": "🐍", "Octopus The artist": "🐙",
              "Doppelganger": "👥", "The King": "🤴", "Angel": "👼", "Santa Claus": "🎅", "Superman": "🦸",
              "Magicial": "🦹", "Gran Draft The Grey": "🧙", "Poseidon": "🧜", "Sleeper": "🛌"
             }
WORDS = load_words()
MAX_HP = 0

def setup_player(max_hp=3):
    global MAX_HP
    MAX_HP = max_hp

def player(hp):
    low = int(MAX_HP/3)
    middle = low*2
    if hp > middle and hp <= MAX_HP: return "😀🔪"
    elif hp > low and hp <= middle: return "😐🔪"
    elif hp > 0 and hp <= low: return "🙁🔪"
    return "💀🔪"

def random_enemy(bounty=0):
    character = rd.choice(list(CHARACTERS.items()))[0]
    word = random_word(bounty)
    return Enemy(character, word)

def random_word(bounty):
    if bounty <= 2: length_range = (3, 4)
    elif bounty <= 3: length_range = (4, 5)
    elif bounty <= 5: length_range = (5, 7)
    elif bounty <= 8: length_range = (7, 9)
    else: length_range = (10, 20)
    word = ""
    while not (len(word) >= length_range[0] and len(word) <= length_range[1]):
        word = rd.choice(WORDS)
        # if not have_meaning:
        #     continue
    return word

class Enemy:
    def __init__(self, character, word) -> None:
        self.character = character
        self.emoji = CHARACTERS[character]
        self.word = word.lower()
        self.hp = len(word)
        self.hidding_word = "".join(["_" for i in range(len(word))])
        self.shaffle_word = " ".join([i.upper() for i in self.shuffling_letter()])
        self.word_dict = self.word_to_dict(word)

    def word_to_dict(self, word):
        word_dict = dict()
        for ch in word: word_dict[ch] = word.count(ch)
        return word_dict

    def check_ch_amount(self, word):
        have_letter = []
        for ch in self.word_dict:
            if word.count(ch) == self.word_dict[ch]: have_letter.append(ch)
        miss_letter = [i for i in word if i not in self.word_dict]
        match = not len(miss_letter)
        return miss_letter, match

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.emoji = "💀"

    def check_lenght(self, answer):
        if len(answer) == len(self.word): return True
        return False

    def check_answer(self, answer):
        correct = 0
        hidding = list(self.hidding_word)
        for i in range(len(answer)):
            if answer[i] == self.word[i] and hidding[i] == '_':
                hidding[i] = answer[i].upper()
                correct += 1
        self.hidding_word = "".join(hidding)
        self.take_damage(correct)
        return correct
    
    def shuffling_letter(self):
        temp = list(self.word)
        rd.shuffle(temp)
        return temp

setup_player()

# r = random_enemy(10)
# print(r.character)
# print(r.emoji)
# print(r.word)
# print(r.hp)