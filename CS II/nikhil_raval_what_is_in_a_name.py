'''
 _____________________________________________________________________________________________________________________________________
|                                                                                                                                    |
|                                                           What's in a Name?                                                        |
|____________________________________________________________________________________________________________________________________|
|   Name- Nikhil Raval                                                                                                               |
|   Description- takes a name and either disects it or analyze it                                                                    |
|   Bugs- couldn't find a way to return a bool and also run the task menu, prints True or False instead                              |
|   Features- 13 tasks can be ran                                                                                                    |
|   Log- 1.0.0- submission                                                                                                           |
|____________________________________________________________________________________________________________________________________|
                                
'''

import random
def welcome():
    '''
    Args:
      none
    
    Returns:
      name, program exit  
    '''
    name = input("Welcome to the Function Library for Names! Please enter your name. To end program, type 0000: ")          #asks user for their name
    if name == "0000":                                                                                                      #how the program ends
       exit()
    else:
       start(name)                                                                                                          #starts the program, name is stored
def start(name):
   '''
   Args:
      user's name
   
   Returns:
      user's choice of task
   '''
   print (f"Welcome, {name}")                                                                                               #greets user
   #LIST OF TASKS THAT CAN BE RAN   
   print ('''                  1. Reverse Characters and Display
                  2. How many vowels are in your name?
                  3. How many consonants are in your name?
                  4. Print First Name
                  5. Print Last Name
                  6. Print Middle Name(s)
                  7. Does your name have a hyphen?
                  8. Convert your name to be all lowercase
                  9. Convert your name to be all uppercase
                  10. Create a random name with the characters in your name
                  11. Is your name a palindrome?
                  12. Print initials
                  13. Does your name have a prefix or suffix?
                  14. End Program
               ''')

   choice = input("Please type the number of the task you would like to run.: ")                                           #asks user what task to run
   #IF THE CHOICE = THE NUMBER IN THE MENU, RUN THE CORRESPONDING TASK, TAKES THE USER'S NAME AND CHOICE
   if choice == "1":
       reverse_display(name, choice)
   elif choice == "2":
       vowel_checker(name, choice)
   elif choice == "3":
       conso_checker(name, choice)
   elif choice == "4":
       get_first_name(name, choice)
   elif choice == "5":
       get_last_name(name, choice)
   elif choice == "6":
       get_middle_name(name, choice)
   elif choice == "7":
       hyphen_check(name, choice)
   elif choice == "8":
       to_lower(name)                                                                                                                             
       print(to_lower(name))                                                                                               #converts name to lowercase                                                                                    
       start(name)                                                                                                         #runs the task menu
   elif choice == "9":
       to_upper(name)
       print(to_upper(name))                                                                                               #converts name to uppercase
       start(name)                                                                                                         #runs the task menu
   elif choice == "10":
      random_name_with_chars(name, choice)
   elif choice == "11":
       palindrome(name, choice)
   elif choice == "12":
      initials(name, choice)
   elif choice == "13":
      title_prefix(name, choice)
   elif choice == "14":
      exit()                                                                                                               #ends the program
   else:                                                                                                                   #if the user's choice is not 1-14, then print this                                                           
       ("Please choose one of the tasks.")
       start(name)                                                                                                         #prompts them again to enter a task
#FUNCTION 1
def reverse_display(name, choice):
   '''
    Args: 
        The user's Full Name, the user choosing this function

    Returns:
        the user's full name but in reverse, displays it
    '''
   if choice == "1":                                                                                                       #if the user's choice is 1
    print(name[::-1])                                                                                                      #reverse all characters and print it
    start(name)                                                                                                            #runs the task menu

#FUNCTION 2
def vowel_checker(name, choice):
   '''
    Args: 
        The user's Full Name, the user choosing this function

    Returns:
        number of vowels in name
    '''
   if choice == "2":                                                                                                       #if the user's choice is 2
      vowel_count = 0                                                                                                      #number of vowels = 0
      vowels = ["a","e","i","o","u"]                                                                                       #list of vowels
      for char in name:                                                                                                    #goes through each character in the name
         if char in vowels:                                                                                                #if a character matches up with a vowel
            vowel_count = vowel_count + 1                                                                                  #number of vowels increases by 1
      print (f"Your name has {vowel_count} vowels.")                                                                       #prints number of vowels
      start(name)                                                                                                          #runs the task menu
   else:                                                                                                                   #if there are no vowels
      print ("Your name has no vowels.")                                                                                   #print that there are no vowels
      start(name)                                                                                                          #runs the task menu


