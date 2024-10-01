import random #imports the package, random, to use the functions inside the package
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
print ("Welcome to Hangman. Use letters A-Z, and if needed, use -")
print ("Please enjoy.")
my_file = open("words.txt","r")
data = my_file.read()
words = data.split("\n")
secret = random.choice(words)       #chooses a random word from the list of words
secret_list = list(secret)          #converts the secret word into a list by splicing the characters
hidden = []                         #create an empty list to be used as a way for players to keep track of their guesses
guesses = 0                         #variable to keep track of incorrect answers the player has made, # of incorrect guesses starts at 0

#adds to the hidden list such that the characters in the secret list line up with dashes to indicate the length of the word
for character in secret_list:       #iterate through every element (character) in the list of the secret word's characters   
    if character == " ":            #if the character is a space
        hidden.append("  ")         #add two spaces to the hidden list to demonstrate that there are multiple words
    else:                           #otherwise
        hidden.append("_ ")         #add a dash and space to the hidden list to represent a character
print("".join(hidden))              #converts the hidden list to a string, which is displayerd, by joining each character in its list

while "_ " in hidden and guesses < len(hangman_pics) - 1:
    while True:
        guess = str.lower(input("Enter a letter: "))

        if guess not in list("abcdefghijklmnopqrstuvwxyz- "):
            print ("Please enter a letter!")
        else:
            break

    if guess in secret_list:
        for index in range (len(secret_list)):
            if guess == secret_list[index]:
                hidden[index]= guess
        print("".join(hidden))
    else:
        print ("Not here!")
        guesses += 1
        print (hangman_pics[guesses])

if "_ " in hidden:
    print (f"You lost! The word was {secret}")
else:
    print("You won!")


        


