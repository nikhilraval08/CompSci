'''
 _____________________________________________________________________________________________________________________________________
|                                                                                                                                    |
|                                                   File Conversion- .txt to CSV                                                     |
|____________________________________________________________________________________________________________________________________|
|   Name- Nikhil Raval                                                                                                               |
|   Description- takes a .txt with fixed length records (student data) and turns it to a CSV file to use in Excel                    |
|   Bugs- none                                                                                                                       |
|   Features- .txt file is converted to CSV for Excel use                                                                            |
|   Log- 1.0.0- submission                                                                                                           |
|____________________________________________________________________________________________________________________________________|
                                
'''
import csv
import re

def seperate_fields(line):
    '''
    Args:
        line

    Returns:
        Preps the dataset to be converted to a CSV, returns the final header structure
    
    '''
#FORMATS EACH FIELD

    #Finds the start and end of each field, removes all unnecessary spaces 
    #finds the Student IDs (first 4 chars of the line)
    student_id = line[:4].strip()
    remaining = line[4:].strip()                                                                    #Everything after ID

    #Find where the Grade (2-digit number) starts
    match = re.search(r'\s(\d{2})\s', remaining) 
    #if a grade cannot be found, the program will stop and raise an error
    if not match:
        raise ValueError(f"Could not locate Grade in: {remaining}")

    grade_index = match.start()                                                                    #Position where Grade starts
    names_part = remaining[:grade_index].strip()                                                   #Everything before Grade (First and Last Name)
    remaining = remaining[grade_index:].strip()                                                    #Everything after Grade

    #Splits the name
    name_parts = names_part.split(maxsplit=1)                                                      #Splits into First & Last
    if len(name_parts) < 2:
        raise ValueError(f"Name format incorrect: {names_part}")

    #saves the first and last names
    first_name = name_parts[0]
    last_name = name_parts[1]

    #Finds the Grade (first 2 characters)
    grade = remaining[:2].strip()
    remaining = remaining[2:].strip()

    #finds GPA 
    gpa = remaining[:4].strip()
    remaining = remaining[4:].strip()

    #finds BirthDate 
    birthdate = remaining[:10].strip()
    remaining = remaining[10:].strip()

    #finds gender 
    gender = remaining[:1].strip()
    remaining = remaining[1:].strip()

    #finds class rank 
    class_rank = remaining[:3].strip()
    remaining = remaining[3:].strip()

    #finds percent attendance
    attend_pct = remaining[:4].strip()
    remaining = remaining[4:].strip()

    #finds Honors (Y/N)
    honors = remaining[:1].strip()
    remaining = remaining[1:].strip()

    #find sports and club count
    sports_match = re.match(r'([A-Za-z\s]+)(\d)$', remaining)
    if sports_match:
        sports = sports_match.group(1).strip()
        club_count = sports_match.group(2).strip()
    else:
        sports = remaining.strip()
        club_count = ""

    #the final header structure is returned to the csv writer
    return [student_id, first_name, last_name, grade, gpa, birthdate, gender, class_rank, attend_pct, honors, sports, club_count]

#CSV IS BEING WRITTEN
def write_fixed_length_csv(input_filename, output_filename):
    '''
    Args:
        the data

    Returns:
        A CSV file of the data    
    '''
    with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

        writer.writerow(["ID", "FirstName", "LastName", "Grade", "GPA", "BirthDate", "Gender", "ClassRank", "AttendPct", "Honors", "Sports", "ClubCount"])

        next(infile)                                                                               #skip the header (ID, First Name, Last Name,...)
        
        #for each line in the file
        for line in infile:                                                                        
            formatted_row = seperate_fields(line)                                                  #runs the first function 
            writer.writerow(formatted_row)

#file in, file out
input_filename = "student_data_cs2 (1).txt"
output_filename = "student_data.csv"

#runs the csv writer
write_fixed_length_csv(input_filename, output_filename)

