from os import system
from time import sleep
from math import ceil
import character as c

MAX_PLAYER_HP = 5
MAX_LOG = 7
LOG_LIST = ["" for i in range(MAX_LOG)]
MAX_ROUND = 10
WAITING_TIME = 5
round = 1
bounty_stack = 0
player_hp = MAX_PLAYER_HP

def check_cheat_code(code):
    pass

# displayer
def screen(player_hp, enemy):
    global MAX_LOG, round, bounty_stack
    system("cls")
    player = c.player(player_hp)

    enemy_hp = "".join(["❤" for i in range(enemy.hp)])
    player_hp = "".join(["❤" for i in range(player_hp)])

    print(f"{' '*5}=Round{round:2}/{MAX_ROUND}{'='*26}   Log: {LOG_LIST[5]}")
    print(f"{' '*6}Bounty {bounty_stack:2}{' '*6}{enemy_hp:>14} {enemy.emoji}{' '*12}{LOG_LIST[4]}")
    print(f"{' '*17}{enemy.character:>20}{' '*13}{LOG_LIST[3]}")
    print(f"{' '*24}VS{' '*24}{LOG_LIST[2]}")
    print(f"{' '*10}{player}{player_hp:10}{' '*26}{LOG_LIST[1]}")
    print(f"{' '*10}Player{' '*6}{enemy.hidding_word:>15}{' '*9} -> {LOG_LIST[0]}")
    print(f"{' '*5}{'='*37}{' '*7}Letters: {enemy.shaffle_word}")
    # print(f"{' '*5}{'='*37}{' '*8}Letter: {enemy.word.upper()}")

# input controller and checker
def enter_input(enemy, LOG_LIST):
    global player_hp, bounty_stack
    input_word = input(f"{' '*7}Worattack: ").lower()
    # check_cheat_code(input_word)
    if not enemy.check_lenght(input_word): # input length not equal answer length
        LOG_LIST.insert(0, f'You guess "{input_word}", invalid answer length')
        return False
    letters, vaild_char = enemy.check_ch_amount(input_word) # have some letter than didn't given
    if not vaild_char:
        LOG_LIST.insert(0, f"You guess \"{input_word}\", invalid letter {' '.join([i.upper() for i in letters])}")
        return False
    take_damage = enemy.check_answer(input_word)
    if take_damage: LOG_LIST.insert(0, f'You guess "{input_word}" deal {take_damage} to {enemy.character}')
    else:
        bounty_stack -= ceil(round/2)
        player_hp -= 1
        LOG_LIST.insert(0, f'You guess "{input_word}" and take 1 damage from {enemy.character}')
    return True

def main():
    global MAX_PLAYER_HP, MAX_ROUND, WAITING_TIME, LOG_LIST, round, bounty_stack
    c.setup_player(MAX_PLAYER_HP)

    while round <= MAX_ROUND:
        enemy = c.random_enemy(bounty_stack)
        LOG_LIST.insert(0, f"Word have {enemy.hp} letters")
        while not (enemy.hp == 0 or player_hp == 0):
            screen(player_hp, enemy)
            if not enter_input(enemy, LOG_LIST):
                continue
            if enemy.hp == 0: # enemy dead
                LOG_LIST.insert(0, f'"{enemy.word.capitalize()}" meaning is {enemy.meaning}')
                LOG_LIST.insert(0, "")
                for i in range(WAITING_TIME, 0, -1):
                    LOG_LIST[0] = f"You beat {enemy.character}. Go to next round in {i} sec."
                    screen(player_hp, enemy)
                    sleep(1)
                LOG_LIST[0] = f"You beat {enemy.character}. Go to next round in 0 sec."
                bounty_stack += ceil(round/2)
                round += 1
            elif player_hp == 0: # player dead
                LOG_LIST.insert(0, f'You had beated by {enemy.character}. The word is "{enemy.word}"')
                LOG_LIST.insert(0, "You Dead. Game Over!")
                screen(player_hp, enemy)
                sleep(5)
                break
        if player_hp == 0: break
    if player_hp == 0:
        print("You lose")
    else:
        print("You win")

if __name__ == "__main__":
    main()