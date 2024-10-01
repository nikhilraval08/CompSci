'''
Name- Nikhil Raval
Date- 5/13/24
Challenges- errors
Bugs- none
Sources- Samantha Marciano
'''
#below are the parallel arrays (not any of my real logins for security purposes)
websites = ["icloud.com", "accounts.google.com", "electronics.sony.com", "wellsfargo.com"]
usernames = ["niki@me.com", "niki@gmail.com", "N1Ki", "nhr0908"]
passwords = ["R7$_gM15059", "8Mgj110?>+ngD32ng", "qU\PPoCY_7?$$2*6", "applebabyNYC24076!5E"]

#if this statement is true
while True:
    pin = input ("Enter security code. :") #prompts user to enter the security code
    if pin == "thebetterappleguy08": #if the user enters the security code
        print ("Unlocked.") #prints unlocked
        
        mode = input("Which would you like: 1. Print all passwords in library, 2. Print Specific password, or 3. Add a password?:") #functions of password keeper
#below is the mode that prints all of the passwords in the keeper
        if mode == "1": 
            for i in range(len(websites)): 
                print(f'''\nwebsite: {websites[i]}  
                    
            username: {usernames [i]}
            password: {passwords[i]}''')
#below is the mode that prints a specific password based on website        
        elif mode == "2":
            site = input ("Enter a website: ")

            if site in websites:
                i = websites.index(site)
                print(f'''\website: {websites[i]}
            
            username: {usernames[i]}
            password: {passwords[i]}''')
                break
#below is the mode to add a password
        elif mode == "3":
            new_password_web = input ("What is the website?: ")
            websites.append(new_password_web)
            new_password_user = input ("What is the username?: ")
            usernames.append(new_password_user)
            new_password_pass = input ("What is the password?: ")
            passwords.append(new_password_pass)
            print ("Your new password information has been added to the database.")
                
            for i in range(len(websites)):
                print(f'''\nwebsite: {websites[i]}
                        
                    username: {usernames [i]}
                    password: {passwords[i]}''')
        #gives user the option to end the program
        exit = input("Do you want to exit?")

        #if they enter yes, the program quits    
        if exit == "yes":
            break
        #if they enter no, the program keeps going but re-verifies
        elif exit == "no":
            print ("Please re-verify")
            pass
        

    
        #prints invalid if response to mode is not 1, 2, or 3
        else:
            print ("Invalid")
            

                
    #prints Try Again if the user does not input the correct security code
    else:
        print ("Try Again.")

        