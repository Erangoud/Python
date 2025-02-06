import random

def snake_and_ladder(player_name, position, dice_rolls_count):
    dice_roll = random.randint(1, 6)  
    dice_rolls_count += 1
    
    option = random.randint(1, 3)  # Random option to select the movement
    
    if option == 1:
        position = position

    elif option == 2:
        if position + dice_roll > 100: 
            position = position
        else:
            position += dice_roll

    elif option == 3:
        position -= dice_roll
        if position < 0:  
            position = 0

    return player_name, dice_rolls_count, dice_roll, position

def player_turn(player_name, position, dice_rolls_count):
    return snake_and_ladder(player_name, position, dice_rolls_count)

p1_won=False
p2_won=False

p1_position=0
p1_rolls_count=0
p2_position=0
p2_rolls_count=0

while not p1_won and not p2_won:
    p1_name, p1_rolls_count, p1_dice_roll, p1_position = player_turn("player1", p1_position, p1_rolls_count)
    p2_name, p2_rolls_count,p2_dice_roll, p2_positon = player_turn("player2 ",p2_positon,p2_rolls_count)

    print(f"{p1_name} Roll_no {p1_rolls_count}: Dice = {p1_dice_roll}, Position = {p1_position}")
    print(f"{p2_name} Roll_no {p2_rolls_count}: Dice = {p2_dice_roll}, Position = {p2_position}")


    if p1_position >= 100:
        p1_won = True
    if p2_position >= 100:
        p2_won = True

if p1_won:
    print(f"p1 reached position 100 and WON the game in {p1_rolls_count} rolls!")
if p2_won:
    print(f"p2 reached position 100 and WON the game in {p2_rolls_count} rolls!")



