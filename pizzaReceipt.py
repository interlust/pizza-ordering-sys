
#from order import orderPizzas #this statement is used to retrieve the order_pizzas function from the order.py file

#pizzas2 = ""
#pizzas2 = [("S", ["PEPPERONI", "HOT PEPPER", "BACON", "PINEAPPLE", "PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE",]), ("XL", ["PEPPERONI", "GREEN PEPPER", "BACON", "PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE",]), ("S", ["PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE","PINEAPPLE",])]
#this above statement comment is used to check interchangeably with "pizzas" variable to test the code easily when making lots of edits.

def generateReceipt(pizzas2): #this is the key function used to print out the receipt
    if len(pizzas2) == 0: #if statement for not ordering anything (empty input)
        print("You did not order anything")
        exit()
    else: #the else statement for calculating the price for all the pizzas and making them in a receipt format.
        print("Your Order: ")
        numberPizza = 0
        totalToppingCost = 0
        totalPizzaCost = 0
        for pizza in pizzas2:  #this for loop uses is the most important in this code as it detects the size of the pizza, the number of toppings and determines the price for the pizza and extra toppings (more than three toppings)
            if pizza[0] == "S":
                pizzaCost = 7.99
                totalPizzaCost = totalPizzaCost + pizzaCost
                toppingCount = 0
                if len(pizza[1]) > 3:
                    topping = (len(pizza[1]))
                    toppingCount = topping - 3
                    toppingCount = toppingCount * 0.50
                    toppingCost = toppingCount
                    totalToppingCost = totalToppingCost + toppingCost

            elif pizza[0] == "M":
                pizzaCost = 9.99
                totalPizzaCost = totalPizzaCost + pizzaCost
                toppingCount = 0
                if len(pizza[1]) > 3:
                    toppingCount = (len(pizza[1]))
                    toppingCount = toppingCount - 3
                    toppingCount = toppingCount * 0.75
                    toppingCost = toppingCount
                    totalToppingCost = totalToppingCost + toppingCost

            elif pizza[0] == "L":
                pizzaCost = 11.99
                totalPizzaCost = totalPizzaCost + pizzaCost
                toppingCount = 0
                if len(pizza[1]) > 3:
                    toppingCount = (len(pizza[1]))
                    toppingCount = toppingCount - 3
                    toppingCount = toppingCount * 1.00
                    toppingCost = toppingCount
                    totalToppingCost = totalToppingCost + toppingCost

            elif pizza[0] == "XL":
                pizzaCost = 13.99
                totalPizzaCost = totalPizzaCost + pizzaCost
                toppingCount = 0
                if len(pizza[1]) > 3:
                    toppingCount = (len(pizza[1]))
                    toppingCount = toppingCount - 3
                    toppingCount = toppingCount * 1.25
                    toppingCost = toppingCount
                    totalToppingCost = totalToppingCost + toppingCost

            numberPizza = numberPizza + 1 #this increments the loop for changing the pizza number in the receipt
            print(f'{"Pizza " + str(numberPizza) + ": " + pizza[0]:30s} {"%.2f" %pizzaCost:>5s}') #this is used to print out the base pizza cost.

            for toppingS in pizza[1]: #this for loop prints out the toppings
                print("- " + toppingS)
            if len(pizza[1]) > 3: #this if statement prints out extra toppinga and its price by determining how many toppings by using the previous toppingCost function
                print(f'{"Extra Topping " + "(" + pizza[0] + ")":30s} {"%.2f" %toppingCost:>5s}')


        tax = 0.13 * (totalPizzaCost + totalToppingCost) #this variable calculates the tax.
        print(f'{"Tax:":30s} {"%.2f" %tax:>5s}') #this statement prints the tax with right alignment to the digits.
        total = tax + (totalPizzaCost + totalToppingCost) #this calculates out the total of the order
        print(f'{"Total:":30s} {"%.2f" %total:>5s}') #this prints out the total for the pizza with the right alignment formating to the digits


