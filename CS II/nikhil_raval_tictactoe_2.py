#Name- Nikhil Raval
#Description- Tic-Tac-Toe for Python 
#Bugs- excepts do not work, breaks when choice is NOT 0-9 (ex- letters, integers over 9), when space is taken, turn is forfeited
#Features- users can play against a bot or with a friend
#Log- 1.0.0- submission
import random
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]                                                       #Spots for the bot to randomly choose
def welcome():
    '''
    The Welcome Page to the game. Asks the user if they want to play or don't want to (anymore)

    Args:
        None

    Returns:
        User's decision to play or not
    '''
    start_sequence = input ("Do you want to Play Tic-Tac-Toe? Please type Yes or No.: ")

    if start_sequence == "Yes":
        print ("Let's Play.")
        start()                                                                                                #calls the function to start the game
    elif start_sequence == "yes":
        print ("Let's Play.")
        start()                                                                                                #calls the function to start the game
    elif start_sequence == "No":
        print ("Ok, come back again!")
        exit()                           
    elif start_sequence == "no":
        print ("Ok, come back again!")
        exit()                                                                                                 #exits the game
    else:
        print ("Please answer Yes or No.")
        welcome()                                                                                              #re-runs the welcome sequence if user does not answer input correctly
    
def start():
    '''
    The Start of the Game. User is asked how many players, answer sends them to play
    
    Args:
        None

    Returns:
        None
    '''
    player_number = input ("How many players? 1 (playing against a bot) or 2 (with a friend)?: ")
    
    try:
        if player_number == "1":
            play_against_bot()                                                                                     #sends user to play against a bot
    
        elif player_number == "2":
            play_with_friend()                                                                                     #sends user to play with a friend
    except SyntaxError or ValueError or TypeError:
        print ("Please enter 1 or 2.")
        start()

def play_against_bot():
    '''
    Playing the game (1 player, against bot)
    
    Args:
        None
    
    Returns:
        None
    '''
    playing_grid = [" " for x in range(9)]                                                                     #creates board, has 9 spaces

    def print_playing_grid():
        '''
        creates the layout of the board

        Args:
            None

        Returns:
            None 
        '''
        #LAYOUT OF THE BOARD, 3 BY 3 GRID, EACH SPACE CORRESPONDS TO AN INDEX IN THE GRID 
        row1 = "| {} | {} | {} |".format(playing_grid[0], playing_grid[1], playing_grid[2])
        row2 = "| {} | {} | {} |".format(playing_grid[3], playing_grid[4], playing_grid[5])
        row3 = "| {} | {} | {} |".format(playing_grid[6], playing_grid[7], playing_grid[8])


        print()
        print(row1)
        print(row2)
        print(row3)
        print()
    def player_move(icon):
        '''
        the playing portion

        Args:
            icon- "X" or "O"

        Returns:
            place to put "X" or "O" in
        '''
        if icon == "X":
            player = 1
        elif icon == "O":
            player = 2
        print("Your turn player {}".format(player))
    
        choice = int(input("Enter your move (1-9) If it is Player 2's turn, type 0: ").strip())                #asks user to enter their move
        try:
            #######FOR THE BOT ONLY########
            if choice == 0:
                bot = random.choice(numbers)                                                                       #bot chooses a number from 1-9 from numbers (top of program, line 7)
                choice = int(bot)                                                                                  #bot's choice is turned into an integer which is entered into choice (line 97)
            ###############################
        except:
            pass
        try:
            if playing_grid[choice - 1] == " ":                                                                    #if player's spot is blank
                playing_grid[choice - 1] = icon                                                                    #enter it
        
        except ValueError or IndexError or TypeError or SyntaxError:                                               #reruns function if program runs into these errors
            play_against_bot()
            
    
        else:
            print()
            print("That space is already taken!")                                                               #tells player that spot is full
    def is_victory(icon):
        '''
        checks who won
        
        Args:
            icon- "X" or "O"
        
        Returns:
            True (if icon is in any of those spots) or False 
        '''
        if (playing_grid[0] == icon and playing_grid[1] == icon and playing_grid[2] == icon) or \
        (playing_grid[3] == icon and playing_grid[4] == icon and playing_grid[5] == icon) or \
        (playing_grid[6] == icon and playing_grid[7] == icon and playing_grid[8] == icon) or \
        (playing_grid[0] == icon and playing_grid[3] == icon and playing_grid[6] == icon) or \
        (playing_grid[1] == icon and playing_grid[4] == icon and playing_grid[7] == icon) or \
        (playing_grid[2] == icon and playing_grid[5] == icon and playing_grid[8] == icon) or \
        (playing_grid[0] == icon and playing_grid[4] == icon and playing_grid[8] == icon) or \
                (playing_grid[2] == icon and playing_grid[4] == icon and playing_grid[6] == icon):              #line 137- horizontal row 1
                                                                                                                #line 138- horizontal row 2
                                                                                                                #line 139- horizontal row 3
                                                                                                                #line 140- vertical column 1
                                                                                                                #line 141- vertical column 2
                                                                                                                #line 142- vertical column 3
                                                                                                                #line 143- diag top left to bottom right
                                                                                                                #line 144- diag top right to bottom left
            return True
        else:
            return False    
    def is_draw():
        '''
        checks if there is a draw

        Args:
            if all spaces are full

        Returns:
            True or False
        '''
        if " " not in playing_grid:                                                                             #if all spaces ar full/there is no blanks on the grid 
            return True                                                                                         #return True/is a draw                    
        else:
            return False                                                                                        #returns False/no draw
    #LOOPS UNTIL A PLAYER HAS WON OR A DRAW HAS BEEN CALLED
    while True:
        print_playing_grid()
        player_move("X")
        print_playing_grid()
        #IF PLAYER 1 (X) WINS
        if is_victory("X"):
            print("X wins! Congratulations!")
            welcome()                                                                                           #game runs again
        elif is_draw():
            print("It's a draw!")
            welcome()                                                                                           #game runs again
        #IF PLAYER 2 (O, THE BOT) WINS
        player_move("O")
        if is_victory("O"):
            print_playing_grid()
            print("O wins! Congratulations!")
            welcome()                                                                                           #game runs again
        elif is_draw():
            print("It's a draw!")
            welcome()                                                                                           #game runs again
    
