'''
Author- Nikhil Raval
Date- 3/29/24
Description- Food-o-Matic
Challenges- Cost Calculation was hard to figure out
Bugs- None
Sources- Siri, Ms. Marciano
'''

import random #brings in the package, random
appetizers = ["Miso Soup", "Wonton Soup", "Papadum", "Fondue", "Peking Duck", "Spring Roll", "Meatballs", "Nachos", "Pasta", "No appetizer"] #list of appetizers
mains = ["Burger", "Dirty Water Hot Dog", "Filet Mignon", "Chicken Tikka Masala", "Pizza", "Salmon Nigiri (4 pieces)", "Quesadilla", "Dosa", "Garden Catering Chicken Tenders", "Chick-fila Spicy Chicken Sandwich", "General Tso's Sweet and Sour Chicken"]#list of main dishes
sides = ["Fries", "Doritos", "Garlic Naan", "Buffalo Wings", "Dumplings", "Noodles", "Indian Street Corn", "Idli", "Mini Tacos", "Okra"]#list of side dishes
drinks = ["Soda", "Beer", "Wine", "Lemonade", "Tea", "Water", "Mango Lassi", "Coffee", "Cocktail", "Mocktail"]#list of drinks
desserts = ["Ice Cream", "New York Cheesecake", "Jalebis", "Gulab Jamun", "Tiramisu", "Mooncake", "No dessert"]#list of desserts

#below are the prices for the appetizers, mains, sides, drinks, and desserts

main_costs = [12, 3, 30, 20, 15, 20, 10, 13, 13, 14, 20]
app_costs = [5, 5, 1, 10, 20, 8, 10, 5, 10, 0]
side_costs = [4, 3, 2, 10, 7, 5, 5, 7, 10, 6]
drink_costs = [3, 7, 30, 3, 4, 0, 7, 7, 13, 7]
dessert_costs = [4, 8, 5, 5, 8, 10, 0]


    
print ("Welcome to the Food-o-Matic!")#prints this when code is started

while True: #if this statement is true
    try: #tries this for errors
        number_of_people = int(input("How many people are ordering?"))#food-o-matic prompts user to specify how mnay people are ordering

        if number_of_people > 10: #if the number of people ordering is more than 10 
            print("We don't have the food to fufill your order. We are terribly sorry.") #prints this as a response to the user's input
        elif number_of_people <=0: #if the number of people is 0, prints the command below
            print("Please enter an integer greater than zero!")
        else: 
            break #stops the while True loop from running
    except ValueError: #if a number is not entered, prints the command below
        print("Please enter an integer!")
        
total_cost = 0 #total cost of bill starts at 0

for i in range (number_of_people): #goes through the range (0,the user's input)

#below are lines of code defining the random choices the food-o-matic made
    main = random.choice(mains) 
    app = random.choice(appetizers)
    side = random.choice(sides)
    drink = random.choice(drinks)
    dessert = random.choice(desserts)

#below is each course/item cost calculation
    
    cost_main = main_costs[mains.index(main)]
    cost_app = app_costs[appetizers.index(app)]
    cost_side = side_costs[sides.index(side)]
    cost_drink = drink_costs[drinks.index(drink)]
    cost_dessert = dessert_costs[desserts.index(dessert)]

   
    cost = int(cost_main + cost_app + cost_side + cost_drink + cost_dessert) #int helps in converting the costs to integers so they can be added

    print(f"I'll start with the {app} followed by {main} with {side} and {drink}. Dessert will be {dessert}")#the generated response
    print(f"Your total cost for this person is ${cost}") #total cost for a singular person
    total_cost += cost #defining the total cost of 0 + the cost of each person
    print(f"Your total cost is ${total_cost}") #total cost of every person eating
    print("Thank you for visiting the Food-o-Matic. Please come again!") #goodbye
   







e come again!") #goodbye
    






