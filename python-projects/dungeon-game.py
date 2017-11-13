# randomly generates monster, door and player location. player attempts to escape in the room with the door, or is eaten alive by monster in room
# learning points:
    # unpacking tuples
    # clear screen function from os library
    # visual mapping using python

import os
import random

# draw grid


# pick random location for monster
# draw player in grid
# take input for movement
# move player unless invalid move (past edges of grid)
# check for win/loss

def clear_screen(): # clear screen and redraw grid
    os.system('cls' if os.name == 'nt' else 'clear')

CELLS = [(0,0), (1,0), (2,0) , (3,0), (4,0),
         (0,1), (1,1), (2,1) , (3,1), (4,1),
         (0,2), (1,2), (2,2) , (3,2), (4,2),
         (0,3), (1,3), (2,3) , (3,3), (4,3),
         (0,4), (1,4), (2,4) , (3,4), (4,4)]

def get_locations():
    # pick random location for monster
    # pick random location for player
    # pick random location for exit door
    return random.sample(CELLS, 3)

def move_player(player, move):
    x, y = player # get player's location
    if move == 'LEFT': # if move == 'LEFT', x-1
        x -= 1
    if move == 'RIGHT': # if move == 'RIGHT', x+1
        x += 1
    if move == 'UP': # if move == 'UP', y-1
        y -= 1
    if move == 'DOWN': # if move =='DOWN', y+1
        y += 1
    return x, y

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player # unpack player's location tuple into coordinates
    if x == 0: # if player's y == 0, they can't move UP
        moves.remove("LEFT")
    if x == 4: # if player's y == 4, they can't move DOWN
        moves.remove('RIGHT')
    if y == 0: # if player's x == 0, they can't move LEFT
        moves.remove('UP')
    if y == 4: # if player's x == 4, they can't move RIGHT
        moves.remove('DOWN')
    return moves

def draw_map(player):
    print(" _" * 5) # prints upper walls of cell
    tile = "|{}" # sets up left walls of cell
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else: 
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else: output = tile.format("_|")
        print(output, end = line_end)


    
def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)
        
        print("You're currently in room {}.".format(player)) # fill with player coordinates
        print("You can move {}".format(', '.join(valid_moves))) # fill with available moves
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':
            print("\n ** Hah! Chicken! See you next time... dead or alive! **\n")
            break
        elif move in valid_moves:
            player = move_player(player, move)
            if monster == player:
                input("\n ** You met the monster in room {} and was eaten alive. You have lost. **".format(player))
                playing = False
            if door == player:
                input("You found the door at room {} and escaped, barely breathing in excitement and fear. \n But you're somehow alive. Congratulations. You won!".format(player))
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        play_again = input("Do you want to play again? [Y/n] ").lower()
        if play_again != 'n':
            game_loop()
        else:
            print("Okay, watch your back! Bye!")

clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
    
    # good move - change player position
    # bad move - don't change anything
    # on door - they win!
    # on monster - they lose!
    # otherwise loop back around


get_locations()