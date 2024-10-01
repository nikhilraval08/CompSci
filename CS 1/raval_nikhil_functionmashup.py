'''
Author- Nikhil Raval
Date- 4/18/24
Description- Function Mashup, a program that does many different things
Bugs- none
Sources- Diego Abanto, Samantha Marciano
Challenges- frustration with errors and frustration with not knowing how to code a specific function, #s 4 and 6
'''
import random #imports the random library
#1
def chorus(): #defines the function, chorus, which is the chorus of the song
    print ("I shot the sheriff")
    print ("But I didn't shoot no deputy")
    print ("Oh, no, oh")
    print ("I shot the sheriff")
    print ("But I didn't shoot no deputy")
    print ("ooh, ooh, ooh")
def sing_song(): #defines the function, sing_song, which makes python sing
    chorus() #calls the chorus function
    print ("Yeah, all around in my home town")
    print ("They're trying to track me down, yeah")
    print ("They say they want to bring me in guilty")
    print ("For the killing of a deputy")
    print ("For the life of a deputy")
    print ("But I say")
    print ("Oh, now, now, oh")
    print ("I shot the sheriff, the sheriff")
    print ("But I swear it was in self-defense, oh no")
    print ("Ooh, ooh, ooh, yeah")
    print ("I say, I shot the sherriff, oh Lord")
    print ("And they say it is a capital offense, yeah")
    print ("Ooh, ooh, ooh, yeah")
    print ("Sheriff John Brown always hated me")
    print ("For what, I don't know")
    print ("Every time I plant a seed")
    print ("He said kill it before it grow")
    print ("He said kill them before they grow")
    print ("And so, and so")
    print ("Read it in the news")
    print ("I shot the sheriff, oh Lord")
    print ("But I swear it was in self-defense")
    print ("Where was the deputy? Ooh, ooh, ooh")
    print ("I say, I shot the sheriff")
    print ("But I swear it was in self-defense, yeah")
    print ("Ooh-ooh")
    print ("Freedom came my way one day")
    print ("And I started out of town, yeah")
    print ("All of a sudden I saw Sheriff John Brown")
    print ("Aiming to shoot me down")
    print ("So I shot, I shot, I shot him down and I say")
    print ("If I am guilty I will pay (pay, pay, pay, pay, pay")
    chorus () #calls the chorus function
#2
def add (num1, num2): #defines add, the function that adds two numbers together
    print(num1+num2) #prints the sum
#3
def print_list(list_to_print): #defines the function to print a list
    for element in list_to_print: #for each item in the list
        print(element) #print the item
#4
def contains_element(my_list, element): #defines the function to see if the item is in the list
    return element in my_list #gives back the element
#5
def is_number_integer (integer): #defines the function that determines if a number is an integer
    if integer.isnumeric(): #if the integer is a number
        return True #says it is true, is a number
    else: 
        return False #says it is false, not a number
#6
def random_nmber(): #defines the random number function
    while True: #if this is true
        num3 = input("Player, please enter your first number.") #asks the user to enter the first number
        num4 = input("Player, please enter your second number.") #asks the user to enter the second number
        if is_number_integer(num3) and is_number_integer(num4): #uses the function from #5 to see if the numbers that the user entered is a number
            print(random.randint(int(num3), int(num4)))#randomly chooses one of the two numbers that the user entered
            break
        else:
            print("Please enter a number, please.") #prints this if the user did not imput a number
#7
def replace_character(string, old_character,new_character): #defines the function that replaces letters in a sentence
    new_string = " " #the new sentence
    for s in string : #for the letter in the old sentence
        if s == old_character: #if the letter is a character from the old sentence
            new_string += new_character #adds the new character to the new sentence

        else:
            new_string += s #keeps the old character

    return new_string #gives the new sentence
#challenge
def palindrome (word): #defines the function that determines if a word is a palindrome
    if word.ispalindrome(): #if the word is a palindrome
        return True #say that it is true, it is a palindrome
    else:
        return False #says that is is false, it is not a palindrome


def main(): #defines the main function that calls every function in the program
    sing_song() #calls the sing_song function
    tech_ceos = ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Sundar Pichai"] #the list
    print_list(tech_ceos)#prints the list for #3
    Rocky = "Rocky" #the element in my_list
    my_list = ["Mall Cop", "Rocky", "Creed"] #the liist, my_list in #4
    print (contains_element(my_list, Rocky)) #prints that the list contains the element
    integer = "9" #the integer for #5 
    print(is_number_integer(integer))#prints that the integer is a number
    print(replace_character("hello world", "l", "a")) #the old sentence, the new characters
    word = "SONOS" #the palindrome
    random_nmber()#calls the function for #6


    
   

main() #calls the main function




##'''
##START OF DO NOW 4/8/24
##
##def function_name(inputs):
##    action
##    output (print of return)
##'''
##def difference(num1, num2):
##    print (num2 - num1)
##
##def is_positive(string):
##    if string.isnumeric():
##        return True
##    else:
##        return False
##
##
##def main():
##    while True:
##        action = input("What would you like to do? Pick 1 or 2. 1. Find Difference, 2. Check if a string is a positive number: ")
##
##        if action == "1":
##            num1 = int(input("Enter number 1: "))
##            num2 = int(input("Enter number 2: "))
##            difference(num1, num2)
##
##        elif action == "2":
##            string = input("Enter string to check: ")
##            print(is_positive(string))
##
##        else:
##            print("Invalid")
##
##main()
##
###END OF DO NOW 4/8/24

    