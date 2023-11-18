# Roman Manuel
# Program 10 - Health Data Tracking (tracker.py)
# COP 2500C Section 5
# Nov 18, 2023

# This function takes in a dictionary, asks for 3 goals, then stores the target value
def load_goals(goals):
	for i in range(3):
		key = input("Enter a category for your goal: ").title()
		value = int(input("Enter your target for "+str(key)+": "))
		goals[key] = value

# This function takes in no parameters but returns a dictionary with the user's data for a day
def load_data():

	# Creates an empty dictionary
	data = {}

	# Loops until the user enters "Done" (line 27 triggers the return to main)
	while (True):
		
		# Asks for the category
		category = input("Enter category: ").title()
		
		# Exits the loop with user enters "Done". Gives main the dictionary we created.
		if (category == "Done"):
			return data

		# Asks for the value
		value = int(input("Enter value: "))

		# Checks to make sure the category exists. If not, create a new category.
		if category not in data:
			data[category] = value
		
		# If category exists, gives the user the option to add or replace the value.
		else:
			print("You already have a value for " + str(category) + ".")
			choice = input("Do you want to (1) Add to Steps, or (2) Replace Steps?\n")
			if (choice == "1"):
				data[category] += value # Adds the value
			else:
				data[category] = value # Replaces the value

# This function takes in 2 dictionaries and returns True or False if all 3 goals were met that day
def compare(goals, day):
	
	# Goal counter
	count = 0

	# Loops through each category within goals
	for category in goals:
		# Checks to make sure it exists first
		if category in day:
			# Adds 1 to counter if the goal was met
			if day[category] >= goals[category]:
				count += 1
	
	# Returns either True or False depending on if all 3 initial goals were met
	if count == 3:
		return 1
	else:
		return 0

# The main function
def main():
	
	# The Welcome message
	print("Set your goals for the week!")

	# Creates an empty goals dictionary, loads the dictionary into the load_goals function, and sets a goal counter
	goals = {}
	load_goals(goals) # Calls function to load goals
	count = 0

	# Creates the days of the week
	days = { "Monday": {}, "Tuesday" : {}, "Wednesday" : {}, "Thursday" : {}, "Friday - Happy Friday!" : {}, "Saturday" : {}, "Sunday" : {} }
	
	# Loops through each day, prints the current day, loads data into that day, then compares.
	for day in days:
		print("\nIt\'s", day, "\nEnter your data with the category and measurement.", "\nType \'done\' when done for today.")
		days[day] = load_data() # Calls function to load data
		count += compare(goals, days[day]) # Calls function to compare goals. Adds +1 if met.
	
	# Final message to indicate how many times all 3 goals were met
	print("\nYou hit your goals " + str(count) + " times this week!")

# This starts our program
main()