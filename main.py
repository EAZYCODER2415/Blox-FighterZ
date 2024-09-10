import random
import replit
import time

def choose_character(option):
    if option == "a" or option == 1:
        character = "Noob"
    elif option == "b" or option == 2:
        character = "Bacon"
    elif option == "c" or option == 3:
        character = "Pizza Man"
    elif option == "d" or option == 4:
        character = "Murderer"
    elif option == "e" or option == 5:
        character = "Criminal"
    elif option == "f" or option == 6:
        character = "Cop"
    elif option == "g" or option == 7:
        character = "Piggy"
    elif option == "h" or option == 8:
        character = "Boxer"
    elif option == "i" or option == 9:
        character = "Ninja"
    elif option == "j" or option == 10:
        character = "Baller"
    return character

def print_options(option, character, hp_regen_count, energy_regen_count, attack_item_count):
    if int(option) == 1:
        if character == "Noob":
            output = f'''
(1) Tackle (10 SP)
(2) Noob Sword Attack (20 SP)
(3) Raygun Rumble (50 SP)
'''
        elif character == "Bacon":
            output = f'''
(1) Tackle (10 SP)
(2) Karate from the Hoods (20 SP)
(3) Bacon Hair Strangle (50 SP)
'''
        elif character == "Pizza Man":
            output = f'''
(1) Tackle (10 SP)
(2) Flaming Pizza Disc (20 SP)
(3) Pizza Box Monster Army (50 SP)
'''
        elif character == "Murderer":
            output = f'''
(1) Tackle (10 SP)
(2) Knife Stab Flash: Sixfold (20 SP)
(3) Rain of Throwing Knives (50 SP)
'''
        elif character == "Criminal":
            output = f'''
(1) Tackle (10 SP)
(2) Gun Shot (20 SP)
(3) Car Crash Frenzy (50 SP)
'''
        elif character == "Cop":
            output = f'''
(1) Tackle (10 SP)
(2) Double Gun Shot (20 SP)
(3) Army of Campers (50 SP)
'''
        elif character == "Piggy":
            output = f'''
(1) Home Run (10 SP)
(2) Good Night Whack (20 SP)
(3) Laser Eye Beam (50 SP)
'''
        elif character == "Boxer":
            output = f'''
(1) Jab (10 SP)
(2) Spammer (20 SP)
(3) Overhand (50 SP)
'''
        elif character == "Ninja":
            output = f'''
(1) Karate Punch (10 SP)
(2) Shinobi Raiden 2K Barrage (20 SP)
(3) Spiral Energy Ball (50 SP)
'''
        elif character == "Baller":
            output = f'''
(1) Ball Jab (10 SP)
(2) Ball of Fire (20 SP)
(3) Multi Fireball Spam (50 SP)
'''
    elif int(option) == 2:
        output = f'''
(1) Block (10 SP)
(2) Dodge (20 SP)
(3) Wait
'''
    elif int(option) == 3:
        if character == "Noob":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Burger x{energy_regen_count}
(3) Dynamite x{attack_item_count}
'''
        elif character == "Bacon":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Energy Drink x{energy_regen_count}
(3) Dynamite x{attack_item_count}
'''
        elif character == "Pizza Man":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Mountain Dew x{energy_regen_count}
(3) Chili Sauce x{attack_item_count}
'''
        elif character == "Murderer":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Energy Drink x{energy_regen_count}
(3) Poison Knife x{attack_item_count}
'''
        elif character == "Criminal":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Energy Drink x{energy_regen_count}
(3) Grenade x{attack_item_count}
'''
        elif character == "Cop":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Gatorade Drink x{energy_regen_count}
(3) Taser x{attack_item_count}
'''
        elif character == "Piggy":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Blood Juice for Cannibals x{energy_regen_count}
