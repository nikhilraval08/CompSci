'''
____________________________________________________________________________________________________________________________________
|                                                                                                                                    |
|                                                            Battleship                                                              |
|____________________________________________________________________________________________________________________________________|
|   Name- Nikhil Raval                                                                                                               |
|   Description- Battleship game with a customizable board size and ship placement.                                                  |
|   Bugs- none                                                                                                                       |
|   Features- allows user to pick board size and guess placement, opponent's board is hidden, sound effects                          |
|   Log- 1.0.0- submission                                                                                                           |
|____________________________________________________________________________________________________________________________________|
'''
import random
import winsound

def welcome():
    '''
    Displays the welcome page and prompts the user to decide whether to play the game.

    Args:
        None

    Returns:
        None
    '''
    start_sequence = input ("Do you want to Play? Please type Yes or No.: ")

    try:
        if start_sequence == "Yes":
            print ("Let's Play.")
            start()                                                                                               #calls the function to start the game
        elif start_sequence == "yes":
            print ("Let's Play.")
            start()                                                                                               #calls the function to start the game
        elif start_sequence == "YES":
            print("Take a deep breath. Be calm.")
            welcome()
        elif start_sequence == "No":
            print ("Ok, come back again!")
            exit()                           
        elif start_sequence == "no":
            print ("Ok, come back again!")
            exit()                                                                                                 #exits the game
        elif start_sequence == "NO":
            print ("Come back when you are less riled up.")
            exit()
        else:
            print ("Please answer Yes or No.")
            welcome()    
    except:
        ValueError, SyntaxError, IndexError, TypeError                                                             #re-runs the welcome sequence if user does not answer input correctly
    
def start():
    '''
    starts the game by setting up the board size, ship numbers, and player boards, prompts players to prepare for the game.

    Args:
        None

    Returns:
        None
    '''
    bs = 0
    board_size = input("Please enter your board size. 4x4, 5x5,....10x10, or random (4-26): ")                     #asks user for board size
    if board_size == "4x4" or "4":
        bs = 16
        ship_number = 4                                                                                            #Number of ships to be placed on the board
        bs_number = 4                                                                                              #height, width of board
    elif board_size == "5x5" or "5":
        bs = 25
        ship_number = 5
        bs_number = 5                                                                                              #height, width of board
    elif board_size == "6x6" or "6":
        bs = 36
        ship_number = 6
        bs_number = 6                                                                                              #height, width of board
    elif board_size == "7x7" or "7":
        bs = 49
        ship_number = 7
        bs_number = 7                                                                                              #height, width of board
    elif board_size == "8x8" or "8":
        bs = 64
        ship_number = 8
        bs_number = 8                                                                                              #height, width of board
    elif board_size == "9x9" or "9":
        bs = 81
        ship_number = 9
        bs_number = 9
    elif board_size == "10x10" or "10":
        bs = 100
        ship_number = 10
        bs_number = 10                                                                                             #height, width of board
    elif board_size == "random":
        bs_number = random.randint(4,26)                                                                           #Randomly choose a number between 4 and 26 for the board size
        ship_number = bs_number                                                                                    #Number of ships to be placed on the board
        bs = bs_number * bs_number                                                                                 #Calculate the board size by squaring the random number
    else:
        print("Please enter a valid size.")
        start()                                                                                                    #re-runs the start sequence if user does not answer input correctly

                                                                                                                   #Initialize ship and player boards for both players
    ship_board_p1 = [" " for x in range(bs)]
    ship_board_p2 = [" " for x in range(bs)] 
    guess_board_p1 = [" " for x in range(bs)]
    guess_board_p2 = [" " for x in range(bs)]
   
    
    print("Welcome! Each player has two boards. One for their ships and one for their guesses. During each turn, the player will only see their boards. The coordinate system is just like Excel--ABCDE.. is the X axis, 12345.. is the Y axis, and the coordinates are letter# (A1, B4) format.")
    print(f"The program will randomly assign the {ship_number} ship locations as the board size is {int(bs)**0.5} x {int(bs)**0.5}.")
    print("\n" * 2)
    rules = input("Please give the machine to Player 1 and press Enter to continue.")
    while True:
        if rules == "":
            break                                                                                                  #Exit the loop if Player 1 is ready
        else:
            print("Please press enter.")
            rules = input("Please give the machine to Player 1 and press Enter to continue.")
    
    icon =  'S'
                                                                                                                   #calls the function to assign ship coordinates for player 1 and player 2
    assign_ship_coords_p1(icon, ship_board_p1, bs, ship_number)
    assign_ship_coords_p2(icon, ship_board_p2, bs, ship_number)                                                    #calls the function to create the ship board for player 1 and player 2
    create_ship_board_player_1(ship_board_p1)

                                                                                                                   #After creating player 1's ship board, prompt to hand over to player 2
    print("Your ship board has been made.")
    p2_go = input("Press Enter when Player 2 is ready.")
    while True:
        if p2_go == "":
            break                                                                                                  #Exit the loop if Player 2 is ready
        else:
            print("Please press enter.")
            p2_go = input("Press Enter when Player 2 is ready.")
                                                                                                                   #Add 1000 new lines to hide Player 1's board
    print("\n" * 1000)
       
    p2_verify = input("Enter if you are Player 2.")
    while True:
        if p2_verify == "":
            break                                                                                                  #Exit the loop if Player 2 is ready
        else:
            print("Please press enter.")
            p2_verify = input("Enter if you are Player 2.")     
                                                                                                                   #creates Player 2's ship board
    create_ship_board_player_2(ship_board_p2)
    
    play(ship_board_p1, ship_board_p2, guess_board_p1, guess_board_p2, bs_number)                                  #Calls the play function to start gameplay

