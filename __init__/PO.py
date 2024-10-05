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
