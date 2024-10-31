Name: Nikhil Raval
Date: 10/30/24
Log: 1.0- submission
Bugs: cannot get rid of punctuation
Features: writes data to a .csv file, which can be used to make a graph/chart in Google Sheets and/or Microsoft Excel
Description: A program that determines the most frequent words in Harris' or Trump's speeches
_____________________________________________________________________________________________________________________________________________________________________________________

HOW TO USE:


When run, the user is prompted to enter who's speech to get the data for. They have to input either harris or trump (all lowercase). 

Once the user chooses the speech, the program will run on its own. In the background, it determines how many times a word is found in the speech, makes the whole speech lowercase,
removes useless words and punctuation (punctuation doesn't work), and then writes to a .csv file with 12-13 of the most frequent words. If the user chooses to get the data for Harris' speech, the top 12 words will be printed, and the top 13 words if Trump's speech is chosen. 

After the .csv files have been written, they are ready to open in Google Sheets and/or Microsoft Excel. Once opened, the user can make charts and graphs with the data.
_____________________________________________________________________________________________________________________________________________________________________________________

TEST DATA:

Input: 			Output:		

1. harris		1. harris_word_data.csv

2. trump		2. trump_word_data.csv

3. Harris		3. harris_word_data.csv

4. Trump		4. trump_word_data.csv

_____________________________________________________________________________________________________________________________________________________________________________________