(3) Claw Trap x{attack_item_count}
'''
        elif character == "Boxer":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Red Bull x{energy_regen_count}
(3) Steroids Attack x{attack_item_count}
'''
        elif character == "Ninja":
                output = f'''
(1) Health Pack x{hp_regen_count}
(2) Energy Pill x{energy_regen_count}
(3) Shuriken x{attack_item_count}
'''
        elif character == "Baller":
            output = f'''
(1) Health Pack x{hp_regen_count}
(2) Energy Drink x{energy_regen_count}
(3) Shock Ball x{attack_item_count}
'''
    return output

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
        replit.clear()
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
                    replit.clear()
                    if option == 1:
                        if character == "Noob":
                            if option2 == 1:
                                print(f'''Noob uses Tackle!''')
                            elif option2 == 2:
                                print(f'''Noob uses Noob Sword Attack!''')
                            elif option2 == 3:
                                print(f'''Noob uses Raygun Rumble!''')
                        elif character == "Bacon":
                            if option2 == 1:
                                print(f'''Bacon uses Tackle!''')
                            elif option2 == 2:
                                print(f'''Bacon uses Karate from the Hoods!''')
                            elif option2 == 3:
                                print(f'''Bacon uses Bacon Hair Strangle!''')
                        elif character == "Pizza Man":
                            if option2 == 1:
                                print(f'''Pizza Man uses Tackle!''')
                            elif option2 == 2:
                                print(f'''Pizza Man uses Flaming Pizza Disc!''')
                            elif option2 == 3:
                                print(f'''Pizza Man uses Pizza Box Monster Army!''')
                        elif character == "Murderer":
                            if option2 == 1:
                                print(f'''Murderer uses Tackle!''')
                            elif option2 == 2:
                                print(f'''Murderer uses Knife Stab Flash: Sixfold!''')
                            elif option2 == 3:
                                print(f'''Murderer uses Rain of Throwing Knives!''')
                        elif character == "Criminal":
                            if option2 == 1:
                                print(f'''Criminal uses Tackle!''')
                            elif option2 == 2:
                                print(f'''Criminal uses Gun Shot!''')
                            elif option2 == 3:
                                print(f'''Criminal uses Car Crash Frenzy!''')
                        elif character == "Cop":
                            if option2 == 1:
                                print(f'''Cop uses Tackle!''')
                            elif option2 == 2:
                                print(f'''Cop uses Double Gun Shot!''')
                            elif option2 == 3:
                                print(f'''Cop uses Army of Campers!''')
                        elif character == "Piggy":
                            if option2 == 1:
                                print(f'''Piggy uses Home Run!''')
                            elif option2 == 2:
                                print(f'''Piggy uses Good Night Whack!''')
                            elif option2 == 3:
                                print(f'''Piggy uses Laser Eye Beam!''')
                        elif character == "Boxer":
                            if option2 == 1:
                                print(f'''Boxer uses Jab!''')
                            elif option2 == 2:
                                print(f'''Boxer uses Spammer!''')
                            elif option2 == 3:
                                print(f'''Boxer uses Overhand!''')
                        elif character == "Ninja":
                            if option2 == 1:
                                print(f'''Ninja uses Karate Punch!''')
                            elif option2 == 2:
                                print(f'''Ninja uses Shinobi Raiden 2K Barrage!''')
                            elif option2 == 3:
                                print(f'''Ninja uses Spiral Energy Ball!''')
                        elif character == "Baller":
                            if option2 == 1:
                                print(f'''Baller uses Ball Jab!''')
                            elif option2 == 2:
                                print(f'''Baller uses Ball of Fire!''')
                            elif option2 == 3:
                                print(f'''Baller uses Multi Fireball Spam!''')
                    elif option == 2:
                        if option2 == 1:
                            if P1_SP >= 10:
                                print(f'''{character} prepares to block the next move.''')
                            else:
                                print(f'''{character} is too exhausted to block.''')
                        elif option2 == 2:
                            if P1_SP >= 20:
                                print(f'''{character} prepares to dodge the next move.''')
                            else:
                                print(f'''{character} is too exhausted to dodge.''')
                        elif option2 == 3:
                            print(f'''{character} waits for the opponent's next move to save energy.''')
                    elif option == 3:
                        if character == "Noob":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Noob uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Noob uses x1 Energy Drink!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Noob uses x1 Dynamite!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Bacon":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Bacon uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Bacon uses x1 Energy Drink!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Bacon uses x1 Dynamite!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Pizza Man":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Pizza Man uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Pizza Man uses x1 Mountain Dew!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Pizza Man uses x1 Chili Sauce!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Murderer":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Murderer uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Murderer uses x1 Energy Drink!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Murderer uses x1 Poison Knife!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Criminal":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Criminal uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Criminal uses x1 Energy Drink!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Criminal uses x1 Grenade!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Cop":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Cop uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Cop uses x1 Gatorade Drink!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Cop uses x1 Taser!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Piggy":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Piggy uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Piggy uses x1 Blood Juice for Cannibals!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Piggy uses x1 Claw Trap!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Boxer":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Boxer uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Boxer uses x1 Red Bull!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Boxer uses x1 Steroids Attack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Ninja":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Ninja uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Ninja uses x1 Energy Pill!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Ninja uses x1 Shuriken!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                        if character == "Baller":
                            if option2 == 1:
                                if P1_hp_regen_count > 0:
                                    print(f'''Baller uses x1 Health Pack!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P1_energy_regen_count > 0:
                                    print(f'''Baller uses x1 Energy Drink!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Baller uses x1 Shock Ball!''')
                                else:
                                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
                    time.sleep(1)
                    if option == 1:
                        if option2 == 1:
                            if P1_SP >= 10:
                                if P2_blocking == True:
                                    P1_SP = P1_SP - 10
                                    if P1_SP < 0:
                                        P1_SP = 0
                                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(10,30)
                                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - (damage - random.randint(10,30))
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    P2_blocking = False
                                elif P2_dodging == True:
                                    P1_SP = P1_SP - 10
                                    if P1_SP < 0:
                                        P1_SP = 0
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
                                        P2_HP = P2_HP - damage
                                        if P2_HP < 0:
                                            P2_HP = 0
                                    time.sleep(0.5)
                                    P2_dodging = False
                                else:
                                    P1_SP = P1_SP - 10
                                    if P1_SP < 0:
                                        P1_SP = 0
                                    damage = random.randint(10,30)
                                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - damage
                                    if P2_HP < 0:
                                        P2_HP = 0
                            else:
                                if P2_blocking == True:
                                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(10,30)
                                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - (damage - random.randint(10,30))
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    P2_blocking = False
                                elif P2_dodging == True:
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
                                        P2_HP = P2_HP - damage
                                        if P2_HP < 0:
                                            P2_HP = 0
                                    time.sleep(0.5)
                                    P2_dodging = False
                                else:
                                    damage = random.randint(10,30)
                                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - damage
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    time.sleep(0.5)
                                hp_loss = random.randint(10,50)
                                print(f'''
{character} lost {hp_loss} HP after risking the move from being tired.''')
                                P1_HP = P1_HP - hp_loss
                                if P2_HP < 0:
                                    P2_HP = 0
                        elif option2 == 2:
                            if P1_SP >= 20:
                                if P2_blocking == True:
                                    P1_SP = P1_SP - 20
                                    if P1_SP < 0:
                                        P1_SP = 0
                                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(40,60)
                                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - (damage + random.randint(40,60))
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    P2_blocking = False
                                elif P2_dodging == True:
                                    P1_SP = P1_SP - 20
                                    if P1_SP < 0:
                                        P1_SP = 0
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
                                        P2_HP = P2_HP - damage
                                        if P2_HP < 0:
                                            P2_HP = 0
                                    time.sleep(0.5)
                                    P2_dodging = False
                                else:
                                    P1_SP = P1_SP - 20
                                    if P1_SP < 0:
                                        P1_SP = 0
                                    damage = random.randint(40,60)
                                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - damage
                                    if P2_HP < 0:
                                        P2_HP = 0
                            else:
                                if P2_blocking == True:
                                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(40,60)
                                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - (damage + random.randint(40,60))
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    P2_blocking = False
                                elif P2_dodging == True:
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
                                        P2_HP = P2_HP - damage
                                        if P2_HP < 0:
                                            P2_HP = 0
                                    time.sleep(0.5)
                                    P2_dodging = False
                                else:
                                    damage = random.randint(40,60)
                                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - damage
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    time.sleep(0.5)
                                hp_loss = random.randint(50,70)
                                print(f'''
{character} lost {hp_loss} HP after risking the move from being tired.''')
                                P1_HP = P1_HP - hp_loss
                                if P2_HP < 0:
                                    P2_HP = 0
                        elif option2 == 3:
                            if P1_SP >= 50:
                                if P2_blocking == True:
                                    P1_SP = P1_SP - 50
                                    if P1_SP < 0:
                                        P1_SP = 0
                                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(70,100)
                                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - (damage + random.randint(70,100))
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    P2_blocking = False
                                elif P2_dodging == True:
                                    P1_SP = P1_SP - 50
                                    if P1_SP < 0:
                                        P1_SP = 0
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
                                        P2_HP = P2_HP - damage
                                        if P2_HP < 0:
                                            P2_HP = 0
                                    time.sleep(0.5)
                                    P2_dodging = False
                                else:
                                    P1_SP = P1_SP - 50
                                    if P1_SP < 0:
                                        P1_SP = 0
                                    damage = random.randint(70,100)
                                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - damage
                                    if P2_HP < 0:
                                        P2_HP = 0
                            else:
                                if P2_blocking == True:
                                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(70,100)
                                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - (damage + random.randint(70,100))
                                    P2_blocking = False
                                elif P2_dodging == True:
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
                                        P2_HP = P2_HP - damage
                                        if P2_HP < 0:
                                            P2_HP = 0
                                    time.sleep(0.5)
                                    P2_dodging = False
                                else:
                                    damage = random.randint(70,100)
                                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - damage
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    time.sleep(0.5)
                                hp_loss = random.randint(70,100)
                                print(f'''
{character} lost {hp_loss} HP after risking the move from being tired.''')
                                P1_HP = P1_HP - hp_loss
                    elif option == 2:
                        if option2 == 1:
                            if P1_SP >= 10:
                                P1_SP = P1_SP - 10
                                if P1_SP < 0:
                                    P1_SP = 0
                                P1_blocking = True
                            print(f'''
Waiting for opponent's turn...''')
                        elif option2 == 2:
                            if P1_SP >= 20:
                                P1_SP = P1_SP - 20
                                if P1_SP < 0:
                                    P1_SP = 0
                                P1_dodging = True
                            print(f'''
Waiting for opponent's turn...''')
                        elif option2 == 3:
                            restore = random.randint(10,50)
                            P1_SP = P1_SP + int(restore)
                            if P1_SP > 100:
                                P1_SP = 100
                            print(f'''
SP has been restored to {P1_SP}!''')
                    elif option == 3:
                        if option2 == 1:
                            if P1_hp_regen_count > 0:
                                P1_hp_regen_count = P1_hp_regen_count - 1
                                if P1_hp_regen_count < 0:
                                    P1_hp_regen_count = 0
                                hp_restore = random.randint(30,100)
                                P1_HP = P1_HP + int(hp_restore)
                                if P1_HP > 200:
                                    P1_HP = 200
                                print(f'''
HP has been restored to {P1_HP}!''')
                            print(f'''
Waiting for opponent's turn...''')
                        elif option2 == 2:
                            if P1_energy_regen_count > 0:
                                P1_energy_regen_count = P1_energy_regen_count - 1
                                if P1_energy_regen_count < 0:
                                    P1_energy_regen_count = 0
                                restore2 = random.randint(10,50)
                                P1_SP = P1_SP + int(restore2)
                                if P1_SP > 100:
                                    P1_SP = 100
                                print(f'''
SP has been restored to {P1_SP}!''')
                            print(f'''
Waiting for opponent's turn...''')
                        elif option2 == 3:
                            if P1_attack_item_count > 0:
                                P1_attack_item_count = P1_attack_item_count - 1
                                if P1_attack_item_count < 0:
                                    P1_attack_item_count = 0
                                if P2_blocking == True:
                                    print(f'''
Surprisingly, {opponent} succesfully blocked {character}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(10,30)
                                    print(f'''
{opponent} has slightly taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - (damage - random.randint(10,30))
                                    if P2_HP < 0:
                                        P2_HP = 0
                                    P2_blocking = False
                                elif P2_dodging == True:
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
                                        P2_HP = P2_HP - damage
                                        if P2_HP < 0:
                                            P2_HP = 0
                                    time.sleep(0.5)
                                    P2_dodging = False
                                else:
                                    damage = random.randint(10,30)
                                    print(f'''
{opponent} has taken {damage} damage from {character}'s attack!''')
                                    P2_HP = P2_HP - damage
                                    if P2_HP < 0:
                                        P2_HP = 0
                            print(f'''
Waiting for opponent's turn...''')
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
                    if opponent_option1 == 1:
                        if opponent == "Noob":
                            if opponent_option2 == 1:
                                print(f'''Noob uses Tackle!''')
                            elif opponent_option2 == 2:
                                print(f'''Noob uses Noob Sword Attack!''')
                            elif opponent_option2 == 3:
                                print(f'''Noob uses Raygun Rumble!''')
                        elif opponent == "Bacon":
                            if opponent_option2 == 1:
                                print(f'''Bacon uses Tackle!''')
                            elif opponent_option2 == 2:
                                print(f'''Bacon uses Karate from the Hoods!''')
                            elif opponent_option2 == 3:
                                print(f'''Bacon uses Bacon Hair Strangle!''')
                        elif opponent == "Pizza Man":
                            if opponent_option2 == 1:
                                print(f'''Pizza Man uses Tackle!''')
                            elif opponent_option2 == 2:
                                print(f'''Pizza Man uses Flaming Pizza Disc!''')
                            elif opponent_option2 == 3:
                                print(f'''Pizza Man uses Pizza Box Monster Army!''')
                        elif opponent == "Murderer":
                            if opponent_option2 == 1:
                                print(f'''Murderer uses Tackle!''')
                            elif opponent_option2 == 2:
                                print(f'''Murderer uses Knife Stab Flash: Sixfold!''')
                            elif opponent_option2 == 3:
                                print(f'''Murderer uses Rain of Throwing Knives!''')
                        elif opponent == "Criminal":
                            if opponent_option2 == 1:
                                print(f'''Criminal uses Tackle!''')
                            elif opponent_option2 == 2:
                                print(f'''Criminal uses Gun Shot!''')
                            elif opponent_option2 == 3:
                                print(f'''Criminal uses Car Crash Frenzy!''')
                        elif opponent == "Cop":
                            if opponent_option2 == 1:
                                print(f'''Cop uses Tackle!''')
                            elif opponent_option2 == 2:
                                print(f'''Cop uses Double Gun Shot!''')
                            elif opponent_option2 == 3:
                                print(f'''Cop uses Army of Campers!''')
                        elif opponent == "Piggy":
                            if opponent_option2 == 1:
                                print(f'''Piggy uses Home Run!''')
                            elif opponent_option2 == 2:
                                print(f'''Piggy uses Good Night Whack!''')
                            elif opponent_option2 == 3:
                                print(f'''Piggy uses Laser Eye Beam!''')
                        elif opponent == "Boxer":
                            if opponent_option2 == 1:
                                print(f'''Boxer uses Jab!''')
                            elif opponent_option2 == 2:
                                print(f'''Boxer uses Spammer!''')
                            elif opponent_option2 == 3:
                                print(f'''Boxer uses Overhand!''')
                        elif opponent == "Ninja":
                            if opponent_option2 == 1:
                                print(f'''Ninja uses Karate Punch!''')
                            elif opponent_option2 == 2:
                                    print(f'''Ninja uses Shinobi Raiden 2K Barrage!''')
                            elif opponent_option2 == 3:
                                    print(f'''Ninja uses Spiral Energy Ball!''')
                        elif opponent == "Baller":
                            if opponent_option2 == 1:
                                print(f'''Baller uses Ball Jab!''')
                            elif opponent_option2 == 2:
                                print(f'''Baller uses Ball of Fire!''')
                            elif opponent_option2 == 3:
                                print(f'''Baller uses Multi Fireball Spam!''')
                    elif opponent_option1 == 2:
                        if opponent_option2 == 1:
                            if P2_SP >= 10:
                                print(f'''{opponent} prepares to block the next move.''')
                            else:
                                print(f'''{opponent} is too exhausted to block.''')
                        elif opponent_option2 == 2:
                            if P2_SP >= 20:
                                print(f'''{opponent} prepares to dodge the next move.''')
                            else:
                                print(f'''{opponent} is too exhausted to dodge.''')
                        elif opponent_option2 == 3:
                                print(f'''{opponent} waits for the opponent's next move to save energy.''')
                    elif opponent_option1 == 3:
                        if opponent == "Noob":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Noob uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Noob uses x1 Energy Drink!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Noob uses x1 Dynamite!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Bacon":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Bacon uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Bacon uses x1 Energy Drink!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Bacon uses x1 Dynamite!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Pizza Man":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Pizza Man uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Pizza Man uses x1 Mountain Dew!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Pizza Man uses x1 Chili Sauce!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Murderer":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Murderer uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Murderer uses x1 Energy Drink!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Murderer uses x1 Poison Knife!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Criminal":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Criminal uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Criminal uses x1 Energy Drink!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Criminal uses x1 Grenade!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Cop":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Cop uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Cop uses x1 Gatorade Drink!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Cop uses x1 Taser!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Piggy":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Piggy uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Piggy uses x1 Blood Juice for Cannibals!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P1_attack_item_count > 0:
                                    print(f'''Piggy uses x1 Claw Trap!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Boxer":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Boxer uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Boxer uses x1 Red Bull!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Boxer uses x1 Steroids Attack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Ninja":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Ninja uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Ninja uses x1 Energy Pill!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Ninja uses x1 Shuriken!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        if opponent == "Baller":
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    print(f'''Baller uses x1 Health Pack!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    print(f'''Baller uses x1 Energy Drink!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    print(f'''Baller uses x1 Shock Ball!''')
                                else:
                                    print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                    time.sleep(1)
                    if opponent_option1 == 1:
                        if opponent_option2 == 1:
                            if P2_SP >= 10:
                                if P1_blocking == True:
                                    P2_SP = P2_SP - 10
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(10,30)
                                    print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - (damage - random.randint(10,30))
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    P1_blocking = False
                                elif P1_dodging == True:
                                    P2_SP = P2_SP - 10
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    chance = random.randint(0,1)
                                    if chance == 0:
                                        print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                    else:
                                        print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                    time.sleep(0.5)
                                    P1_dodging = False
                                else:
                                    P2_SP = P2_SP - 10
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    damage = random.randint(10,30)
                                    print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - damage
                                    if P1_HP < 0:
                                        P1_HP = 0
                            else:
                                if P1_blocking == True:
                                    print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(10,30)
                                    print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - (damage - random.randint(10,30))
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    P1_blocking = False
                                elif P1_dodging == True:
                                    chance = random.randint(0,1)
                                    if chance == 0:
                                        print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                    else:
                                        print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                    time.sleep(0.5)
                                    P1_dodging = False
                                else:
                                    damage = random.randint(10,30)
                                    print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - damage
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    time.sleep(0.5)
                                hp_loss = random.randint(10,50)
                                print(f'''
{opponent} lost {hp_loss} HP after risking the move from being tired.''')
                                P2_HP = P2_HP - hp_loss
                                if P2_HP < 0:
                                    P2_HP = 0
                        elif opponent_option2 == 2:
                            if P2_SP >= 20:
                                if P1_blocking == True:
                                    P2_SP = P2_SP - 20
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(40,60)
                                    print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - (damage + random.randint(40,60))
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    P1_blocking = False
                                elif P1_dodging == True:
                                    P2_SP = P2_SP - 20
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    chance = random.randint(0,1)
                                    if chance == 0:
                                        print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                    else:
                                        print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                    time.sleep(0.5)
                                    P1_dodging = False
                                else:
                                    P2_SP = P2_SP - 20
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    damage = random.randint(40,60)
                                    print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - damage
                                    if P1_HP < 0:
                                        P1_HP = 0
                            else:
                                if P1_blocking == True:
                                    print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(40,60)
                                    print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - (damage + random.randint(40,60))
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    P1_blocking = False
                                elif P1_dodging == True:
                                    chance = random.randint(0,1)
                                    if chance == 0:
                                        print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                    else:
                                        print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                    time.sleep(0.5)
                                    P1_dodging = False
                                else:
                                    damage = random.randint(40,60)
                                    print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - damage
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    time.sleep(0.5)
                                hp_loss = random.randint(50,70)
                                print(f'''
{opponent} lost {hp_loss} HP after risking the move from being tired.''')
                                P2_HP = P2_HP - hp_loss
                                if P2_HP < 0:
                                    P2_SP = 0
                        elif opponent_option2 == 3:
                            if P2_SP >= 50:
                                if P1_blocking == True:
                                    P2_SP = P2_SP - 50
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(70,100)
                                    print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - (damage + random.randint(70,100))
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    P1_blocking = False
                                elif P1_dodging == True:
                                    P2_SP = P2_SP - 50
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    chance = random.randint(0,1)
                                    if chance == 0:
                                        print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                    else:
                                        print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                    time.sleep(0.5)
                                    P1_dodging = False
                                else:
                                    P2_SP = P2_SP - 50
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    damage = random.randint(70,100)
                                    print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - damage
                                    if P1_HP < 0:
                                        P1_HP = 0
                            else:
                                if P1_blocking == True:
                                    print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(70,100)
                                    print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - (damage + random.randint(70,100))
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    P1_blocking = False
                                elif P1_dodging == True:
                                    chance = random.randint(0,1)
                                    if chance == 0:
                                        print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                    else:
                                        print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                    time.sleep(0.5)
                                    P1_dodging = False
                                else:
                                    damage = random.randint(70,100)
                                    print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - damage
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    time.sleep(0.5)
                                hp_loss = random.randint(70,100)
                                print(f'''
{opponent} lost {hp_loss} HP after risking the move from being tired.''')
                                P2_HP = P2_HP - hp_loss
                                if P2_HP < 0:
                                    P2_HP = 0
                    elif opponent_option1 == 2:
                        if opponent_option2 == 1:
                            if P2_SP >= 10:
                                P2_SP = P2_SP - 10
                                if P2_SP < 0:
                                    P2_SP = 0
                                P2_blocking = True
                            print(f'''
Waiting for opponent's turn...''')
                        elif opponent_option2 == 2:
                            if P2_SP >= 20:
                                P2_SP = P2_SP - 20
                                if P2_SP < 0:
                                    P2_SP = 0
                                P2_dodging = True
                            print(f'''
Waiting for opponent's turn...''')
                        elif opponent_option2 == 3:
                            restore = random.randint(10,50)
                            P2_SP = P2_SP + int(restore)
                            if P2_SP > 100:
                                P2_SP = 100
                            print(f'''
SP has been restored to {P2_SP}!''')
                    elif opponent_option1 == 3:
                        if opponent_option2 == 1:
                            if P2_hp_regen_count > 0:
                                P2_hp_regen_count = P2_hp_regen_count - 1
                                if P2_hp_regen_count < 0:
                                    P2_hp_regen_count = 0
                                hp_restore = random.randint(30,100)
                                P2_HP = P2_HP + int(hp_restore)
                                if P2_HP > 200:
                                    P2_HP = 200
                                print(f'''
HP has been restored to {P2_HP}!''')
                            print(f'''
Waiting for opponent's turn...''')
                        elif opponent_option2 == 2:
                            if P2_energy_regen_count > 0:
                                P2_energy_regen_count = P2_energy_regen_count - 1
                                if P2_energy_regen_count < 0:
                                    P2_energy_regen_count = 0
                                restore2 = random.randint(10,50)
                                P2_SP = P2_SP + int(restore2)
                                if P2_SP > 100:
                                    P2_SP = 100
                                print(f'''
SP has been restored to {P2_SP}!''')
                            print(f'''
Waiting for opponent's turn...''')
                        elif opponent_option2 == 3:
                            if P2_attack_item_count > 0:
                                P2_attack_item_count = P2_attack_item_count - 1
                                if P2_attack_item_count < 0:
                                    P2_attack_item_count = 0
                                if P1_blocking == True:
                                    print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                    time.sleep(0.5)
                                    damage = random.randint(10,30)
                                    print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - (damage - random.randint(10,30))
                                    if P1_HP < 0:
                                        P1_HP = 0
                                    P1_blocking = False
                                elif P1_dodging == True:
                                    chance = random.randint(0,1)
                                    if chance == 0:
                                        print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                    else:
                                        print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                    time.sleep(0.5)
                                    P1_dodging = False
                                else:
                                    damage = random.randint(10,30)
                                    print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                    P1_HP = P1_HP - damage
                                    if P1_HP < 0:
                                        P1_HP = 0
                            print(f'''
Waiting for opponent's turn...''')
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
                        replit.clear()
                        if opponent_option1 == 1:
                            if opponent == "Noob":
                                if opponent_option2 == 1:
                                    print(f'''Noob uses Tackle!''')
                                elif opponent_option2 == 2:
                                    print(f'''Noob uses Noob Sword Attack!''')
                                elif opponent_option2 == 3:
                                    print(f'''Noob uses Raygun Rumble!''')
                            elif opponent == "Bacon":
                                if opponent_option2 == 1:
                                    print(f'''Bacon uses Tackle!''')
                                elif opponent_option2 == 2:
                                    print(f'''Bacon uses Karate from the Hoods!''')
                                elif opponent_option2 == 3:
                                    print(f'''Bacon uses Bacon Hair Strangle!''')
                            elif opponent == "Pizza Man":
                                if opponent_option2 == 1:
                                    print(f'''Pizza Man uses Tackle!''')
                                elif opponent_option2 == 2:
                                    print(f'''Pizza Man uses Flaming Pizza Disc!''')
                                elif opponent_option2 == 3:
                                    print(f'''Pizza Man uses Pizza Box Monster Army!''')
                            elif opponent == "Murderer":
                                if opponent_option2 == 1:
                                    print(f'''Murderer uses Tackle!''')
                                elif opponent_option2 == 2:
                                    print(f'''Murderer uses Knife Stab Flash: Sixfold!''')
                                elif opponent_option2 == 3:
                                    print(f'''Murderer uses Rain of Throwing Knives!''')
                            elif opponent == "Criminal":
                                if opponent_option2 == 1:
                                    print(f'''Criminal uses Tackle!''')
                                elif opponent_option2 == 2:
                                    print(f'''Criminal uses Gun Shot!''')
                                elif opponent_option2 == 3:
                                    print(f'''Criminal uses Car Crash Frenzy!''')
                            elif opponent == "Cop":
                                if opponent_option2 == 1:
                                    print(f'''Cop uses Tackle!''')
                                elif opponent_option2 == 2:
                                    print(f'''Cop uses Double Gun Shot!''')
                                elif opponent_option2 == 3:
                                    print(f'''Cop uses Army of Campers!''')
                            elif opponent == "Piggy":
                                if opponent_option2 == 1:
                                    print(f'''Piggy uses Home Run!''')
                                elif opponent_option2 == 2:
                                    print(f'''Piggy uses Good Night Whack!''')
                                elif opponent_option2 == 3:
                                    print(f'''Piggy uses Laser Eye Beam!''')
                            elif opponent == "Boxer":
                                if opponent_option2 == 1:
                                    print(f'''Boxer uses Jab!''')
                                elif opponent_option2 == 2:
                                    print(f'''Boxer uses Spammer!''')
                                elif opponent_option2 == 3:
                                    print(f'''Boxer uses Overhand!''')
                            elif opponent == "Ninja":
                                if opponent_option2 == 1:
                                    print(f'''Ninja uses Karate Punch!''')
                                elif opponent_option2 == 2:
                                        print(f'''Ninja uses Shinobi Raiden 2K Barrage!''')
                                elif opponent_option2 == 3:
                                        print(f'''Ninja uses Spiral Energy Ball!''')
                            elif opponent == "Baller":
                                if opponent_option2 == 1:
                                    print(f'''Baller uses Ball Jab!''')
                                elif opponent_option2 == 2:
                                    print(f'''Baller uses Ball of Fire!''')
                                elif opponent_option2 == 3:
                                    print(f'''Baller uses Multi Fireball Spam!''')
                        elif opponent_option1 == 2:
                            if opponent_option2 == 1:
                                if P2_SP >= 10:
                                    print(f'''{opponent} prepares to block the next move.''')
                                else:
                                    print(f'''{opponent} is too exhausted to block.''')
                            elif opponent_option2 == 2:
                                if P2_SP >= 20:
                                    print(f'''{opponent} prepares to dodge the next move.''')
                                else:
                                    print(f'''{opponent} is too exhausted to dodge.''')
                            elif opponent_option2 == 3:
                                    print(f'''{opponent} waits for the opponent's next move to save energy.''')
                        elif opponent_option1 == 3:
                            if opponent == "Noob":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Noob uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Noob uses x1 Energy Drink!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Noob uses x1 Dynamite!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Bacon":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Bacon uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Bacon uses x1 Energy Drink!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Bacon uses x1 Dynamite!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Pizza Man":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Pizza Man uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Pizza Man uses x1 Mountain Dew!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Pizza Man uses x1 Chili Sauce!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Murderer":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Murderer uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Murderer uses x1 Energy Drink!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Murderer uses x1 Poison Knife!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Criminal":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Criminal uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Criminal uses x1 Energy Drink!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Criminal uses x1 Grenade!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Cop":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Cop uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Cop uses x1 Gatorade Drink!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Cop uses x1 Taser!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Piggy":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Piggy uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Piggy uses x1 Blood Juice for Cannibals!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P1_attack_item_count > 0:
                                        print(f'''Piggy uses x1 Claw Trap!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Boxer":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Boxer uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Boxer uses x1 Red Bull!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Boxer uses x1 Steroids Attack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Ninja":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Ninja uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Ninja uses x1 Energy Pill!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Ninja uses x1 Shuriken!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                            if opponent == "Baller":
                                if opponent_option2 == 1:
                                    if P2_hp_regen_count > 0:
                                        print(f'''Baller uses x1 Health Pack!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 2:
                                    if P2_energy_regen_count > 0:
                                        print(f'''Baller uses x1 Energy Drink!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                                elif opponent_option2 == 3:
                                    if P2_attack_item_count > 0:
                                        print(f'''Baller uses x1 Shock Ball!''')
                                    else:
                                        print(f'''{opponent} tried to find his/her item, not knowing it ran out.''')
                        time.sleep(1)
                        if opponent_option1 == 1:
                            if opponent_option2 == 1:
                                if P2_SP >= 10:
                                    if P1_blocking == True:
                                        P2_SP = P2_SP - 10
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                        time.sleep(0.5)
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - (damage - random.randint(10,30))
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        P1_blocking = False
                                    elif P1_dodging == True:
                                        P2_SP = P2_SP - 10
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        chance = random.randint(0,1)
                                        if chance == 0:
                                            print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                        else:
                                            print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                            damage = random.randint(10,30)
                                            print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                            P1_HP = P1_HP - damage
                                            if P1_HP < 0:
                                                P1_HP = 0
                                        time.sleep(0.5)
                                        P1_dodging = False
                                    else:
                                        P2_SP = P2_SP - 10
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                else:
                                    if P1_blocking == True:
                                        print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                        time.sleep(0.5)
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - (damage - random.randint(10,30))
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        P1_blocking = False
                                    elif P1_dodging == True:
                                        chance = random.randint(0,1)
                                        if chance == 0:
                                            print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                        else:
                                            print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                            damage = random.randint(10,30)
                                            print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                            P1_HP = P1_HP - damage
                                            if P1_HP < 0:
                                                P1_HP = 0
                                        time.sleep(0.5)
                                        P1_dodging = False
                                    else:
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        time.sleep(0.5)
                                    hp_loss = random.randint(10,50)
                                    print(f'''
{opponent} lost {hp_loss} HP after risking the move from being tired.''')
                                    P2_HP = P2_HP - hp_loss
                                    if P2_HP < 0:
                                        P2_HP = 0
                            elif opponent_option2 == 2:
                                if P2_SP >= 20:
                                    if P1_blocking == True:
                                        P2_SP = P2_SP - 20
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                        time.sleep(0.5)
                                        damage = random.randint(40,60)
                                        print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - (damage + random.randint(40,60))
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        P1_blocking = False
                                    elif P1_dodging == True:
                                        P2_SP = P2_SP - 20
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        chance = random.randint(0,1)
                                        if chance == 0:
                                            print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                        else:
                                            print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                            damage = random.randint(10,30)
                                            print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                            P1_HP = P1_HP - damage
                                            if P1_HP < 0:
                                                P1_HP = 0
                                        time.sleep(0.5)
                                        P1_dodging = False
                                    else:
                                        P2_SP = P2_SP - 20
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        damage = random.randint(40,60)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                else:
                                    if P1_blocking == True:
                                        print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                        time.sleep(0.5)
                                        damage = random.randint(40,60)
                                        print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - (damage + random.randint(40,60))
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        P1_blocking = False
                                    elif P1_dodging == True:
                                        chance = random.randint(0,1)
                                        if chance == 0:
                                            print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                        else:
                                            print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                            damage = random.randint(10,30)
                                            print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                            P1_HP = P1_HP - damage
                                            if P1_HP < 0:
                                                P1_HP = 0
                                        time.sleep(0.5)
                                        P1_dodging = False
                                    else:
                                        damage = random.randint(40,60)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        time.sleep(0.5)
                                    hp_loss = random.randint(50,70)
                                    print(f'''
{opponent} lost {hp_loss} HP after risking the move from being tired.''')
                                    P2_HP = P2_HP - hp_loss
                                    if P2_HP < 0:
                                        P2_SP = 0
                            elif opponent_option2 == 3:
                                if P2_SP >= 50:
                                    if P1_blocking == True:
                                        P2_SP = P2_SP - 50
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                        time.sleep(0.5)
                                        damage = random.randint(70,100)
                                        print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - (damage + random.randint(70,100))
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        P1_blocking = False
                                    elif P1_dodging == True:
                                        P2_SP = P2_SP - 50
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        chance = random.randint(0,1)
                                        if chance == 0:
                                            print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                        else:
                                            print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                            damage = random.randint(10,30)
                                            print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                            P1_HP = P1_HP - damage
                                            if P1_HP < 0:
                                                P1_HP = 0
                                        time.sleep(0.5)
                                        P1_dodging = False
                                    else:
                                        P2_SP = P2_SP - 50
                                        if P2_SP < 0:
                                            P2_SP = 0
                                        damage = random.randint(70,100)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                else:
                                    if P1_blocking == True:
                                        print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                        time.sleep(0.5)
                                        damage = random.randint(70,100)
                                        print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - (damage + random.randint(70,100))
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        P1_blocking = False
                                    elif P1_dodging == True:
                                        chance = random.randint(0,1)
                                        if chance == 0:
                                            print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                        else:
                                            print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                            damage = random.randint(10,30)
                                            print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                            P1_HP = P1_HP - damage
                                            if P1_HP < 0:
                                                P1_HP = 0
                                        time.sleep(0.5)
                                        P1_dodging = False
                                    else:
                                        damage = random.randint(70,100)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        time.sleep(0.5)
                                    hp_loss = random.randint(70,100)
                                    print(f'''
{opponent} lost {hp_loss} HP after risking the move from being tired.''')
                                    P2_HP = P2_HP - hp_loss
                                    if P2_HP < 0:
                                        P2_HP = 0
                        elif opponent_option1 == 2:
                            if opponent_option2 == 1:
                                if P2_SP >= 10:
                                    P2_SP = P2_SP - 10
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    P2_blocking = True
                                print(f'''
Waiting for opponent's turn...''')
                            elif opponent_option2 == 2:
                                if P2_SP >= 20:
                                    P2_SP = P2_SP - 20
                                    if P2_SP < 0:
                                        P2_SP = 0
                                    P2_dodging = True
                                print(f'''
Waiting for opponent's turn...''')
                            elif opponent_option2 == 3:
                                restore = random.randint(10,50)
                                P2_SP = P2_SP + int(restore)
                                if P2_SP > 100:
                                    P2_SP = 100
                                print(f'''
SP has been restored to {P2_SP}!''')
                        elif opponent_option1 == 3:
                            if opponent_option2 == 1:
                                if P2_hp_regen_count > 0:
                                    P2_hp_regen_count = P2_hp_regen_count - 1
                                    if P2_hp_regen_count < 0:
                                        P2_hp_regen_count = 0
                                    hp_restore = random.randint(30,100)
                                    P2_HP = P2_HP + int(hp_restore)
                                    if P2_HP > 200:
                                        P2_HP = 200
                                    print(f'''
HP has been restored to {P2_HP}!''')
                                print(f'''
Waiting for opponent's turn...''')
                            elif opponent_option2 == 2:
                                if P2_energy_regen_count > 0:
                                    P2_energy_regen_count = P2_energy_regen_count - 1
                                    if P2_energy_regen_count < 0:
                                        P2_energy_regen_count = 0
                                    restore2 = random.randint(10,50)
                                    P2_SP = P2_SP + int(restore2)
                                    if P2_SP > 100:
                                        P2_SP = 100
                                    print(f'''
SP has been restored to {P2_SP}!''')
                                print(f'''
Waiting for opponent's turn...''')
                            elif opponent_option2 == 3:
                                if P2_attack_item_count > 0:
                                    P2_attack_item_count = P2_attack_item_count - 1
                                    if P2_attack_item_count < 0:
                                        P2_attack_item_count = 0
                                    if P1_blocking == True:
                                        print(f'''
Surprisingly, {character} succesfully blocked {opponent}'s attack!''')
                                        time.sleep(0.5)
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has slightly taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - (damage - random.randint(10,30))
                                        if P1_HP < 0:
                                            P1_HP = 0
                                        P1_blocking = False
                                    elif P1_dodging == True:
                                        chance = random.randint(0,1)
                                        if chance == 0:
                                            print(f'''
Surprisingly, {character} succesfully dodged {opponent}'s attack!''')
                                        else:
                                            print(f'''
{character} failed to dodge {opponent}'s attack!''')
                                            damage = random.randint(10,30)
                                            print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                            P1_HP = P1_HP - damage
                                            if P1_HP < 0:
                                                P1_HP = 0
                                        time.sleep(0.5)
                                        P1_dodging = False
                                    else:
                                        damage = random.randint(10,30)
                                        print(f'''
{character} has taken {damage} damage from {opponent}'s attack!''')
                                        P1_HP = P1_HP - damage
                                        if P1_HP < 0:
                                            P1_HP = 0
                                print(f'''
Waiting for opponent's turn...''')
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