'''
Author: Nikhil Raval
Date: 11/14/23
Description: A Magic 8 Ball Game
Challenges: When using the commands to stop, it printed one of the items from the list
Bugs: none
Sources: Samantha Marciano, Nick Shklovsky


'''
import random #importing the package, random
responses = ["Yes", "I don't know", "Maybe", "Probably", "Probably not","No","100% yes", "100% no", "ask someone else"]#the list of responses
print("Welcome to the nobel prize winning 8 ball.")#the greeting

while True:
    question = input ("Ask me something.")#prompts user to ask a question
        
    if question == ("stop") or question == "i am done" or question == "done" or question == "no": #options to end the game
        print ("Ok. Thanks for playing. Come again!")#response to ending the game
        break

    print(random.choice(responses)) #prints any of the responses from the list, "responses" only when the if statement is false











