'''
Author: Nikhil Raval
Date: 11/6/23
Description: My Morning Routine- allows users to go through my Morning Routine
Challenges: Errors when coding while True loops, getting things to print a certain way
Bugs: none
Sources: Samantha Marciano, Eli Murphy, Oliver Davis
'''
print ("Alarm!") #prints the word Alarm


while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
    getup = input("Get up?: ") #input that the user has to respond to, asks the user ("Get up?")

    if getup == ("yes"): #the accepted response from the user to input (thing asked) 
        break #stops repeating code
    elif getup == "no": #the accepted response from the user to input (thing asked) 
        print ("Snooze") #the action caused by the user's response, prints (“snooze”) until getup == (“yes”)

    else:
        print("invalid") #prints this if the response is not “yes” or “no”

        
while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
    shower = input("Shower?") #input that the user has to respond to, asks the user (“Shower?”)

    if shower == ("yes"): #the accepted response from the user to input (thing asked) 
        print ("You are clean now.") #the action caused by the user's response, prints “You are clean now.”)
        break #stops repeating code
    elif shower == ("no"): #the accepted response from the user to input (thing asked) 
        print ("You are dirty.") #the action caused by the user's response, prints “You are dirty” until shower == (“yes”)
    else:
        print("invalid") #prints this if the response is not “yes” or “no”

        

while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
    getdressed = input ("Get dressed. Is it colder or warmer?") #input that the user has to respond to, asks the user ("Get dressed. Is it colder or warmer?")

    if getdressed == ("colder"): #the accepted response from the user to input (thing asked) 
        print ("Personally, I think you should dress heavier.") #the action caused by the user's response, prints (“Personally, I think you should dress heavier.”)

        while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
            dressheavier = input ("Do you want to dress heavier?") #input that the user has to respond to, asks the user ("Do you want to dress heavier?")

            if dressheavier == ("yes"): #the accepted response from the user to input (thing asked) 
                print ("Good choice.") #the action caused by the user's response, prints (“Good choice.”)
                break #stops repeating code
            elif dressheavier == ("no"):
                print ("You will suffer from hypothermia.") #the action caused by the user's response, prints (“You will suffer from hypothermia.”)
                break #stops repeating code

            else:
                print("invalid") #prints this if the response is not “yes” or “no”

        break #stops repeating code

    elif getdressed == ("warmer"): #the accepted response from the user to input (thing asked) 
        print ("Personally, I think you should dress lighter.") #the action caused by the user's response, prints (“Personally, I think you should dress lighter.”)

        while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
            dresslighter = input ("Do you want to dress lighter?") #input that the user has to respond to, asks the user ("Do you want to dress lighter?")

            if dresslighter == ("yes"): #the accepted response from the user to input (thing asked) 
                print ("Good choice.") #the action caused by the user's response, prints (“Good choice.”)
                break #stops repeating code
            elif dresslighter == ("no"): #the accepted response from the user to input (thing asked) 
                print ("You will suffer from heatstroke.") #the action caused by the user's response, prints (“You will suffer from heatstroke.”)
                break #stops repeating code
            else:
                print("invalid") #prints this if the response is not “yes” or “no”
        break #stops repeating code
               
    else:
        print("Invalid") #prints this if the response is not “yes” or “no”

    
print ("Pack Bag.") #prints the words Pack Bag
while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
    breakfast = input ("Eat breakfast. What do you want?") #input that the user has to respond to, asks the user ("Eat breakfast. What do you want?")
    if breakfast == ("bagel"): #the accepted response from the user to input (thing asked) 
        print ("Ok.") #the action caused by the user's response
        coffee = input ("Do you want coffee?") #input that the user has to respond to, asks the user ("Do you want coffee?")
        if coffee == ("yes"): #the accepted response from the user to input (thing asked) 
            print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
            break #stops repeating code
        elif coffee == ("no"): #the accepted response from the user to input (thing asked) 
            print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
            break #stops repeating code
    elif breakfast == ("peanut butter sandwich"): #the accepted response from the user to input (thing asked) 
        print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
        coffee = input ("Do you want coffee?") #input that the user has to respond to, asks the user ("Do you want coffee?")
        if coffee == ("yes"): #the accepted response from the user to input (thing asked) 
            print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
            break #stops repeating code
        elif coffee == ("no"): #the accepted response from the user to input (thing asked) 
            print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
            break #stops repeating code
    elif breakfast == ("eggs"): #the accepted response from the user to input (thing asked) 
        print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
        coffee = input ("Do you want coffee?") #input that the user has to respond to, asks the user ("Do you want coffee?")
        if coffee == ("yes"): #the accepted response from the user to input (thing asked) 
            print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
            break #stops repeating code
        elif coffee == ("no"): #the accepted response from the user to input (thing asked) 
            print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
            break #stops repeating code
        else:
            print ("Invalid") #prints this if the response is not “yes” or “no”
