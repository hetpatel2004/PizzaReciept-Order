from pizzaReceipt import *

# This function allows the user to pick the sizes for S,M,L or Xl. This function also checks whether if the user input is S,M,L,XL. If its not one of these, then the user will be prompted to type it again


def avalibleSizes():
    size = input("Choose a size: S, M, L, or XL: ")
    # This while loop allows the user to type s,m,l, xl in lower case, and if these size abbrevations are not typed where the user types something else, then they will be prompted with a statement saying "invalid size, try again".
    while size.lower() not in ("s", "m", "l", "xl"):
        print("Invalid size, try again ")
        size = input("Choose a size: ")
    return size

# This function simply allows the user to enter toppings and add it to the list, and it also checks whether if the toping is correctly typed. The function also shows the users the toppings when "x" is typed. If the user types in a topping that is not from the given toping kistm then they will be prompted to type a valid toping


def addedToppings():
    # This line stores the selectable toppings, the user is able to choose when picking topings.
    TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE",
                "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI",
                "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
    addedToppings = []
    x = True
    # This while block simply asks the user whether if they want to see the list of avalible toppings. So when the user types list in any case, they will be able to see
    while x == True:
        print(
            "Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\""
        )
        addedToppingsInput = input()
        addedToppingsInput = addedToppingsInput.upper()

        if addedToppingsInput == "LIST":
            print(TOPPINGS)
# This ellif statement simply adds the toppings the selected topics the user has and prints it
        elif addedToppingsInput in TOPPINGS:
            print("Added " + addedToppingsInput + " to your pizza")
            addedToppings.append(addedToppingsInput)

        elif addedToppingsInput == "X":

            return addedToppings

        else:
            print("Invalid topping")


# This empty list is used to enter the topings the user type
ordersList = []

# This part of the if statement, the input is used to ask the user if they want to order pizza.
response = input("Do you want to order a pizza? ")
# This part of the if statement accepts both cases of no and q to quit. So this allows the user to be able to type no and yes in both cases.

if response.lower() == "no" or response.lower() == "q":
    generateReceipt(ordersList)
else:
    s = avalibleSizes()
    t = addedToppings()
    pizza = (s, t)
    ordersList.append(pizza)

    # This part of the program asks the user if they want to continue ordering after 1 pizza has been ordered. However If they type in no or q in any case, then the program will simply exit and print out their current reciept list
    x = True
    while x == True:
        userInput = input("\nDo you want to continue ordering? ")
        # As mentioned earlier, this if statement specifically exceutes what would happen when the user types in NO or Q in any case.
        if userInput.upper() != "Q" and userInput.upper() != "NO":
            s = avalibleSizes()
            t = addedToppings()
            pizza = (s, t)
            ordersList.append(pizza)
        else:
            x = False
    generateReceipt(ordersList)
