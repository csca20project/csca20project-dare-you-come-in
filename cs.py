import os

# constants
MAP_FILE = "map1.txt"
PLAYER_SYMBOL = "P"
EXIT_SYMBOL = "X"
BOMB_SYMBOL = "O"
WALL_SYMBOL = "#"

def create_map(file):
    '''Read the file and create a map list
    '''
    map_list = []
    for line in file:
        map_list.append(list(line.strip("\n")))
    return map_list
    

def display_map(map_list):
    '''Prints the map
    '''
    
    # clear shell
    print("\n" * 50)
    
    for r in range(len(map_list)):
        for c in range(len(map_list[r])):
            # hide the bomb from printing
            if map_list[r][c] == BOMB_SYMBOL:
                print(" ", end="")
            else:
                print(map_list[r][c], end="")
        print("")    


def find_position(map_list, symbol):
    '''find the row and column of the given symbol in the map
    '''
    for r in range(len(map_list)):
        for c in range(len(map_list[r])):
            if map_list[r][c] == symbol:
                return (r, c)


def next_position(move, r, c):
    '''Given the move (w, a, s, d), return the updated row and column
    '''
    
    new_r = r
    new_c = c
    
    if move == "w":
        new_r = new_r - 1
    elif move == "a":
        new_c = new_c - 1
    elif move == "s":
        new_r = new_r + 1
    elif move == "d":
        new_c = new_c + 1
        
    return (new_r, new_c)

def valid_move(move):
    if not (len(move) == 1 and move in "wasd"):
        print("Invalid Move entered, please enter one of w, a, s, or d")
        return False
    
    (new_Pr, new_Pc) = next_position(move, Pr, Pc)
    
    if map_list[new_Pr][new_Pc] == WALL_SYMBOL:
        print("Invalid Move, You are walking into a wall")
        return False
    
    return True
        
def make_move():
    move = input("Please enter a move (W A S D):").lower()
    while not valid_move(move):
        move = input("Please enter a move (W A S D):").lower()
    return move
    





# read the file, and create the map list
map_file = open(MAP_FILE, "r")
map_list = create_map(map_file)
map_file.close()

# player row and player column
Pr, Pc = find_position(map_list, PLAYER_SYMBOL)

dead = False
win = False

while not win and not dead:
    # display the map
    display_map(map_list)
    # ask for a move
    move = make_move()
    # get the new position
    new_Pr, new_Pc = next_position(move, Pr, Pc)
    
    # if the new position is a bomb, DEAD
    if map_list[new_Pr][new_Pc] == BOMB_SYMBOL:
        dead = True
    elif map_list[new_Pr][new_Pc] == EXIT_SYMBOL:
        win = True
    # update the map 
    map_list[new_Pr][new_Pc] = PLAYER_SYMBOL
    map_list[Pr][Pc] = " "
    
    # update player position
    Pr, Pc = new_Pr, new_Pc
    
display_map(map_list)
if win:
    print("Congradulation!!")
else:
    print("BOOOOOMM!!!!!!!!!!!!!!!")
    print("YOU DIED, SUCKER :)")    
    