def play(ship_board_p1, ship_board_p2, guess_board_p1, guess_board_p2, bs_number):
    '''
    the actual gameplay, players take turns guessing coordinates and updates their boards

    Args:
        ship_board_p1: Player 1's ship board.
        ship_board_p2: Player 2's ship board.
        guess_board_p1: Player 1's guess board.
        guess_board_p2: Player 2's guess board.
        bs_number: Integer representing the size of the board (number of rows/columns).

    Returns:
        None
    '''
    while True:
        if  'S' not in ship_board_p2:                                                                              #Check if Player 2's ships are all hit
            print("Player 1 wins!")
            break      
        
        elif  'S' not in ship_board_p1:
            print("Player 2 wins!")                                                                                #Exit the loop if Player 2 wins
            break

        else:
            pass                                                                                                       
                                                                                                                  
        p1_go = input("Press Enter when Player 1 is ready to play.")
        while True:
            if p1_go == "":
                break
            else:
                print("Please press enter.")
                                           
                p1_go = input("Press Enter when Player 1 is ready to play.")                                           
        print("\n" * 1000)                                                                                         #Add 1000 new lines to hide Player 1's board
        p1_verify = input("Enter if you are Player 1.")
        while True:
            if p1_verify == "":
                break                                                                                              #Exit the loop if Player 1 is ready
            else:
                print("Please press enter.")
                p1_verify = input("Enter if you are Player 1.")                                                    #Prompt for Player 1 to enter
                                                                                                                   #Add 1000 new lines to hide Player 2's board
        print("\n" * 1000)
        print("Player 1's Ship Board:")
        create_ship_board_player_1(ship_board_p1)
        print("Player 1's Guess Board:")
        create_guess_board_player_1(guess_board_p1)
        coord_selection = input("Player 1, please enter your guess: ")
        index = choose_coords(coord_selection, bs_number)
        place_guess(ship_board_p2, guess_board_p1, index, 'H' if ship_board_p2[index] ==  'S' else  'M')
        if ship_board_p2[index] == "H":
            winsound.PlaySound("hit.wav", winsound.SND_FILENAME)                                                   #Play sound if hit
        elif ship_board_p2[index] == "M":
            winsound.PlaySound("miss.wav", winsound.SND_FILENAME)
                                                                                            
        p2_go = input("Press Enter when Player 2 is ready to play.")
        while True:
            if p2_go == "":
                break                                                                                              #Exit the loop if Player 2 is ready
            else:
                print("Please press enter.")
                p2_go = input("Press Enter when Player 2 is ready to play.")
                                                                                                                   #Add 1000 new lines to hide Player 1's board
        print("\n" * 1000)
        p2_verify = input("Enter if you are Player 2.")
        while True:
            if p2_verify == "":
                break
            else:
                print("Please press enter.")
                p2_verify = input("Enter if you are Player 2.")
        print("\n" * 1000)
        print("Player 2's Ship Board:")
        create_ship_board_player_2(ship_board_p2)
        print("Player 2's Guess Board:")
        create_guess_board_player_2(guess_board_p2)
        coord_selection = input("Player 2, please enter your guess: ")
        index = choose_coords(coord_selection, bs_number)
        place_guess(ship_board_p1, guess_board_p2, index, 'H' if ship_board_p1[index] ==  'S' else  'M')
        if ship_board_p1[index] == "H":
            winsound.PlaySound("hit.wav", winsound.SND_FILENAME)                                                   #Play sound if hit
        elif ship_board_p1[index] == "M":
            winsound.PlaySound("miss.wav", winsound.SND_FILENAME)