while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
    rain = input ("Is it raining?") #input that the user has to respond to, asks the user ("Is it raining?")
        
    if rain == ("yes"): #the accepted response from the user to input (thing asked) 
        print ("I think you should wear your workout sneakers and wear a raincoat.") #the action caused by the user's response, prints (“I think you should wear your workout sneakers and wear a raincoat.”)

        while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
            workoutclothes = input ("Do you want to wear your workout sneakers and a raincoat?") #input that the user has to respond to, asks the user ("Do you want to wear your workout sneakers and a raincoat?")
            if workoutclothes == ("yes"): #the accepted response from the user to input (thing asked) 
                print ("Good choice.") #the action caused by the user's response, prints (“Good choice.”)
                break #stops repeating code
            elif workoutclothes == ("no"): #the accepted response from the user to input (thing asked) 
                print ("You will ruin your shoes and will be very wet.") #the action caused by the user's response, prints (“You will ruin your shoes and be very wet.”) 
                break #stops repeating code
            else:
                print("invalid") #prints this if the response is not “yes” or “no”
        break #stops repeating code
    elif rain == ("no"): #the accepted response from the user to input (thing asked) 
        print ("You can wear nicer sneakers today.") #the action caused by the user's response, prints (“You can wear nicer sneakers today.”)

        
        while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
            sneakers = input ("Do you want to wear your nice sneakers?") #input that the user has to respond to, asks the user ("Do you want to wear your nice sneakers?")
            if sneakers == ("yes"): #the accepted response from the user to input (thing asked) 
                print ("Good choice.") #the action caused by the user's response, prints (“Good choice.”)
                break #stops repeating code
            elif sneakers == ("no"): #the accepted response from the user to input (thing asked) 
                print ("Ok. Wear whatever shoes you want.") #the action caused by the user's response, prints (“Ok. Wear whatever shoes you want.”)
                break #stops repeating code
            else:
                print("invalid") #prints this if the response is not “yes” or “no”
        break #stops repeating code
    else:
        print("Invalid") #prints this if the response is not “yes” or “no”

while True: #runs repeatedly until break (command that stops repeating code in a while true loop)
    workoutrain = input ("Are you working out today?") #input that the user has to respond to, asks the user ("Are you working out today?")

    if workoutrain==("no"): #the accepted response from the user to input (thing asked) 
        if rain == 'yes': #if this is true (this is a statement that has already been proved true/false)
            print ("Still wear workout sneakers.") #the action caused by if the statement is true, prints (“Still wear workout sneakers.”)

        elif rain == 'no': #if this is true (this is a statement that has already been proved true/false)
            print ("Wear whatever sneakers you want.") #the action caused by if the statement is true, prints (“Wear whatever sneakers you want.”)
        break #stops repeating code
    elif workoutrain == ("yes"): #the accepted response from the user to input (thing asked) 
        if rain == 'no': #if this is true (this is a statement that has already been proved true/false)
            print ("Wear workout sneakers.") #the action caused by if the statement is true, prints (“Wear workout sneakers.”)
            print ("Pack your gym bag.") #the action caused by if the statement is true, prints (“Pack your gym bag.”)
        elif rain == 'yes': #if this is true (this is a statement that has already been proved true/false)
            print ("Still wear workout sneakers.") #the action caused by if the statement is true, prints (“Still wear workout sneakers.”)
            print ("Pack your gym bag.") #the action caused by if the statement is true, prints (“Pack your gym bag.”)
        break #stops repeating code
    else:
        print("Invalid") #prints this if the response is not “yes” or “no”

