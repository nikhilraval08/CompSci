'''
Author: Nikhil Raval
Date: 11/27/23
Description: Rock, Paper, Scissors Game- allows users to play Rock, Paper, Scissors against a bot
Challenges: When the user printed "stop", it didn't stop the game immediately. It printed a response from the list then stopped. Another challenge was when the game got to 3 points, it didn't stop the game.
Bugs: none
Sources: Samantha Marciano, Eli Murphy
'''
import random #imports the package called random
rpslist = ["rock", "paper", "scissors"]#list, the options
score_p1 = 0 #the human's score, human's score starts at 0
score_bot = 0 #the bot's score, bot's score starts at 0

while True:
    if score_p1 >= 3: #if the human's score is 3 or greater, print "You won the round! Please run the program again for another round!"
        print ("You won the round! Please run the program again for another round!")
        break #stops repeating code
    elif score_bot >= 3: #if the bot's score is 3 or greater, print "You lost the round. Please run the program again for another round."
        print ("You lost the round. Please run the program again for another round.")
        break #stops repeating code

    rps = input ("(Enter stop to end, type in lowercase) First to 3! Rock! Paper! Scissors! ... Shoot!") #input that the user has to respond to, start of the game, round starts when human puts in Rock, Paper, or Scissors
    if rps == "stop": #if the response to the input is stop, it ends the game
        print ("Ok. Thanks for playing.") #action of printing the word "stop"
        break #stops repeating code

    bot = random.choice(rpslist)#how the bot chooses rock, paper or scissors. It chooses it randomly.
    print (bot)#prints the bot's choice

    if rps == ("rock") and bot == ("rock"): #if the human chose rock and the bot chose rock
        print ("It's a tie.") #prints this if the statement above is true
        print (f"The score is You- {score_p1} - Me- {score_bot}") #prints the score
    elif rps == ("rock") and bot == ("paper"): #if the human chose rock and the bot chose paper
        print ("You lost.") #prints this if that statement above is true
        score_bot += 1 #bot's score = +1 
        print (f"The score is You- {score_p1} - Me- {score_bot}") #prints the score
    elif rps == ("rock") and bot == ("scissors"): #if the human chose rock and the bot chose scissors
        print ("You won!") #prints this if the statement above is true
        score_p1 = score_p1+1 #human's score = +1
        print (f"The score is You- {score_p1} - Me- {score_bot}") #prints the score
    elif rps == ("paper") and bot == ("rock"): #if the human chose paper and the bot chose rock
        print ("You won!") #prints this of the statement above is true
        score_p1 = score_p1+1 #human's score = +1
        print (f"The score is You- {score_p1} - Me- {score_bot}") #prints the score
    elif rps == ("paper") and bot == ("paper"): #if the human chose paper and the bot chose paper
        print ("It's a tie.") #prints this if the statement above is true
        print (f"The score is You- {score_p1} - Me- {score_bot}") #prints the score
    elif rps == ("paper") and bot == ("scissors"): #if the human chose paper and the bot chose scissors
        print ("You lost.") #prints this if the statement above is true
        score_bot = score_bot+1 #bot's score = +1
        print (f"The score is You- {score_p1} - Me- {score_bot}") #prints the score
    elif rps == ("scissors") and bot == ("rock"): #if the human chose scissors and the bot chose rock
        print ("You lost.") #prints this if the statement above is true
        score_bot = score_bot+1 #bot's score = +1
        print (f"The score is You- {score_p1} - Me- {score_bot}") #prints the score
    elif rps == ("scissors") and bot == ("paper"): #if the human chose scissors and the bot chose paper
        print ("You won!") #prints this if the statement above is true 
        score_p1 = score_p1+1 #human's score = +1
        print (f"The score is You- {score_p1} - Me- {score_bot}")#prints the score
    elif rps == ("scissors") and bot == ("scissors"): #if the human chose scissors and the bot chose scissors
        print ("It's a tie.") #prints this if the statement above is true
        print (f"The score is You- {score_p1} - Me- {score_bot}") #prints the score
    else:
        print ("invalid") #prints this if the response to the input, rps, isn't rock, paper, scissors or stop- prints this even if it is uppercase
        
