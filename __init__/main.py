import random
import os
import time
from CC import choose_character
from PO import print_options
from OF import option_func

def option_effects(option, option2, opponent, character, time, random, SP, opponent_blocking, opponent_dodging, player_hp, opponent_hp, player_energy_regen_count, player_hp_regen_count, player_attack_item_count):
    if option == 1:
        if option2 == 1:
            if SP >= 10:
                if opponent_blocking == True:
                    SP = SP - 10
                    if SP < 0:
                        SP = 0
                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                    time.sleep(0.5)
                    damage = random.randint(10,30)
                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - (damage - random.randint(10,30))
                    if opponent_hp < 0:
                        opponent_hp = 0
                    opponent_blocking = False
                elif opponent_dodging == True:
                    SP = SP - 10
                    if SP < 0:
                        SP = 0
                    chance = random.randint(0,1)
                    if chance == 0:
                        print(f'''
Surprisingly, {opponent} succesfully dodged {character}'s attack!''')
                    else:
                        print(f'''
{opponent} failed to dodge {character}'s attack!''')
                        damage = random.randint(10,30)
                        print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                        opponent_hp = opponent_hp - damage
                        if opponent_hp < 0:
                            opponent_hp = 0
                    time.sleep(0.5)
                    opponent_dodging = False
                else:
                    SP = SP - 10
                    if SP < 0:
                        SP = 0
                    damage = random.randint(10,30)
                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - damage
                    if opponent_hp < 0:
                        opponent_hp = 0
            else:
                if opponent_blocking == True:
                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                    time.sleep(0.5)
                    damage = random.randint(10,30)
                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - (damage - random.randint(10,30))
                    if opponent_hp < 0:
                        opponent_hp = 0
                    opponent_blocking = False
                elif opponent_dodging == True:
                    chance = random.randint(0,1)
                    if chance == 0:
                        print(f'''
Surprisingly, {opponent} succesfully dodged {character}'s attack!''')
                    else:
                        print(f'''
{opponent} failed to dodge {character}'s attack!''')
                        damage = random.randint(10,30)
                        print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                        opponent_hp = opponent_hp - damage
                        if opponent_hp < 0:
                            opponent_hp = 0
                    time.sleep(0.5)
                    opponent_dodging = False
                else:
                    damage = random.randint(10,30)
                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - damage
                    if opponent_hp < 0:
                        opponent_hp = 0
                    time.sleep(0.5)
                hp_loss = random.randint(10,50)
                print(f'''
{character} lost {hp_loss} HP after risking the move from being tired.''')
                player_hp = player_hp - hp_loss
                if opponent_hp < 0:
                    opponent_hp = 0
        elif option2 == 2:
            if SP >= 20:
                if opponent_blocking == True:
                    SP = SP - 20
                    if SP < 0:
                        SP = 0
                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                    time.sleep(0.5)
                    damage = random.randint(40,60)
                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - (damage + random.randint(40,60))
                    if opponent_hp < 0:
                        opponent_hp = 0
                    opponent_blocking = False
                elif opponent_dodging == True:
                    SP = SP - 20
                    if SP < 0:
                        SP = 0
                    chance = random.randint(0,1)
                    if chance == 0:
                        print(f'''
Surprisingly, {opponent} succesfully dodged {character}'s attack!''')
                    else:
                        print(f'''
{opponent} failed to dodge {character}'s attack!''')
                        damage = random.randint(10,30)
                        print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                        opponent_hp = opponent_hp - damage
                        if opponent_hp < 0:
                            opponent_hp = 0
                    time.sleep(0.5)
                    opponent_dodging = False
                else:
                    SP = SP - 20
                    if SP < 0:
                        SP = 0
                    damage = random.randint(40,60)
                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - damage
                    if opponent_hp < 0:
                        opponent_hp = 0
            else:
                if opponent_blocking == True:
                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                    time.sleep(0.5)
                    damage = random.randint(40,60)
                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - (damage + random.randint(40,60))
                    if opponent_hp < 0:
                        opponent_hp = 0
                    opponent_blocking = False
                elif opponent_dodging == True:
                    chance = random.randint(0,1)
                    if chance == 0:
                        print(f'''
Surprisingly, {opponent} succesfully dodged {character}'s attack!''')
                    else:
                        print(f'''
{opponent} failed to dodge {character}'s attack!''')
                        damage = random.randint(10,30)
                        print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                        opponent_hp = opponent_hp - damage
                        if opponent_hp < 0:
                            opponent_hp = 0
                    time.sleep(0.5)
                    opponent_dodging = False
                else:
                    damage = random.randint(40,60)
                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - damage
                    if opponent_hp < 0:
                        opponent_hp = 0
                    time.sleep(0.5)
                hp_loss = random.randint(50,70)
                print(f'''
{character} lost {hp_loss} HP after risking the move from being tired.''')
                player_hp = player_hp - hp_loss
                if opponent_hp < 0:
                    opponent_hp = 0
        elif option2 == 3:
            if SP >= 50:
                if opponent_blocking == True:
                    SP = SP - 50
                    if SP < 0:
                        SP = 0
                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                    time.sleep(0.5)
                    damage = random.randint(70,100)
                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - (damage + random.randint(70,100))
                    if opponent_hp < 0:
                        opponent_hp = 0
                    opponent_blocking = False
                elif opponent_dodging == True:
                    SP = SP - 50
                    if SP < 0:
                        SP = 0
                    chance = random.randint(0,1)
                    if chance == 0:
                        print(f'''
Surprisingly, {opponent} succesfully dodged {character}'s attack!''')
                    else:
                        print(f'''
{opponent} failed to dodge {character}'s attack!''')
                        damage = random.randint(10,30)
                        print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                        opponent_hp = opponent_hp - damage
                        if opponent_hp < 0:
                            opponent_hp = 0
                    time.sleep(0.5)
                    opponent_dodging = False
                else:
                    SP = SP - 50
                    if SP < 0:
                        SP = 0
                    damage = random.randint(70,100)
                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - damage
                    if opponent_hp < 0:
                        opponent_hp = 0
            else:
                if opponent_blocking == True:
                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                    time.sleep(0.5)
                    damage = random.randint(70,100)
                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - (damage + random.randint(70,100))
                    opponent_blocking = False
                elif opponent_dodging == True:
                    chance = random.randint(0,1)
                    if chance == 0:
                        print(f'''
Surprisingly, {opponent} succesfully dodged {character}'s attack!''')
                    else:
                        print(f'''
{opponent} failed to dodge {character}'s attack!''')
                        damage = random.randint(10,30)
                        print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                        opponent_hp = opponent_hp - damage
                        if opponent_hp < 0:
                            opponent_hp = 0
                    time.sleep(0.5)
                    opponent_dodging = False
                else:
                    damage = random.randint(70,100)
                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - damage
                    if opponent_hp < 0:
                        opponent_hp = 0
                    time.sleep(0.5)
                hp_loss = random.randint(70,100)
                print(f'''
{character} lost {hp_loss} HP after risking the move from being tired.''')
                player_hp = player_hp - hp_loss
    elif option == 2:
        if option2 == 1:
            if SP >= 10:
                SP = SP - 10
                if SP < 0:
                    SP = 0
                P1_blocking = True
            print(f'''
Waiting for opponent's turn...''')
        elif option2 == 2:
            if SP >= 20:
                SP = SP - 20
                if SP < 0:
                    SP = 0
                P1_dodging = True
            print(f'''
Waiting for opponent's turn...''')
        elif option2 == 3:
            restore = random.randint(10,50)
            SP = SP + int(restore)
            if SP > 100:
                SP = 100
            print(f'''
SP has been restored to {SP}!''')
    elif option == 3:
        if option2 == 1:
            if player_hp_regen_count > 0:
                player_hp_regen_count = player_hp_regen_count - 1
                if player_hp_regen_count < 0:
                    player_hp_regen_count = 0
                hp_restore = random.randint(30,100)
                player_hp = player_hp + int(hp_restore)
                if player_hp > 200:
                    player_hp = 200
                print(f'''
HP has been restored to {player_hp}!''')
            print(f'''
Waiting for opponent's turn...''')
        elif option2 == 2:
            if player_energy_regen_count > 0:
                player_energy_regen_count = player_energy_regen_count - 1
                if player_energy_regen_count < 0:
                    player_energy_regen_count = 0
                restore2 = random.randint(10,50)
                SP = SP + int(restore2)
                if SP > 100:
                    SP = 100
                print(f'''
SP has been restored to {SP}!''')
            print(f'''
Waiting for opponent's turn...''')
        elif option2 == 3:
            if player_attack_item_count > 0:
                player_attack_item_count = player_attack_item_count - 1
                if player_attack_item_count < 0:
                    player_attack_item_count = 0
                if opponent_blocking == True:
                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                    time.sleep(0.5)
                    damage = random.randint(10,30)
                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - (damage - random.randint(10,30))
                    if opponent_hp < 0:
                        opponent_hp = 0
                    opponent_blocking = False
                elif opponent_dodging == True:
                    chance = random.randint(0,1)
                    if chance == 0:
                        print(f'''
Surprisingly, {opponent} succesfully dodged {character}'s attack!''')
                    else:
                        print(f'''
{opponent} failed to dodge {character}'s attack!''')
                        damage = random.randint(10,30)
                        print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                        opponent_hp = opponent_hp - damage
                        if opponent_hp < 0:
                            opponent_hp = 0
                    time.sleep(0.5)
                    opponent_dodging = False
                else:
                    damage = random.randint(10,30)
                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                    opponent_hp = opponent_hp - damage
                    if opponent_hp < 0:
                        opponent_hp = 0
            print(f'''
Waiting for opponent's turn...''')

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
    global winner, P1_HP, P2_HP, P1_SP, P2_SP, P1_hp_regen_count, P1_energy_regen_count, P1_attack_item_count, P2_hp_regen_count, P2_energy_regen_count, P2_attack_item_count, P1_blocking, P2_blocking, P1_dodging, P2_dodging, turn, damage, chance
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