def play_with_friend():
    '''
    Playing the game (2 player, human vs. human)
    
    Args:
        None
    
    Returns:
        None
    '''
    playing_grid = [" " for x in range(9)]                                                                     #creates board, has 9 spaces

    def print_playing_grid():
        #LAYOUT OF THE BOARD, 3 BY 3 GRID, EACH SPACE CORRESPONDS TO AN INDEX IN THE GRID 
        row1 = "| {} | {} | {} |".format(playing_grid[0], playing_grid[1], playing_grid[2])
        row2 = "| {} | {} | {} |".format(playing_grid[3], playing_grid[4], playing_grid[5])
        row3 = "| {} | {} | {} |".format(playing_grid[6], playing_grid[7], playing_grid[8])


        print()
        print(row1)
        print(row2)
        print(row3)
        print()
    def player_move(icon):
        '''
        the playing portion

        Args:
            icon- "X" or "O"

        Returns:
            place to put "X" or "O" in
        '''
        if icon == "X":
            player = 1
        elif icon == "O":
            player = 2
        print("Your turn player {}".format(player))                                     
        choice = int(input("Enter your move (1-9): ").strip())                                              #asks user to enter their move
        try:
            if playing_grid[choice - 1] == " ":                                                             #if player's spot is blank
                playing_grid[choice - 1] = icon                                                             #enter it
        
        except ValueError or IndexError or TypeError or SyntaxError:                                        #reruns function if program runs into these errors
            play_against_bot()
        else:
            print()
            print("That space is already taken!")                                                           #tells player that spot is full
    def is_victory(icon):
        '''
        checks who won
        
        Args:
            icon- "X" or "O"
        
        Returns:
            True (if icon is in any of those spots) or False 
        '''
        if (playing_grid[0] == icon and playing_grid[1] == icon and playing_grid[2] == icon) or \
        (playing_grid[3] == icon and playing_grid[4] == icon and playing_grid[5] == icon) or \
        (playing_grid[6] == icon and playing_grid[7] == icon and playing_grid[8] == icon) or \
        (playing_grid[0] == icon and playing_grid[3] == icon and playing_grid[6] == icon) or \
        (playing_grid[1] == icon and playing_grid[4] == icon and playing_grid[7] == icon) or \
        (playing_grid[2] == icon and playing_grid[5] == icon and playing_grid[8] == icon) or \
        (playing_grid[0] == icon and playing_grid[4] == icon and playing_grid[8] == icon) or \
        (playing_grid[2] == icon and playing_grid[4] == icon and playing_grid[6] == icon):                      #line 250- horizontal row 1
                                                                                                                #line 251- horizontal row 2
                                                                                                                #line 252- horizontal row 3
                                                                                                                #line 253- vertical column 1
                                                                                                                #line 254- vertical column 2
                                                                                                                #line 255- vertical column 3
                                                                                                                #line 256- diag top left to bottom right
                                                                                                                #line 257- diag top right to bottom left
            return True
        else:
            return False      
    def is_draw():
        '''
        checks if there is a draw

        Args:
            if all spaces are full

        Returns:
            True or False
        '''
        if " " not in playing_grid:                                                                            #if all spaces ar full/there is no blanks on the grid 
            return True                                                                                        #return True/is a draw
        else:
            return False                                                                                       #returns False/no draw
    #LOOPS UNTIL A PLAYER HAS WON OR A DRAW HAS BEEN CALLED
    while True:
        print_playing_grid()
        player_move("X")
        print_playing_grid()
        #IF PLAYER 1 (X) WINS
        if is_victory("X"):
            print("X wins! Congratulations!")
            welcome()                                                                                          #game runs again
        elif is_draw():
            print("It's a draw!")
            welcome()                                                                                          #game runs again
        #IF PLAYER 2 (O) WINS
        player_move("O")
        if is_victory("O"):
            print_playing_grid()
            print("O wins! Congratulations!")
            welcome()                                                                                          #game runs again
        elif is_draw():
            print("It's a draw!")
            welcome()                                                                                          #game runs again

welcome()                                                                                                      #starts the whole program