def create_ship_board_player_1(ship_board_p1):
    '''
    Displays Player 1's ship board with row and column labels.

    Args:
        ship_board_p1: Player 1's ship board.

    Returns:
        None
    '''
                                                                                                                                                                            #Column labels
    column_labels = "     " + "     ".join(chr(65 + i) for i in range(len(ship_board_p1) // int(len(ship_board_p1)**0.5)))
    print(column_labels)

                                                                                                                                                                            #Generate rows with row labels
    size = int(len(ship_board_p1)**0.5)                                                                                                                                     #Calculate the size of the board (square root of bs)
    rows = ["{:>2} | ".format(i + 1) + " | ".join("{:^3}".format(ship_board_p1[i * size + j]) for j in range(size)) + " |" for i in range(size)]

                                                                                                                                                                            #Print the rows to display the grid
    print("\n".join(rows) + "\n")

def create_guess_board_player_1(guess_board_p1):
    '''
    Displays Player 1's guess board with row and column labels.

    Args:
        guess_board_p1: Player 1's guess board.

    Returns:
        None
    '''
                                                                                                                                                                            #Column labels
    column_labels = "     " + "     ".join(chr(65 + i) for i in range(len(guess_board_p1) // int(len(guess_board_p1)**0.5)))
    print(column_labels)

                                                                                                                                                                            #Generate rows with row labels
    size = int(len(guess_board_p1)**0.5)                                                                                                                                    #Calculate the size of the board (square root of bs)
    rows = ["{:>2} | ".format(i + 1) + " | ".join("{:^3}".format(guess_board_p1[i * size + j]) for j in range(size)) + " |" for i in range(size)]
                                                                                                                                                                            #Print the rows to display the grid
    print("\n".join(rows) + "\n")

def create_ship_board_player_2(ship_board_p2):
    '''
    Displays Player 2's ship board with row and column labels.

    Args:
        ship_board_p2: Player 2's ship board.

    Returns:
        None
    '''
                                                                                                                                                                            #Column labels
    column_labels = "     " + "     ".join(chr(65 + i) for i in range(len(ship_board_p2) // int(len(ship_board_p2)**0.5)))
    print(column_labels)

                                                                                                                                                                            #Generate rows with row labels
    size = int(len(ship_board_p2)**0.5)                                                                                                                                     #Calculate the size of the board (square root of bs)
    rows = ["{:>2} | ".format(i + 1) + " | ".join("{:^3}".format(ship_board_p2[i * size + j]) for j in range(size)) + " |" for i in range(size)]

                                                                                                                                                                            #Print the rows to display the grid
    print("\n".join(rows) + "\n")

def create_guess_board_player_2(guess_board_p2):
    '''
    Displays Player 2's guess board with row and column labels.

    Args:
        guess_board_p2: Player 2's guess board.

    Returns:
        None
    '''
                                                                                                                                                                            #Column labels
    column_labels = "     " + "     ".join(chr(65 + i) for i in range(len(guess_board_p2) // int(len(guess_board_p2)**0.5)))
    print(column_labels)

                                                                                                                                                                            #Generate rows with row labels
    size = int(len(guess_board_p2)**0.5)                                                                                                                                    #Calculate the size of the board (square root of bs)
    rows = ["{:>2} | ".format(i + 1) + " | ".join("{:^3}".format(guess_board_p2[i * size + j]) for j in range(size)) + " |" for i in range(size)]

                                                                                                                                                                            #Print the rows to display the grid
    print("\n".join(rows) + "\n")

def assign_ship_coords_p1(icon, ship_board_p1, bs, ship_number):
    '''
    Randomly assigns ship coordinates for Player 1.

    Args:
        icon: String representing the ship icon.
        ship_board_p1: Player 1's ship board.
        bs: number of spots on the board. 4x4 = 16, 5x5 = 25, 6x6 = 36, 7x7 = 49, 8x8 = 64, 9x9 = 81, 10x10 = 100, random (4-26) = 16-676
        ship_number: the number of ships to place, which is equal to bs_number.


    Returns:
        Updated ship_board_p1 with ships placed.
    '''
    for _ in range(ship_number):                                                                                                                                            #Loop to place [ship_number] amount of ships
        while True:
            index = random.randint(0, bs-1)                                                                                                                                 #Randomly choose an index between 0 and board spots - 1
            if ship_board_p1[index] == " ":                                                                                                                                 #Check if the randomly chosen spot is empty
                ship_board_p1[index] = icon                                                                                                                                 #Place the ship icon at the chosen spot
                break                                                                                                                                                       #Exit the loop once a ship is placed
    if  'S' not in ship_board_p1:                                                                                                                                           #Check if Player 2's ships are all hit
        print("Player 2 wins!")                                                                                                                                             #Notify Player 1 wins
        return ship_board_p1
        exit()
    else:
        pass   
        return ship_board_p1                                                                                                                                                #Return the updated ship board

def assign_ship_coords_p2(icon, ship_board_p2, bs, ship_number):
    '''
    Randomly assigns ship coordinates for Player 2.

    Args:
       icon: String representing the ship icon.
        ship_board_p2: Player 2's ship board.
        bs: number of spots on the board. 4x4 = 16, 5x5 = 25, 6x6 = 36, 7x7 = 49, 8x8 = 64, 9x9 = 81, 10x10 = 100, random (4-26) = 16-676
        ship_number: the number of ships to place, which is equal to bs_number.

    Returns:
        Updated ship_board_p2 with ships placed.
    '''
    for _ in range(ship_number):                                                                                                                                            #Loop to place [ship_number] amount of ships
        while True:
            index = random.randint(0, bs-1)                                                                                                                                 #Randomly choose an index between 0 and board spots - 1
            if ship_board_p2[index] == " ":                                                                                                                                 #Check if the randomly chosen spot is empty
                ship_board_p2[index] = icon                                                                                                                                 #Place the ship icon at the chosen spot
                break                                                                                                                                                       #Exit the loop once a ship is placed
    if  'S' not in ship_board_p2:                                                                                                                                           #Check if Player 2's ships are all hit
        print("Player 1 wins!")                                                                                                                                             #Notify Player 1 wins
        return ship_board_p2
        exit()
    else:
        pass 
    return ship_board_p2                                                                                                                                                    #Return the updated ship board

def choose_coords(coord_selection, bs_number):
    '''
    Validates and converts player input into a valid board index.

    Args:
        coord_selection: player's coordinate selection (e.g., "A1", "B2").
        bs_number: Integer representing the size of the board (number of rows/columns).

    Returns:
        Integer representing the valid coordinate index.
    '''
    while True:
        coord = coord_selection                                                                                                                                             #player input for coordinates
        coord = coord.upper()                                                                                                                                               #Convert input to uppercase for consistency
        if len(coord) == 2 and coord[0] in [chr(65 + i) for i in range(bs_number)] and coord[1].isdigit() and 1 <= int(coord[1]) <= bs_number:
            col = ord(coord[0]) - ord('A')                                                                                                                                  #Convert column letter to index
            row = int(coord[1]) - 1                                                                                                                                         #Convert row number to index
            return row * bs_number + col                                                                                                                                    
        elif coord == "":
            print("Invalid input. Try again.")                                                                                                                              #Prompt again if input is invalid
            coord_selection = input("Please enter a new guess: ")                                                                                                           #Prompt for a new guess
            continue
        else:
            print("Invalid input. Try again.")                                                                                                                              #Prompt again if input is invalid
            coord_selection = input("Please enter a new guess: ")                                                                                                           #Prompt for a new guess
            continue                                                                                                                                                        #Use continue to recheck the while loop

def place_guess(ship_board, guess_board, index, icon):
    '''
    Places a player's guess on the opponent's ship board and updates the guess board.

    Args:
        ship_board: the opponent's ship board.
        guess_board: the player's guess board.
        index:  the index where the guess will be placed.
        icon: the icon to place ('H' for hit, 'M' for miss).

    Returns:
        Updated ship_board with the guess placed.
    '''
    while True:                                                                                                                                                             #Loop until a valid guess is made
        if ship_board[index] ==  'S':                                                                                                                                       #Check if the spot contains a ship
            ship_board[index] = 'H'                                                                                                                                         #Mark as a hit on the opponent's ship board
            guess_board[index] = 'H'                                                                                                                                        #Mark as a hit on the player's guess board
            print("It's a hit!")
            break
        elif ship_board[index] == " ":                                                                                                                                      #Check if the spot is empty
            ship_board[index] =  'M'                                                                                                                                        #Mark as a miss on the opponent's ship board
            guess_board[index] =  'M'                                                                                                                                       #Mark as a miss on the player's guess board
            print("It's a miss.")
            break
        else:
            print("Spot already guessed. Try again.")                                                                                                                       #Notify player if spot is already guessed
            coord_selection = input("Please enter a new guess: ")                                                                                                           #Prompt for a new guess
            index = choose_coords(coord_selection)                                                                                                                          #Recalculate the index for the new guess

    print("\nYour Guess Board:")
    create_guess_board_player_1(guess_board)                                                                                                                                #Replace with the correct function for the current player

    return ship_board                                                                                                                                                       #Return the updated ship board


welcome()                                                                                                                                                                   #Call the welcome function to start the game