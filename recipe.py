# Roman Manuel
# Program 7 - Smoothie Recipes
# COP 2500C Section 5
# 10/25/2023

# This function lets the user input the initial amounts for each ingredient.
def load(ingredients):
    ingredients[0] = float(input("How many bananas do you have?\n"))
    ingredients[1] = float(input("How many strawberries do you have?\n"))
    ingredients[2] = float(input("How many blueberries do you have?\n"))
    ingredients[3] = float(input("How many cups of spinach do you have?\n"))
    ingredients[4] = float(input("How many avocados do you have?\n"))

# This function shows the menu screen and returns the user's choice.
def menu():
    print("\nWhat would you like to do?")
    print("1 - View Ingredients")
    print("2 - Update Ingredients")
    print("3 - Make a Smoothie")
    print("4 - Quit")
    option = int(input(""))
    return option

# This function allows the user to view how many of each ingredients they have.
def view(ingredients):
    print("\nAmount of Ingredients:")
    print("Bananas:        ", ingredients[0])
    print("Strawberries:   ", ingredients[1])
    print("Blueberries:    ", ingredients[2])
    print("Spinach:        ", ingredients[3], "cups")
    print("Avocados:       ", ingredients[4])

# This functions lets the user change how many of each ingredient they have.
def update(ingredients):
    ingredients[0] = float(input("\nHow many bananas do you have?\n"))
    ingredients[1] = float(input("How many strawberries do you have?\n"))
    ingredients[2] = float(input("How many blueberries do you have?\n"))
    ingredients[3] = float(input("How many cups of spinach do you have?\n"))
    ingredients[4] = float(input("How many avocados do you have?\n"))

# This function asks which ingredients to use, then checks if there's enough.
# If there is enough, will calculate the Drink Score and the Health Score.
def make(ingredients):

    # Asks whhihch ingredients to use.
    bananas_ = input("\nWill you use bananas?\n").lower()
    strawberries_ = input("Will you use strawberries?\n").lower()
    blueberries_ = input("Will you use blueberries?\n").lower()
    spinach_ = input("Will you use spinach?\n").lower()
    avocado_ = input("Will you use avocado?\n").lower()

    # Checks if there is enough ingredients to make a smoothie.
    if ((bananas_ == "yes" and ingredients[0] < 1)
        or (strawberries_ == "yes" and ingredients[1] < 5)
        or (blueberries_ == "yes" and ingredients[2] < 12)
        or (spinach_ == "yes" and ingredients[3] < 1)
            or (avocado_ == "yes" and ingredients[4] < .5)):
        print("\nSorry, this recipe cannot be completed")
        return

    # Calculates the smoothies' Drinkn Score.
    if (spinach_ == "yes" and avocado_ == "yes"):
        print("\nYour recipe scored a Drink Score of 0. Yuck!")
    elif (spinach_ == "no" or avocado_ == "no"):
        print("\nYour recipe scored a Drink Score of 1. It will be delicious!")

    # Calculates the smoothies' Health Score.
    if (spinach_ == "no" and avocado_ == "no"):
        print("Your recipe scored a Health Score of 0. It probably tastes good though.")
    elif (spinach_ == "yes" and avocado_ == "yes"):
        print("Your recipe scored a Health Score of 2. It will be super healthy!")
    elif ((spinach_ == "no" and avocado_ == "yes") or (spinach_ == "yes" and avocado_ == "no")):
        print("Your recipe scored a Health Score of 1. It is good to go!")

    # If an ingredient is used, subtracts the amount used from the total.
    if (bananas_ == "yes"):
        ingredients[0] -= 1
    if (strawberries_ == "yes"):
        ingredients[1] -= 5
    if (blueberries_ == "yes"):
        ingredients[2] -= 12
    if (spinach_ == "yes"):
        ingredients[3] -= 1
    if (avocado_ == "yes"):
        ingredients[4] -= .5


def main():

    # The Welcome Message
    print("Welcome to our Smoothie Recipe Analyzer!\n")

    # Declares a list with 5 items.
    ingredients = [0, 0, 0, 0, 0]

    # Loads the initial amounts for each ingredient by calling the load() function.
    load(ingredients)

    # Calls the menu() function, then calls the correct function based on the input.
    option = menu()
    while (option != 4):
        if option == 1:
            view(ingredients)
        if option == 2:
            update(ingredients)
        if option == 3:
            make(ingredients)
        option = menu()


# This starts our program.
main()