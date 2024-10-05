import random
import os
import time
from CC import choose_character
from PO import print_options
from OF import option_func, option_effects

def main():
    print(f'''

░█▀▀█ █── █▀▀█ █─█ 
░█▀▀▄ █── █──█ ▄▀▄ 
░█▄▄█ ▀▀▀ ▀▀▀▀ ▀─▀ 

░█▀▀▀ ─▀─ █▀▀▀ █──█ ▀▀█▀▀ █▀▀ █▀▀█ ░█▀▀▀█ 
░█▀▀▀ ▀█▀ █─▀█ █▀▀█ ──█── █▀▀ █▄▄▀ ─▄▄▄▀▀ 
░█─── ▀▀▀ ▀▀▀▀ ▀──▀ ──▀── ▀▀▀ ▀─▀▀ ░█▄▄▄█''')
    mode = "none"
    print(f'''
Choose your play mode:
a) SINGLE-PLAYER
b) MULTI-PLAYER
''')
    mode_option = input("(a, b) >>> ")
    while mode_option.lower() != 'a' and mode_option.lower() != 'b':
        mode_option = input(">>> ")
    if mode_option == "a":
        mode = "single"
    else:
        mode = "pvp"
    print(f'''
Choose your character (P1):
a) Noob
b) Bacon
c) Pizza Man
d) Murderer
e) Criminal
f) Cop
g) Piggy
h) Boxer
i) Ninja
j) Baller
''')
    character_option = input(">>> ")
    while character_option.lower() != 'a' and character_option.lower() != 'b' and character_option.lower() != 'c' and character_option.lower() != 'd' and character_option.lower() != 'e' and character_option.lower() != 'f' and character_option.lower() != 'g' and character_option.lower() != 'h' and character_option.lower() != 'i' and character_option.lower() != 'j':
        character_option = input(">>> ")
    character = choose_character(character_option)
    if mode == "pvp":
        print(f'''
Choose your character (P2):
a) Noob
b) Bacon
c) Pizza Man
d) Murderer
e) Criminal
f) Cop
g) Piggy
h) Boxer
i) Ninja
j) Baller
''')
        opponent_option = input(">>> ")
        while opponent_option.lower() != 'a' and opponent_option.lower() != 'b' and opponent_option.lower() != 'c' and opponent_option.lower() != 'd' and opponent_option.lower() != 'e' and opponent_option.lower() != 'f' and opponent_option.lower() != 'g' and opponent_option.lower() != 'h' and opponent_option.lower() != 'i' and opponent_option.lower() != 'j':
            opponent_option = input(">>> ")
    else:
        opponent_option = random.randint(1,10)
    opponent = choose_character(opponent_option)
    if mode == "pvp":
        print(f'''
GAME SET!
    
P1 is {character}
P2 is {opponent}''')
    else:
        print(f'''
GAME SET!
    
P1 is {character}
COM is {opponent}''')
    start_game = input(f"Press [Enter] to start fight >> ")
    winner = "none"
    P1_HP = 200
    P2_HP = 200
    P1_SP = 100
    P2_SP = 100
    P1_hp_regen_count = 1
    P1_energy_regen_count = 1
    P1_attack_item_count = 2
    P2_hp_regen_count = 1
    P2_energy_regen_count = 1
    P2_attack_item_count = 2
    P1_blocking = False
    P2_blocking = False
    P1_dodging = False
    P2_dodging = False
    turn = "P1"
    damage = 0
    chance = 0
    while winner == "none":
        os.system("clear")
        if turn == "P1":
            if P1_HP > 0:
                print(f"|{character.upper()} VS {opponent.upper()}|")
                print(f'''
{character}'s HP: {P1_HP}
{opponent}'s HP: {P2_HP}

{character}'s SP: {P1_SP}
''')
                print(f"{turn}'S TURN!")
                print(f'''
(1) ATTACK | (2) DEFEND/REGEN | (3) ITEM | (4) GIVE UP
''')
                option = int(input("> "))
                while option != 1 and option != 2 and option != 3 and option != 4:
                    option = int(input("> "))
                if not(int(option) == 4):
                    output = print_options(option, character, P1_hp_regen_count, P1_energy_regen_count, P1_attack_item_count)
                    print(output)
                    option2 = int(input("> "))
                    if option == 1:
                        while option2 != 1 and option2 != 2 and option2 != 3:
                            option2 = int(input("> "))
                    elif option == 2:
                        while option2 != 1 and option2 != 2 and option2 != 3 and option2 != 4:
                            option2 = int(input("> "))
                    elif option == 3:
                        while option2 != 1 and option2 != 2 and option2 != 3:
                            option2 = int(input("> "))
                    os.system("clear")
                    option_func(character, option, option2, P1_energy_regen_count, P1_attack_item_count, P1_hp_regen_count, P1_SP)
                    time.sleep(1)
                    option_effects(option, option2, opponent, character, time, random, P1_SP, P2_blocking, P2_dodging, P1_HP, P2_HP, P1_energy_regen_count, P1_hp_regen_count, P1_attack_item_count)
                    time.sleep(4)
                    P2_blocking = False
                    P2_dodging = False
                    turn = "P2"
                else:
                    print(f"{character} gave up!")
                    winner = opponent
            else:
                print(f"{character} fainted!")
                winner = opponent
        elif turn == "P2":
            if P2_HP > 0:
                if mode == "single":
                    opponent_option1 = random.randint(1,3)
                    opponent_option2 = random.randint(1,3)
                    option_func(opponent, opponent_option1, opponent_option2, P2_energy_regen_count, P2_attack_item_count, P2_hp_regen_count, P2_SP)
                    time.sleep(1)
                    option_effects(opponent_option1, opponent_option2, character, opponent, time, random, P2_SP, P1_blocking, P1_dodging, P2_HP, P1_HP, P2_energy_regen_count, P2_hp_regen_count, P2_attack_item_count)
                    time.sleep(4)
                    P1_blocking = False
                    P1_dodging = False
                    turn = "P1"
                else:
                    print(f"|{character.upper()} VS {opponent.upper()}|")
                    print(f'''
{opponent}'s HP: {P2_HP}
{character}'s HP: {P1_HP}

{opponent}'s SP: {P2_SP}
''')
                    print(f"{turn}'S TURN!")
                    print(f'''
(1) ATTACK | (2) DEFEND/REGEN | (3) ITEM | (4) GIVE UP
''')
                    opponent_option1 = int(input("> "))
                    while opponent_option1 != 1 and opponent_option1 != 2 and opponent_option1 != 3 and opponent_option1 != 4:
                        opponent_option1 = int(input("> "))
                    if not(int(opponent_option1) == 4):
                        output = print_options(opponent_option1, opponent, P2_hp_regen_count, P2_energy_regen_count, P2_attack_item_count)
                        print(output)
                        opponent_option2 = int(input("> "))
                        if opponent_option1 == 1:
                            while opponent_option2 != 1 and opponent_option2 != 2 and opponent_option2 != 3:
                                opponent_option2 = int(input("> "))
                        elif opponent_option1 == 2:
                            while opponent_option2 != 1 and opponent_option2 != 2 and opponent_option2 != 3 and opponent_option2 != 4:
                                opponent_option2 = int(input("> "))
                        elif opponent_option1 == 3:
                            while opponent_option2 != 1 and opponent_option2 != 2 and opponent_option2 != 3:
                                opponent_option2 = int(input("> "))
                        os.system("clear")
                        option_func(opponent, opponent_option1, opponent_option2, P2_energy_regen_count, P2_attack_item_count, P2_hp_regen_count, P2_SP)
                        time.sleep(1)
                        option_effects(opponent_option1, opponent_option2, character, opponent, time, random, P2_SP, P1_blocking, P1_dodging, P2_HP, P1_HP, P2_energy_regen_count, P2_hp_regen_count, P2_attack_item_count)
                        time.sleep(4)
                        P1_blocking = False
                        P1_dodging = False
                        turn = "P1"
                    else:
                        print(f"{character} has gave up the fight.")
                        winner = opponent
            else:
                print(f"{opponent} fainted!")
                winner = character
        
    print(f"{winner} wins!")
    
main()
