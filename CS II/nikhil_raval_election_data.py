'''
Name: Nikhil Raval
Date: 10/30/24
Log: 1.0- submission
Features: writes data to a .csv file, which can be used to make a graph/chart in Google Sheets and/or Microsoft Excel
Bugs: cannot get rid of punctuation
Description: A program that determines the most frequent words in Harris' or Trump's speeches
'''
import csv

#SPEECH SELECTION
person_speech = input ("Pick a speech. Harris or Trump?: ")                                                                                                                                                                                                             #user is asked to pick a speech
if person_speech == ("harris") or ("Harris"):
    file = open('kamala_new.txt')                                                                                                                                                                                                                                       #opens Harris' speech
elif person_speech == ("trump") or ("Trump"):
    file = open('trump.txt')                                                                                                                                                                                                                                            #opens Trump's speech
#WORD FREQUENCY VALUES BEING ASSIGNED
speech = dict()                                                                                                                                                                                                                                                         #creates the dictionary
for line in file:                                                                                                                                                                                                                                                       #for every line in the speech
    words = line.split()                                                                                                                                                                                                                                                #splits each word
    for word in words:                                                                                                                                                                                                                                                  #for every word in the speech
        if word not in speech:                                                                                                                                                                                                                                          #if the word is not in the speech
            speech[word] = 1                                                                                                                                                                                                                                            #value is 1
        else:
            speech[word] += 1                                                                                                                                                                                                                                           #if word is in the speech, each time the word is found, the value increases by 1

#SPEECH EDITING/SORTING (CAPITALIZATION, PUNCTUATION, USELESS WORDS, SORTING BY FREQUENCY)
useless_words = ("by", "in", "for", "from", "in", "will", "be", "inside", "like", "are", "because", "has", "have", "was", "why","so", "is", "of", "off","on", "onto", "over", "since", "to", "up", "it", "with", "the", "an", "a", "some", "and", "because", "due")     #list of words to remove
punct = (".", ",", "!", "#", "?", "'", "%", "&")                                                                                                                                                                                                                        #punctuation to remove
speech_lower = {k.lower(): v for k, v in speech.items()}                                                                                                                                                                                                                #makes the whole speech lowercase
sorted_words = {key: val for key, val in sorted(speech_lower.items(), key = lambda ele: ele[1], reverse = True)}                                                                                                                                                        #sorts the words by most frequent to least frequent
for word in useless_words:                                                                                                                                                                                                                                              
    sorted_words.pop(word,0)                                                                                                                                                                                                                                            #gets rid of any word in the list of useless words that is also in the dictionary
for punct_mark in punct:                                                                                                                                                                                                                                                
    sorted_words.pop(punct_mark,0)                                                                                                                                                                                                                                      #gets rid of any punctuation that is in the dictionary

#CSV WRITING 
if person_speech == ("trump") or ("Trump"):                                                                                                                                                                                                                                          #if the user asked to get the data for Trump's speech
    with open('trump_word_data.csv', 'w', newline= '') as file:                                                                                                                                                                                                         #creates the csv
        for key, value in sorted_words.items():                                                                                                                                                                                                                         #for every key value pair (word) in the dictionary
            if value >= 14:                                                                                                                                                                                                                                             #if the value is 14 or greater
                file.writelines(key + "," + str (value) + "\n")                                                                                                                                                                                                         #writes to csv with , as the delimeter between key and value
elif person_speech == ("harris") or ("Harris"):                                                                                                                                                                                                                                       #if the user asked to get the data for Harris' speech
    with open('harris_word_data.csv', 'w', newline= '') as file:                                                                                                                                                                                                        #creates the csv
        for key, value in sorted_words.items():                                                                                                                                                                                                                         #for every key value pair (word) in the dictionary    
            if value >= 10:                                                                                                                                                                                                                                             #if the value is 10 or greater
                file.writelines(key + "," + str (value) + "\n")                                                                                                                                                                                                         #writes to csv with , as the delimeter between key and value