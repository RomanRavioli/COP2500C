# Roman Manuel
# Program 10 - Health Data Tracking (tracker.py)
# COP 2500C Section 5
# Nov 18, 2023

def load_goals(goals):
	for i in range(3):
		key = input("Enter a category for your goal: ").title()
		goals[key] = int(input("Enter your target for "+key+": "))
		print("\n"+str(goals)+"\n") # Debug statement

def load_data():
	return

def main():
	
	print("Set your goals for the week!\n")
	
	goals = {}
	days = { "Monday": [], "Tuesday" : [], "Wednesday" : [], "Thursday" : [], "Friday" : [], "Saturday" : [], "Sunday" : [] }
	
	load_goals(goals)
	
	for day in days:
		print("It\'s "+day)
		print("Enter your data with the category and measurement.")
		print("Type \'done\' when done for today.")
		category = input("Enter category: ").title()
		
	
main()