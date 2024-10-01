#Name- Nikhil Raval
#Description- a program to optimize the productivity of the GCDS Post Office, program to determine mail type and cost to send
#Bugs- none
#Features- allows users to determine the individual cost of as many parcels as they want
#Log- 1.0.0- submission


def main():
    print ("Welcome to the GCDS Post Office!")                                                                                                                          #welcomes user to the program           
    details = input ("Please enter your parcel info. To stop, type stop. (Please Seperate length, height, thickness, ZIP from, ZIP to, using commas): ")                #prompts user to enter parcel information  
    if details == ("stop"):                                                                                                                                             #lines 11-13 = command to end the program
        print ("Thanks for stopping by.")
        exit()                                                                                                          
    try:                                                                                                                                                                
        information = details.split(",")                                                                                                                                #seperates the data using "," as the delimeter, makes each data correspond to an index in a list (lines 16-20)
        length = float(information[0])                                                                                                                                  #length is index 0, converts data into a float (number with a decimal)
        height = float(information[1])                                                                                                                                  #height is index 1, converts data into a float (number with a decimal)
        thickness = float(information[2])                                                                                                                               #thickness is index 2, converts data into a float (number with a decimal)
        zip_from = int(information[3])                                                                                                                                  #ZIP from is index 3, converts data into an integer
        zip_to = int(information[4])                                                                                                                                    #ZIP to is index 4, converts data into an integer
        
        mail_type = get_post_type(length, height, thickness)                                                                                                            #gets the mail type from the function get_mail_type (lines 41-71)
        zone_info = abs(get_zone(zip_to) - get_zone(zip_from))                                                                                                          #calculation to figure out zone distance, takes the absolute value of that number
        cost = get_price(mail_type, zone_info)                                                                                                                          #calculates the final cost to send parcel
        print("The cost is: " + str(cost))                                                                                                                              #prints the final calculation 
        print ("_________________________________________________________")                                                                                             
        main()                                                                                                                                                          #program restarts to add more parcels
    

    except ValueError:                                                                                                                                                  #tells program to expect a ValueError, caused by user not entering correctly formatted data
        print ("Please enter an integer. Try again.")                                                                                                                   #the response to give to the user
        print ("_________________________________________________________")
        main()                                                                                                                                                          #program restarts to add more parcels
    
    except IndexError:                                                                                                                                                  #tells program to expect an IndexError, caused by user not entering correctly formatted data
        print ("Please enter correct dimensions and real ZIP Codes. Try again.")
        print ("_________________________________________________________")
        main()                                                                                                                                                          #program restarts to add more parcels


def get_post_type(length, height, thickness):
    #determines the mail type based on dimensions entered, returns the mail type to the main function to prepare for cost calculation
    '''
    Args:
        length: the length of the package
        height: the height of the package
        thickness: the thickness of the package
    
    Returns:
        A mail type based on the dimensions
    '''
                                                                                                                                                                        
    if length > 3.5 and length < 4.25 and height > 3.5 and height < 6 and thickness > .007 and thickness < .016:                                                        #returns Regular Postcard if the dimensions match
        return "Regular Postcard"
    
    elif length > 4.25 and length < 6 and height > 6 and height < 11.5 and thickness > .007 and thickness < .015:                                                       #returns Large Postcard if the dimensions match
        return "Large Postcard"
    
    elif length > 3.5 and length < 6.125 and height > 5 and height < 11.5 and thickness > .016 and thickness < .25:                                                     #returns Envelope if the dimensions match
        return "Envelope"
    
    elif length > 6.125 and length < 24 and height > 11 and height < 18 and thickness > .25 and thickness < .5:                                                         #returns Large Envelope if the dimensions match
        return "Large Envelope"
    
    elif length > 6.125 and length < 24 and height > 11 and height < 18 and thickness > .25 and thickness < .5 and (length + 2*(height) + 2*(thickness) <= 84):         #returns Package if the dimensions exceed the rules for large envelope and the length plus the distance around the sides of the package is equal to 84 inches or less 
        return "Package"
    
    elif (length + 2*(height) + 2*(thickness)) >= 84 and (length + 2*(height) + 2*(thickness)) <= 130:                                                                  #returns Large Package if the length plus the distance around the sides of the package is more than 84 inches and less than 130 inches
        return "Large Package"
    
    else:
        return "Unmailable"                                                                                                                                             #returns Unmailable if none of these conditions apply


def get_zone(zip):  
    #determines the zone distance, how many zones does the parcel have to go through
    '''
    Args:
        zip: the ZIP Code
    
    Returns:
        The distance between ZIP Code zones that the parcel goes through
    '''
                                                                                                                                                                                                                                                                                                            
    if zip > 1 and zip < 6999:                                                                                                                                          #if either ZIP Code is between this range, the zone distance is 1
        zone_distance = 1
    
    elif zip > 7000 and zip < 19999:                                                                                                                                    #if either ZIP Code is between this range, the zone distance is 2
        zone_distance = 2
    
    elif zip > 20000 and zip < 35999:                                                                                                                                   #if either ZIP Code is between this range, the zone distance is 3
        zone_distance = 3

    elif zip > 36000 and zip < 62999:                                                                                                                                   #if either ZIP Code is between this range, the zone distance is 4
        zone_distance = 4
    
    elif zip> 63000 and zip < 84999:                                                                                                                                    #if either ZIP Code is between this range, the zone distance is 5
        zone_distance = 5

    elif zip> 85000 and zip < 99999:                                                                                                                                    #if either ZIP Code is between this range, the zone distance is 6
        zone_distance = 6

    return zone_distance                                                                                                                                                #returns the zone distance to the main function to prepare for cost calculation                                                                                                                                                                                                                                         


def get_price(post_type, zones):   
    #determines the cost to send the package, returns the cost                                                                                                    
    '''
    Args:
        post_type: the mail type
        zones: the zone distance that the parcel goes through

    Returns:
        The cost to send the parcel to its destination
    '''
    if post_type == "Regular Postcard":                                                                                                                                #if the post type is a Regular Postcard, it costs 20 cents plus 3 cents times the number of zones the parcel travels
        return .20+.03*zones
    
    elif post_type == "Large Postcard":                                                                                                                                #if the post type is a Large Postcard, it costs 37 cents plus 3 cents times the number of zones the parcel travels
        return .37+.03*zones
    
    elif post_type == "Envelope":                                                                                                                                      #if the post type is an Envelope, it costs 37 cents plus 4 cents times the number of zones the parcel travels
        return .37+.04*zones
    
    elif post_type == "Large Envelope":                                                                                                                                #if the post type is a Large Envelope, it costs 60 cents plus 5 cents times the number of zones the parcel travels
        return .60+.05*zones
    
    elif post_type == "Package":                                                                                                                                       #if the post type is a Package, it costs $2.95 plus 25 cents times the number of zones the parcel travels
        return 2.95+.25*zones
    
    elif post_type == "Large Package":                                                                                                                                 #if the post type is a Large Package, it costs $3.95 plus 35 cents times the number of zones the parcel travels
        return 3.95+.35*zones
    
    else:                                                                                                                                                              #always declares the post type as unmailable
        return "unmailable"
    

main()                                                                                                                                                                 #starts the program

