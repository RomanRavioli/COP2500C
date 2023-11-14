# Roman Manuel
# COP 2500C Section 5
# 11/13/2023

def load_goals(dictionary_name):
    # Loads Goals Function
    # Takes in a dictionary and prompts the user for 3 goals and stores the category as the key, and the amount of that goal as the value.

    # Ask for the category and the value
    # Save it into the dictionary
    # Do that 3 times - for loop

def enter_data():
    # 1. Function is named correctly and takes in no parameters.
    # 2. Create an empty dictionary.
    
    # 3. Loops until the user inputs "done" - While Loop!
        
        # 4. Prompts the user to enter category and value.
    
        # 5. Inputs the value into the dictionary if it doesn't exist.
        # if category in dictionaryvariable: <- This tells you if category is in dictionaryvariable
        # else <- This tells you that it is not in the dictionary
        # 6. If it does exist, ask if they would like to add or replace value.
            # 7. If they select add, adds the value to the previous value/If they select replace, replaces the previous value
    # 8. Returns the dictionary to the main function.

def compare_goals(dictionary_1, dictionary_2):
    # 1. Takes in two dictionaries as parameters
    # 2. Check if all three goals are met
    # 3. Returns 0 or Flase if they are not met, and returns 1 or True if they are met

    # Loop through each key in goals and do... (for key in goals)
        # If the key is in the daily dictionary
            # If the goal is greater than the daily key
                # return False
        # Else <- This will be True if it isn't in the dictionary
            # return False
    return True

def main():
    # Main Function - Variables
    # 1. Creates a dictionary to store the goals of the user.
    goals = {}

    # 2. Has a variable that keeps track of how many days the user meets all 3 goals.
    day = 0

    # Calls function to Load Goals - Passes in the goals dicitonary.

    # For each day:
    # 1. Prints out the day of the weeek
    # 2. Calls the function to enter data
    # In step 2, you should save that dictionary
    # Then write a line that passes that step 2 dictionary and goals into the compare_goals
    # Save the result of compare_goals, and if it is true or 1, then add 1 to day

    # Print how many days met (formatted)