#FUNCTION 3
def conso_checker(name, choice):
   '''
    Args: 
        The user's Full Name, the user choosing this function

    Returns:
        number of consonants in name
    '''
   if choice == "3":                                                                                                       #if the user's choice is 3
      conso_count = 0                                                                                                      #number of consonants = 0
      consos = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]                       #list of consonants
      for character in name:                                                                                               #goes through each character in the name
         if character in consos:                                                                                           #if a character is a consonant
            conso_count = conso_count + 1                                                                                  #number of consonants increases by 1
      print (f"Your name has {conso_count} consonants.")                                                                   #prints the number of consonants
      start(name)                                                                                                          #runs the task menu
   else:
      print ("Your name has no consonants.")                                                                               #prints this if the user's name has no consonants
      start (name)                                                                                                         #runs the task menu
#FUNCTION 4
def get_first_name(name, choice):
   '''
   Args:
      User's name, user choosing the function

   Returns:
      user's first name
   '''
   if choice == "4":                                                                                                       #if the user's choice is 4
      sorted_name = name.split()                                                                                           #split the user's name (delimeter is a space)
      length = len(sorted_name)                                                                                            #length of name is the length of the list
      if length >= 3:                                                                                                      #if the length of the name is greater or equal to 3
         print (sorted_name[1])                                                                                            #print the second index of the list
         start(name)                                                                                                       #runs the task menu
      else:                                                                                                                #if the length is not greater or equal to 3
         print(sorted_name[0])                                                                                             #print the first index of the list                                                                
         start(name)                                                                                                       #runs the task menu

#FUNCTION 5
def get_last_name(name, choice):                                                                                     
   '''
   Args:
      User's name, user choosing the function

   Returns:
      user's last name
   '''
   if choice == "5":                                                                                                       #if the user's choice is 5
      sorted_name = name.split()                                                                                           #split the user's name (delimeter is a space)
      length = len(sorted_name)                                                                                            #length of name is the length of the list
      if length == 3:                                                                                                      #if the length of name is 3
         print (sorted_name[2])                                                                                            #print the third index of the list
         start(name)                                                                                                       #runs the task menu
      elif length == 1:                                                                                                    #if the length of the name is 1
         print(sorted_name[0])                                                                                             #print the first index
         start(name)                                                                                                       #runs the task menu
      elif length >= 4:                                                                                                    #if the length of the name is greater or equal to 4
         print(sorted_name[length - 1])                                                                                    #lists start at index 0, length starts at 1 so the program has to find the length of the name and minus -1 to get the index #. Once calculated print the corresponding index
         start(name)                                                                                                       #runs the task menu
      else:                                                                                                                #if the length of the name is 2 (all odd cases were previously tested)
         print(sorted_name[1])                                                                                             #prints the second index
         start(name)                                                                                                       #runs the task menu

#FUNCTION 6
def get_middle_name(name, choice):
   '''
   Args:
      User's name, user choosing the function

   Returns:
      user's middle name/s
   '''
   if choice == "6":                                                                                                       #if the user's choice is 6
      sorted_name = name.split()                                                                                           #splits the user's name (delimeter is a space)
      length = len(sorted_name)                                                                                            #length of name is the length of the list
      if length == 3:                                                                                                      #if the length of name is 3
         if sorted_name[0] == "Mr." or "Mrs." or "Miss" or "Master" or "President":                                        #if the first index is a prefix
            sorted_name.pop(0)                                                                                             #get rid of the prefix
            print (sorted_name[0])                                                                                         #print the new first index
            start(name)                                                                                                    #runs the task menu
      elif length == 2:                                                                                                    #if the length of name is 2                                                                    
         print ("You have no middle name.")                                                                                #user has no middle name, prints that they don't
         start(name)                                                                                                       #runs the task menu
      elif length >= 4:                                                                                                    #if the length of name is greater or equal to 4
         if sorted_name[0] == "Mr." or "Mrs." or "Miss" or "Master" or "President":                                        #if the first index is a prefix
            sorted_name.pop(0)                                                                                             #get rid of the prefix
            print(sorted_name[1:length-2])                                                                                 #prints all indexes from index 1 to the index that is the length of the name - 2 (1 index being the last name, 1 is to compensate for the list starting at 0 and length starting at 1)
            start(name)                                                                                                    #runs the task menu

