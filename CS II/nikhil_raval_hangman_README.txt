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
HOW TO PLAY:

When the program is ran, the user is asked if they want to play or not. They have to type Y or N. If they type y or Y, the game will run. If they type n or N, the game will end. 

When the game starts, the first hangman stage is printed, and the program randomly chooses a word from the 25k word list. The program will print a series of underscores
which is each character in the word. The user is then asked to enter a letter (a-z). If the letter is in the word, the letter will go in the matching characters. If the letter is 
not in the word, the program will add the letter to a list of characters that are not in the word, subtract one life, and print the corresponding hangman stage. The user has
6 lives. 

If the user guesses 6 letters incorrectly, the game ends, because they have lost 6 lives. The user has unlimited correct letter guesses. 

No matter if the user wins or loses, the user is asked if they want to play again. If the user types y or Y, the program runs again. If the user types n or N, the game quits. 

______________________________________________________________________________________________



