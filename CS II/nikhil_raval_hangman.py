'''
 _____________________________________________________________________________________________________________________________________
|                                                                                                                                    |
|                                                               Hangman                                                              |
|____________________________________________________________________________________________________________________________________|
|   Name- Nikhil Raval                                                                                                               |
|   Description- Hangman game with a 25,002 word list                                                                                |
|   Bugs- none                                                                                                                       |
|   Features- keeps note of # of incorrect guesses left                                                                              |
|   Log- 1.0.0- submission                                                                                                           |
|   to easily test the code, use hangman_test_words.txt. This file has 6 words. If you want to use the list of words                 |
|   that has 25k words in it (hangman_words.txt), you will have to uncomment the command to open this file in the program.           |
|____________________________________________________________________________________________________________________________________|
                                
'''
import random 
#the stages of the hangman
hangman_pics = ['''              
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
#GREETS THE USER
def welcome():
    '''
    Args: 
        None

    Returns:
        Whether the user wants to play
    '''
    greeting = input ("Welcome to Hangman. Do you want to play? Y/N: ")
    if greeting == "y":
        play_game()                                               #starts the game                                                                       
    elif greeting == "Y":
        play_game()                                               #starts the game
    elif greeting == "n":
        print ("Ok, come again.")
        exit()                                                    #ends the game
    elif greeting == "N":
        print ("Ok, come again.")
        exit()                                                    #ends the game
    else:
        print ("Please enter Y or N.")
        welcome()                                                 #greets user again if answer is not y or n
#ASKS USER IF THEY WANT TO KEEP PLAYING
def play_more():
    '''
    Args: 
        None

    Returns:
        Whether the user wants to play again
    '''
    play_again = input ("Do you want to play again? Y/N: ")
    if play_again== "y":
        play_game()                                               #starts the game again
    elif play_again == "Y":
        play_game()                                               #starts the game again
    elif play_again == "n":
        print ("Ok, come again.")
        exit()                                                    #ends the game
    elif play_again == "N":
        print ("Ok, come again.")
        exit()                                                    #ends the game
    else:
        print ("Please enter Y or N.")
        play_more()                                               #if answer is not y or n, asks the user to answer it again
#STARTS THE GAME
def play_game():
    '''
    Args:
        None

    Returns:
        None
    '''
    print (hangman_pics [0])
    print ("Welcome to Hangman. Use letters A-Z.")
    print ("Please enjoy.")
    #my_file = open("hangman_words.txt","r")                       #opens the list of words- list with 20k words
    my_file = open("hangman_test_words.txt","r")                  #opens the list of words- for testing, has 6 words
    data = my_file.read()                                         #reads the list 
    words = data.split("\n")                                      #each new line is a new word
    secret = random.choice(words)                                 #chooses a random word from the list of words
    secret_list = list(secret)                                    #converts the secret word into a list of characters
    letters_chosen = []                                           #creates a list of the characters that are not in the word
    hidden = []                                                   #create an empty list to be used as a way for players to keep track of their guesses
    guesses = 0                                                   #variable to keep track of incorrect answers the player has made, # of incorrect guesses starts at 0
    guesses_left = 6                                              #how many incorrect guesses the user has left

    #adds to the hidden list such that the characters in the secret list line up with dashes to indicate the length of the word
    for character in secret_list:                                 #iterate through every element (character) in the list of the secret word's characters   
        if character == " ":                                      #if the character is a space
            hidden.append("  ")                                   #add two spaces to the hidden list to demonstrate that there are multiple words

        else:                                                     #otherwise
            hidden.append("_ ")                                   #add a dash and space to the hidden list to represent a character
    print("".join(hidden))                                        #converts the hidden list to a string, which is displayed by joining each character in its list
#DETRERMINES IF THE GUESS IS A LETTER
    while "_ " in hidden and guesses < len(hangman_pics) - 1:
        while True:
            guess = str.lower(input("Enter a letter: "))

            if guess not in list("abcdefghijklmnopqrstuvwxyz "):
                print ("Please enter a letter!")
            else:
                break
#DETERMINES IF THE GUESS IS IN THE WORD
        if guess in secret_list:
            for index in range (len(secret_list)):
                if guess == secret_list[index]:
                    hidden[index]= guess
            print("".join(hidden))
            
        else:
            print ("Not here!")
            #IF THE LETTER GUESSED HAS ALREADY BEEN GUESSED
            if guess in letters_chosen:
                print (hangman_pics[guesses])
                print ("You have already guessed this letter!")
                print (f"You have {guesses_left} guesses left")
                print ("Below are the letters you have guessed that are not in the word.")
                print (*letters_chosen, sep =', ')
                print("".join(hidden))
            else: 
                guesses += 1                                      #number of incorrect guesses increases by 1
                guesses_left -= 1                                 #number of guesses left decreases by 1
                print (hangman_pics[guesses])                     
                print (f"You have {guesses_left} guesses left")
                letters_chosen.append (guess)
                print ("Below are the letters you have guessed that are not in the word.")
                print (*letters_chosen, sep =', ')               
                print("".join(hidden))

#GAME OVER
    #IF USER LOST
    if "_ " in hidden or guesses == 6:                      
        print (f"You lost! The word was {secret}")                #prints the word
        play_more()                                               #asks user if they want to play again                                 
    #IF USER WON
    else:
        print("You won!")
        play_more()                                               #asks user if they want to play again

welcome()                                                         #starts program