#FUNCTION 7
def hyphen_check(name, choice):
   '''
      Args: 
         The user's Full Name, the user choosing this function

      Returns:
         if name has a hyphen (-)
      '''
   if choice == "7":                                                                                                       #if the user's choice is 7
      for char in name:                                                                                                    #goes through each character
         if char == "-":                                                                                                   #if the character is a space
            print ("True")                                                                                                 #print true (I couldn't find a way to return a bool while also calling the task menu)
            start(name)                                                                                                          #runs the task menu
         else:                                                                                                                   #if there is no - in the name
            print ("False")                                                                                                      #print false (I couldn't find a way to return a bool while also calling the task menu)
            start(name)                                                                                                          #runs the task menu

#FUNCTION 8
def to_lower(string):
   '''
    Args: 
        characters in the name

    Returns:
        all lowercase characters of the name
    '''
   result = ""                                                                                                             #the result after running the program
   for char in string:                                                                                                     #for each character in the string
      if 'A' <= char <= 'Z':                                                                                               #if the character is an upper case                                                                                        
         result += chr(ord(char) + 32)                                                                                     #find the corresponding character's ordinal values (ASCII) to make it lowercase
      else:
         result += char                                                                                                                                                                    
   return result                                                                                                           #return the result

#FUNCTION 9
def to_upper(string):
   '''
    Args: 
        characters in the name

    Returns:
        all uppercase characters of the name
    '''
   result = ""                                                                                                             #the result after running the program
   for char in string:                                                                                                     #goes through each character in the string                                                   
      if 'a' <= char <= 'z':                                                                                               #if the character is a lower case
          result += chr(ord(char) - 32)                                                                                    #the result
      else:
         result += char                   
   return result                                                                                                           #return the result

#FUNCTION 10
def random_name_with_chars(name, choice):
   '''
   Args:
      user's name, user's choice to run this task
   
   Returns:
      new name made with random characters from the user's name   
   '''
   if choice == "10":                                                                                                      #if the user's choice is 10
     og_name = str(name)                                                                                                   #converts the user's name to a string
     new_name= list(og_name)                                                                                               #their name is then converted to be a list of characters
     random.shuffle(new_name)                                                                                               #shuffles the characters
     edited_name = ''.join(new_name)                                                                                       #adds them to a new string
     print (edited_name)                                                                                                   #prints the new string                                                                           
     start(name)                                                                                                           #runs the task menu

#FUNCTION 11
def palindrome(name, choice):                                                                                              
    '''
    Args: 
        The user's Full Name, the user choosing this function

    Returns:
        whether the user's first name is a palindrome
    '''
    if choice == "11":                                                                                                     #if the user's choice is 11
      #DETERMINES WHAT IS THE FIRST NAME 
      name_split = name.split()                                                                                            #split the name, is put into a list, delimeter is a space
      length = len(name_split)                                                                                             #length of name is the length of the new list
      if length >= 3:                                                                                                      #if the length of the name is greater or equal to 3
         name_reverse = (name_split[1])                                                                                    #use what is in index 1 as it is the first name
      else:
         name_reverse = (name_split[0])                                                                                    #the first name is in index 0
      #DETERMINES THE PALINDROME
      edited_name_reverse = reversed(name_reverse)                                                                         #palindrome version of first name is defined as a reverse of the first name (determined above)
      if list(name_reverse) == list(edited_name_reverse):                                                                  #if the first name is equal to the first name reversed
         print ("True")                                                                                                    #print true (I couldn't find a way to return a bool and also run the task menu)
         start(name)                                                                                                       #runs the task menu
      else:
         print ("False")                                                                                                   #prints false (I couldn't find a way to return a bool and also run the task menu)
         start(name)                                                                                                       #runs the task menu

