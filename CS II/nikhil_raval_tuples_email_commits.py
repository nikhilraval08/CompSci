'''
 _____________________________________________________________________________________________________________________________________
|                                                                                                                                    |
|                                                              Tuples                                                                |
|____________________________________________________________________________________________________________________________________|
|   Name- Nikhil Raval                                                                                                               |
|   Description- takes an email log and returns who had the most commits                                                             |
|   Bugs- none                                                                                                                       |
|   Features- two files to choose from                                                                                               |
|   Log- 1.0.0- submission                                                                                                           |
|____________________________________________________________________________________________________________________________________|
                                
'''
from collections import defaultdict

#CREATES A DICTIONARY TO STORE THE COMMIT FREQUENCIES OF EMAILS
email_count = defaultdict(int)

#ASKS THE USER WHAT FILE THEY WOULD LIKE TO USE
data_set_choice = input ("What program would you like to use? Type 1 for mbox.txt or Type 2 for mbox_short.txt.: ")

#IF THE USER CHOOSES 1, THE PROGRAM WILL USE THE BIGGER FILE
if data_set_choice == "1":
    with open("mbox.txt", "r") as file:
        for line in file:
            if line.startswith("From "):
                words = line.split()
                if len(words) > 1:
                    email = words[1]
                    email_count[email] += 1
                
    #converts the dictionary to a list of tuples (count, email)
    email_list = [(count, email) for email, count in email_count.items()]
    
    #sorts the list in descending commit order
    email_list.sort(reverse=True, key=lambda x: x[0])
    
    #if the person that has the most commits is also the person that is at the top of the list (index 0), print who had the most commits, and how many
    if email_list:
        most_frequent_commits = email_list[0]
        print (f" The person with the most email commits is {most_frequent_commits[1]} with ({most_frequent_commits[0]}) total commits.")

    else:
        print ("No emails found in the file. Try again.")

#IF THE USER CHOOSES 2, THE PROGRAM WILL USE THE SMALLER FILE
elif data_set_choice == "2":
    with open("mbox_short.txt", "r") as file:
        for line in file:
            if line.startswith("From "):
                words = line.split()
                if len(words) > 1:
                    email = words[1]
                    email_count[email] += 1
                
    #converts the dictionary to a list of tuples (count, email)
    email_list = [(count, email) for email, count in email_count.items()]
    
    #sorts the list in descending commit order
    email_list.sort(reverse=True, key=lambda x: x[0])
    
    #if the person that has the most commits is also the person that is at the top of the list (index 0), print who had the most commits, and how many
    if email_list:
        most_frequent_commits = email_list[0]
        print (f" The person with the most email commits is {most_frequent_commits[1]} with ({most_frequent_commits[0]}) total commits.")

    else:
        print ("No emails found in the file. Try again.")



