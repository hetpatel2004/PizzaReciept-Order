# In this function, if the user enters a empty string then the message you did not order anything will be printe. However, if the user does type somehting then they will be prompted further to enter in their custom order information
def generateReceipt(pizzaOrder):
    if len(pizzaOrder) == 0 or pizzaOrder == "":
        print("You did not order anything")
    else:
        print("Your order:")

        runningTotal = 0
        # This for loop simply stores the indvidual prices for the diffrent types of pizza sizes avalible.
        for pizza in pizzaOrder:
            basePizzaCost = 0
            # For small or the abbreviation "s" in any case, the price will be set to $7.99
            if pizza[0].upper() == "S":
                basePizzaCost = 7.99
# For medium or the abbreviation "m" in any case, the price will be set to $9.99
            elif pizza[0].upper() == "M":
                basePizzaCost = 9.99
# For large or the abbreviation "l" in any case, the price will be set to $11.99
            elif pizza[0].upper() == "L":
                basePizzaCost = 11.99
# For extra lare or the abbreviation "xl" in any case, the price will be set to $13.99
            elif pizza[0].upper() == "XL":
                basePizzaCost = 13.99


# Increment for running total from 0
            runningTotal += basePizzaCost

            # This block of code simply is used to print the allignment. It also prints the the correct pizza size in correlation with the respective "basePizzaCost", in other words the price
            print("{:<20}{:>20,.2f}".format(
                "Pizza " + str(pizzaOrder.index(pizza) + 1) + ": " +
                str(pizza[0]).upper(), basePizzaCost))

            for topping in pizza[1]:
                print("- ", topping)

            if len(pizza[1]) > 3:
                extraToppings = len(pizza[1]) - 3
                toppingCost = 0

                if pizza[0].upper() == "S":
                    toppingCost = extraToppings * 0.5
                elif pizza[0].upper() == "M":
                    toppingCost = extraToppings * 0.75
                elif pizza[0].upper() == "L":
                    toppingCost = extraToppings * 1
                elif pizza[0].upper() == "XL":
                    toppingCost = extraToppings * 1.25

                runningTotal += toppingCost

                # This for loop is simply used for the right allignment once again, however this time the allignment is used for the extra topping caculations.
                for i in range(0, extraToppings):
                    if pizza[0].upper() == "S":
                        print("{:<20}{:>20,.2f}".format(
                            "Extra Topping (" + str(pizza[0]).upper() + ")", 0.5))

                    elif pizza[0].upper() == "M":
                        print("{:<20}{:>20,.2f}".format(
                            "Extra Topping (" + str(pizza[0]).upper() + ")", 0.75))

                    elif pizza[0].upper() == "L":
                        print("{:<20}{:>20,.2f}".format(
                            "Extra Topping (" + str(pizza[0]).upper() + ")", 1.00))

                    elif pizza[0].upper() == "XL":
                        print("{:<20}{:>20,.2f}".format(
                            "Extra Topping (" + str(pizza[0]).upper() + ")", 1.25))

        TAXRATE = 0.13
        # Multiplies the pizza cost x 13%
        tax = runningTotal * TAXRATE
        print("{:<20}{:>20,.2f}".format("Tax:", tax))
        print("{:<20}{:>20,.2f}".format("Total:", runningTotal + tax))