while True:
    gotoschool = input ("Go to school?") #input that the user has to respond to, asks the user ("Go to school?")
    
    if gotoschool == ("yes"): #the accepted response from the user to input (thing asked) 
        print ("Have fun. See you when you get home. From, Your Indian Personal Assistant from Python.") #the action caused by the user's response, prints (“Have fun. See you when you get home. From, Your Indian Personal Assistant from Python.”)
        break #stops repeating code
    elif gotoschool == ("no"): #the accepted response from the user to input (thing asked) 
        print ("Ok.") #the action caused by the user's response, prints (“Ok.”)

        while True: #runs repeatedly until break (command that stops repeating code in a while true loop)  
            noschool = str.lower(input ("Why?")) #input that the user has to respond to, asks the user ("Why?")

            if noschool == ("i do not feel well"): #the accepted response from the user to input (thing asked) 
                print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
                break #stops repeating code
            elif noschool == ("no"): #the accepted response from the user to input (thing asked) 
                print ("I need more info.") #the action caused by the user's response, prints (“I need more info.”) and then repeats the input noschool until noschool == either of the accepted responses
            elif noschool == ("i do not want to"): #the accepted response from the user to input (thing asked) 
                print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
                break #stops repeating code
            else:
                print ("invalid") #prints this if the response is not “yes” or “no”
        break #stops repeating code
    else:
        print("Invalid") #prints this if the response is not “yes” or “no”


while True: #runs repeatedly until break (command that stops repeating code in a while true loop) 
    dontfeelwell = input ("Ask your mom or dad if you can stay home.") #input that the user has to respond to, asks the user ("Ask your mom or dad if you can stay home.")
    
    if dontfeelwell == ("ok"): #the accepted response from the user to input (thing asked) 
        print ("Tell me what they say.") #the action caused by the user's response, prints (“Tell me what they say.”)
        break #stops repeating code

    else:
        print ("invalid") #prints this if the response is not “yes” or “no”


while True: #runs repeatedly until break (command that stops repeating code in a while true loop) 
    parentsdecisiononstayinghome = input ("What did they say?") #input that the user has to respond to, asks the user ("What did they say?") 
    if parentsdecisiononstayinghome == ("yes"): #the accepted response from the user to input (thing asked) 
        print ("Ok. Email your teachers.") #the action caused by the user's response, prints (“Ok. Email your teachers.”)
        break #stops repeating code

    elif parentsdecisiononstayinghome == ("no"): #the accepted response from the user to input (thing asked) 
        print ("Ok.") #the action caused by the user's response, prints (“Ok.”)
        break #stops repeating code



while True: #runs repeatedly until break (command that stops repeating code in a while true loop) 
    convinceorgotoschool = input ("Convince them or go to school. Pick one.") #input that the user has to respond to, asks the user ("Convince them or go to school. Pick one.") 
    if convinceorgotoschool == ("go to school"): #the accepted response from the user to input (thing asked) 
        print ("Ok, hang in there. See you when you get home. From, Your Indian Personal Assistant from Python.") #the action caused by the user's response, prints (“Have fun. See you when you get home. From, Your Indian Personal Assistant from Python.”)
        break #stops repeating code
    elif convinceorgotoschool == ("Convince.") or ("Convince them."): #the accepted response from the user to input (thing asked) 
        print ("Good luck.") #the action caused by the user's response, prints (“Good luck.”)
        parentsdecisiononstayinghome = input ("What did they say?") #input that the user has to respond to, asks the user ("What did they say?") 

        if parentsdecisiononstayinghome == ("yes"): #the accepted response from the user to input (thing asked) 
            print ("Ok. Email your teachers.") #the action caused by the user's response, prints (“Ok. Email your teachers.”)
            break #stops repeating code
    
        elif parentsdecisiononstayinghome == ("no"): #the accepted response from the user to input (thing asked) 
            print ("Ok.") #the action caused by the user's response, prints (“Ok.”)

        else:
            print ("invalid") #prints this if the response is not “yes” or “no”

else:
    print ("invalid") #prints this if the response is not “yes” or “no”
