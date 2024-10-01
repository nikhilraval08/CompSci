#Name- Nikhil Raval
#Description- a program to optimize the productivity of the GCDS Post Office, program to determine mail type and cost to send
#Bugs- none
#Features- allows users to determine the individual cost of as many parcels as they want
#Log- 1.0.0- submission
_____________________________________________________________________________________________________________________________________________________________________________________

HOW TO USE:


When ran, the user is asked to enter the dimensions of their package using this format: (length, height, thickness, ZIP from, ZIP to), including the commas. The comma is the delimiter, which separates the data. If the user does not enter their data in the correct format, they will be asked to enter it again in the correct format. The same procedure is in place if they do not enter any data or they do not enter a number. After the correct data is entered, the user will receive the final cost. 

The program will run again on its own to allow the user to determine the cost of another package. Every time the program is ran, the program will give the command to end the 
program when the user is done. That command is "stop". Once that command is entered, the program will quit. 

_____________________________________________________________________________________________________________________________________________________________________________________

TEST DATA: 

Input					Output

1. 4,4,.009,02893,08516			1. 0.23

2. 5,7,.013,07245,45216			2. 0.43

3. 5,7,.2,45216,07245			3. 0.45

4. 10,12,.4,15623,89175			4. 0.80

5. 10,12,30,21505,72400			5. 4.65

6. 1000,1000,60,06878,22044		6. unmailable

7. 1,1,.001,32789,23477			7. unmailable

_____________________________________________________________________________________________________________________________________________________________________________________
