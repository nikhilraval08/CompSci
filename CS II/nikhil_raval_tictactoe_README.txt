#Name- Nikhil Raval
#Description- Tic-Tac-Toe for Python 
#Bugs- excepts do not work, breaks when choice is NOT 0-9 (ex- letters, integers over 9), ***when space is taken, turn is forfeited
#Features- users can play against a bot or with a friend
#Log- 1.0.0- submission
_____________________________________________________________________________________________________________________________________

HOW TO USE:

When ran, the user is prompted with a Welcome message on the Welcome page, which asks them if they want to play or if they don't want to play (anymore). If the user responds "Yes", the user will be sent to the Start Sequence.

Once in the Start Sequence, the user is asked to say how many players there are. 1 Player (played against a bot) or 2 Players (playing with a friend). Once responded, they will be sent to play.

If the user chose 1 player, they will be playing against a bot. The program will ask Player 1 (the user), who is X to enter a number 1-9. Once entered, it is then the bot's turn. To get the bot to choose a spot, the user will have to 
type 0. When 0 is typed, the bot will randomly choose a number 1-9, and O will go to that space. If the space is empty, X or O (depending on whose turn it is) will go there. If the space is taken, the user will be alerted. 
There is a bug regarding this. *** 

The game will go on until a player has won or there is a draw. If a player won or there is a draw, the program will announce it. Once that happens, the user is sent back to the Welcome page to play again. If they want to play, they
type "Yes". If they don't want to play again, they type "No", and the program quits. 

_____________________________________________________________________________________________________________________________________