def option_func(character, option, option2, energy_regen_count, attack_item_count, hp_regen_count, SP):
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
            if SP >= 10:
                print(f'''{character} prepares to block the next move.''')
            else:
                print(f'''{character} is too exhausted to block.''')
        elif option2 == 2:
            if SP >= 20:
                print(f'''{character} prepares to dodge the next move.''')
            else:
                print(f'''{character} is too exhausted to dodge.''')
        elif option2 == 3:
            print(f'''{character} waits for the opponent's next move to save energy.''')
    elif option == 3:
        if character == "Noob":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Noob uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Noob uses x1 Energy Drink!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Noob uses x1 Dynamite!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Bacon":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Bacon uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Bacon uses x1 Energy Drink!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Bacon uses x1 Dynamite!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Pizza Man":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Pizza Man uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Pizza Man uses x1 Mountain Dew!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Pizza Man uses x1 Chili Sauce!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Murderer":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Murderer uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Murderer uses x1 Energy Drink!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Murderer uses x1 Poison Knife!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Criminal":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Criminal uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Criminal uses x1 Energy Drink!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Criminal uses x1 Grenade!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Cop":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Cop uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Cop uses x1 Gatorade Drink!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Cop uses x1 Taser!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Piggy":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Piggy uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Piggy uses x1 Blood Juice for Cannibals!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Piggy uses x1 Claw Trap!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Boxer":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Boxer uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Boxer uses x1 Red Bull!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Boxer uses x1 Steroids Attack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Ninja":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Ninja uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Ninja uses x1 Energy Pill!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Ninja uses x1 Shuriken!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
        if character == "Baller":
            if option2 == 1:
                if hp_regen_count > 0:
                    print(f'''Baller uses x1 Health Pack!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 2:
                if energy_regen_count > 0:
                    print(f'''Baller uses x1 Energy Drink!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')
            elif option2 == 3:
                if attack_item_count > 0:
                    print(f'''Baller uses x1 Shock Ball!''')
                else:
                    print(f'''{character} tried to find his/her item, not knowing it ran out.''')


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