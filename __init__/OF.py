def option_func(character, option1, option2, energy_regen_count, attack_item_count, hp_regen_count):
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