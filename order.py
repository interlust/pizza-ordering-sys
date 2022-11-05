from pizzaReceipt import generateReceipt
#Pizza Order Parameter

#pizzas2 = [("S", ["PEPPERONI", "HOT PEPPER", "BACON"]), ("XL", ["PEPPERONI", "GREEN PEPPER", "BACON", "PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE",]), ("S", ["PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE",])]

def orderPizzas(): #This function is the primary function that takes in input values from the user about their order.
    PIZZA_SIZES = ("S", "M", "L", "XL") #these are the abbreviations of pizza sizes
    TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
    pizzas = [] #empty list into which the pizza options will get added which will further be sent to pizzareceipt.py
    size = 0
    askOrder = 0

    askOrder = input("Do you want to order Pizza? ") #initial input asking question

    if askOrder.upper() == "" or askOrder.upper() == " ": #if statement to print "you did not order anything" for empty inputs
        print("You did not order anything")
        return

    while askOrder.upper() != "NO" and askOrder.upper() != "N" and askOrder.upper() != "Q" and askOrder.upper() != "" and askOrder.upper() != " ": #this while loop initiates the function with any value other than 0.
        size = input("Choose a Size: S, M, L or XL: ") #this asks the user of the size of the pizza they want.
        pizza1 = (size.upper(), []) #this creates colums in the list for size and toppings.
        if size.upper() in list(PIZZA_SIZES):
            askToppings = ""
            while askToppings.upper() != "X": #this command asks the user for toppings.
                askToppings = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter ""LIST"". When you are done adding toppings, enter ""X"" ")
                if askToppings.upper() == "LIST": #this command prints the list of toppings if the user wants to view them.
                    print(TOPPINGS)

                elif askToppings.upper() in TOPPINGS: #this statement appends (puts the topping in the end) which the user chooses and it is continious with the loop.
                    pizza1[1].append(askToppings.upper())
                    print("Added " + askToppings.upper() + " to your pizza")
                    
                elif askToppings.upper() == "X": #this is the input the user uses to end their pizza order.
                    pizzas.append(pizza1)
                    askOrder = input("Do you want to order more Pizza? ") #this command asks the user if they want more pizza.

                else: #this condition displays to the user that the topping they inputted is invalid and we do not sell it.
                    print("Invalid Topping")
                    
        else:
            print("Invalid Input") #this command gives out invalid input - for e.g. if the user types an invalid size.

    return pizzas  #this returns the order of list of pizzas which the receipt file calls and make a receipt out of.

pizzas2 = orderPizzas()
generateReceipt(pizzas2)



