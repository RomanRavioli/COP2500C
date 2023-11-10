# Roman Manuel
# Program 8 - 5k Race Qualifiers
# COP 2500C Section 5
# Nov 10, 2023

# This functioon allows the user to choose from a menu and returns the choice
def menu():
    print("\nWhat would you like to do?")
    print("1 - Add a time")
    print("2 - Delete a time")
    print("3 - Compare times")
    print("4 - Check qualifiers")
    print("5 - Quit")
    choice = int(input(""))
    return choice

# This function lets user add a time to any racer
def add_time(racer_a, racer_b):
    choice = input("\nWhich racer is adding a time? (A/B)\n").upper()
    if (choice != "A" and choice != "B"):
        print("Could not interpret racer. Please use A or B")
        return
    time = float(input("What is the time to be added?\n"))
    if (choice == "A"):
        racer_a.append([])
        racer_a[len(racer_a) - 1].append(time)
        return
    if (choice == "B"):
        racer_b.append([])
        racer_b[len(racer_b) - 1].append(time)
        return

# This function lets user delete a time, either by deleting a race or a time
def delete_time(racer_a, racer_b):
    
    choice = input("\nWhich racer is deleting a time? (A/B)\n").upper()
    
    # Checks to see if input is valid
    if (choice != "A" and choice != "B"):
        print("Could not interpret racer. Please use A or B")
        return
    question = input("Delete a time or delete a race?\n").lower()
    if (question != "time" and question != "race"):
        print("Could not interpret deletion. Please use time or race.")
        return

    # Deletes time through the inner list
    if (question == "time"):
        time = float(input("What time should be deleted?\n"))
        if (choice == "A"):
            racer_a.remove([time])
            return
        if (choice == "B"):
            racer_b.remove([time])
            return
        
    # Deletes an entire race through the outer list
    if (question == "race"):
        race = int(input("What race should be deleted?\n"))
        if (choice == "A"):
            racer_a.pop(race - 1)
            return 
        if (choice == "B"):
            racer_b.pop(race - 1)
            return

# This function compares each racer to see who won.
# Only compares the lowest number of races that can be compared
def compare_time(racer_a, racer_b):

    # Checks to see if any racer has zero times
    if(len(racer_a) == 0 or len(racer_b) == 0):
        print("At least one racer has no times!")
        return
    
    # Checks to see if both racers have the same number of races
    # Displays how many races will be calculated
    if(len(racer_a) != len(racer_b)):
        print("\nRacer A has data for " + str(len(racer_a)) + " races.")
        print("Racer B has data for " + str(len(racer_b)) + " races.")
    if(len(racer_a) > len(racer_b)):
        print("We will compare the first " + str(len(racer_b)) + " races.")
    if(len(racer_a) < len(racer_b)):
        print("We will compare the first " + str(len(racer_a)) + " races.")
    if(len(racer_a) == len(racer_b)):
        print("We will compare the first " + str(len(racer_b)) + " races.")
    
    # If racer A has less races
    if(len(racer_a) < len(racer_b)):
        for i in range(len(racer_a)):
            # Racer A wins
            if (racer_a[i] > racer_b[i]):
                print("Racer A has won race #" + str(i + 1) + "!")
            # Racer B wins
            if (racer_a[i] < racer_b[i]):
                print("Racer B has won race #" + str(i + 1) + "!")
            # Tie
            if (racer_a[i] == racer_b[i]):
                print("The racers tie race #" + str(i + 1) + ".")       
    
    # If racer B has less races
    if(len(racer_a) > len(racer_b)):
        for i in range(len(racer_b)):
            # Racer A wins
            if (racer_a[i] > racer_b[i]):
                print("Racer A has won race #" + str(i + 1) + "!")
            # Racer B wins
            if (racer_a[i] < racer_b[i]):
                print("Racer B has won race #" + str(i + 1) + "!")
            # Tie
            if (racer_a[i] == racer_b[i]):
                print("The racers tie race #" + str(i + 1) + ".")      
    
    # If both racers have the same amount of races
    if(len(racer_a) == len(racer_b)):
        for i in range(len(racer_b)):
            if (racer_a[i] > racer_b[i]):
                print("Racer A has won race #" + str(i + 1) + "!")
            if (racer_a[i] < racer_b[i]):
                print("Racer B has won race #" + str(i + 1) + "!")
            if (racer_a[i] == racer_b[i]):
                print("The racers tie race #" + str(i + 1) + ".")

# This function checks to see who qualifies
def check_qualifiers(racer_a, racer_b, qualifer):
    for i in range (3):
        print("") # For style spacing
        if(racer_a[i][0] > qualifer[i]):
            print("Racer A Qualifies!")
        if(racer_b[i][0] > qualifer[i]):
            print("Racer B Qualifies!")
        if(racer_a[i][0] <= qualifer[i] and racer_b[i][0] <= qualifer[i]):
            print("Neither racer qualified.")
        return

# Our main function  
def main():

    # Creates a 2d-list for Racer A and Racer B, as well as a normal list for qualifer times
    racer_a = [[0], [0], [0]]
    racer_b = [[0], [0], [0]]
    qualifer = [0,0,0]
    
    # Loads the times for Racer A
    print("Enter times for Racer A:")
    racer_a[0][0] = float(input("Race #1: "))
    racer_a[1][0] = float(input("Race #2: "))
    racer_a[2][0] = float(input("Race #3: "))

    # Loads the times for Racer B
    print("\nEnter times for Racer B:")
    racer_b[0][0] = float(input("Race #1: "))
    racer_b[1][0] = float(input("Race #2: "))
    racer_b[2][0] = float(input("Race #3: "))
    
    # Loads the qualifying times
    print("\nEnter times for the qualifiers:")
    qualifer[0] = float(input("Race #1: "))
    qualifer[1] = float(input("Race #2: "))
    qualifer[2] = float(input("Race #3: "))
    
    # Infinitely looping menu selection that stops on choice = 5
    choice = menu()
    while (choice != 5):
        if(choice == 1):
            add_time(racer_a, racer_b)
        if(choice == 2):
            delete_time(racer_a, racer_b)
        if(choice == 3): 
            compare_time(racer_a, racer_b)
        if(choice == 4):
            check_qualifiers(racer_a, racer_b, qualifer)
        choice = menu()

# This starts our program
main()