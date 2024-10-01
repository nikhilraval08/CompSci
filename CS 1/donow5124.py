last_names = ["Marciano", "Campbell", "Iverson", "Russo"]
first_names = ["Sam", "Gordie", "Annette", "Paula"]
subjects = ["CS1", "CS2", "Calculus", "Law"]

mode = input("Which would you like: 1. Print all, 2. Print Specific")

if mode == "1":
    for i in range(len(first_names)):
        print(f'''\nlast name: {last_names[i]}
              
    first name: {first_names [i]}
    subject: {subjects[i]}''')
    
elif mode == "2":
    name = input ("Enter a last name: ")

    if name in last_names:
        i = last_names.index(name)
        print(f'''\nlast name: {last_names[i]}
    
    first name: {first_names[i]}
    subject: {subjects[i]}''')

