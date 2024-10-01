import random #imports the random module
score = 0 #starts the score at 0


while True:
    if score == int("5"): #if score is 5
        print ("You won!") #print this
        break #stops the code as game is over
        
    color_options = ["Red", "Blue", "Pink"] #list of colors
    color_answer = random.choice(color_options) #picks a random color out of the list of colors
    user_input = input ("Please guess a color. Red, Blue or Pink?") #asks user to pick a color
    
    if user_input == (color_answer): #if the user picked the correct answer
        print ("Correct") #print this
        score = score + 1 #adds up score
         
        print (score) #prints score

    elif user_input !=(color_answer): #if the user does not pick the correct answer
        print ("Sorry, wrong answer.") #prints this