#FUNCTION 12
def initials(name, choice):
   '''
    Args: 
        The user's Full Name, the user choosing this function

    Returns:
        initials
    '''
   if choice == "12":                                                                                                      #if the user's choice is 12
      sorted_name = name.split()                                                                                           #split the name, put into a list, delimeter is a space
      #IF INDEX 0 OF THE LIST IS A PREFIX
      if sorted_name[0] == "Mr" or sorted_name[0] == "Mrs" or sorted_name[0] == "Miss" or sorted_name[0] == "Master" or sorted_name[0] == "President" or sorted_name[0] == "Dr" or sorted_name[0] == "Sir" or sorted_name[0] == "Madam" or sorted_name[0] ==  "Senor" or sorted_name[0] == "Senorita" or sorted_name[0] == "Senora" or sorted_name[0] == "Professor" or sorted_name[0] == "Profesor" or sorted_name[0] == "Profesora" or sorted_name[0] == "Profe":
         sorted_name.pop(0)                                                                                                #remove it
      #IF THE LAST INDEX OF THE LIST IS A SUFFIX/TITLE/DISTINCTION 
      if sorted_name[-1] == "PhD" or sorted_name[-1] == "Esq" or sorted_name[-1] == "II" or sorted_name[-1] == "III" or sorted_name[-1] == "IV" or sorted_name[-1] == "V" or sorted_name[-1] == "VI" or sorted_name[-1] == "VII" or sorted_name[-1] == "VIII" or sorted_name[-1] == "IX" or sorted_name[-1] == "X" or sorted_name[-1] == "MD" or sorted_name[-1] == "Jr" or sorted_name[-1] == "Sr":
         sorted_name.pop(-1)                                                                                               #remove it
      initials = [item[0] for item in sorted_name]                                                                         #the initials are the first character of each index in the name without a prefix and/or suffix/title/distinction
      print(initials)                                                                                                      #print the initials
      start(name)                                                                                                          #run the task menu
      
#FUNCTION 13
def title_prefix(name, choice):
   '''
    Args: 
        The user's Full Name, the user choosing this function

    Returns:
        whether the user has a prefix and/or suffix/title/distinction
    '''
   if choice == "13":                                                                                                      #if the user's choice is 13
      sorted_name = name.split()                                                                                           #split the name, put into a list, delimeter is a space
      #IF INDEX 0 OF THE LIST IS A PREFIX OR THE LAST INDEX OF THE LIST IS A SUFFIX/TITLE/DISTINCTION
      if sorted_name[0] == "Mr" or sorted_name[0] == "Mrs" or sorted_name[0] == "Miss" or sorted_name[0] == "Master" or sorted_name[0] == "President" or sorted_name[0] == "Dr" or sorted_name[0] == "Sir" or sorted_name[0] == "Madam" or sorted_name[0] ==  "Senor" or sorted_name[0] == "Senorita" or sorted_name[0] == "Senora" or sorted_name[0] == "Professor" or sorted_name[0] == "Profesor" or sorted_name[0] == "Profesora" or sorted_name[0] == "Profe" and sorted_name[-1] == "PhD" or sorted_name[-1] == "Esq" or sorted_name[-1] == "II" or sorted_name[-1] == "III" or sorted_name[-1] == "IV" or sorted_name[-1] == "V" or sorted_name[-1] == "VI" or sorted_name[-1] == "VII" or sorted_name[-1] == "VIII" or sorted_name[-1] == "IX" or sorted_name[-1] == "X" or sorted_name[-1] == "MD" or sorted_name[-1] == "Jr" or sorted_name[-1] == "Sr":
         print ("True")                                                                                                    #print true (I couldn't find a way to return a bool while also running the task menu)
         start(name)                                                                                                       #runs the task menu
      else:                                                                                                                #if the user has no prefix or suffix
         print ("False")                                                                                                   #print false (I couldn't find a way to return a bool while also running the task menu)
         start(name)                                                                                                       #run the task menu
     
welcome()                                                                                                                  #runs the whole entire program

