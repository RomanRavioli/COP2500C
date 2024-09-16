# Roman Manuel
# COP 2500C Section 5
# Lab 5: Challenge 2
# Sep 25, 2023

# Variable declaration
days = int(input("How many days are we tracking?\n"))
steps = 0
total = 0
average = 0

# Creates a for loop than includes the final day by adding +1 in range
for i in range(1, days + 1):
    # Ask user for number of steps that day
    steps = int(input("Day " + str(i) + ": How many steps?\n"))
    # Keeps track of total in order to calculate the average later
    total += steps
    # Nested if statement used to determine which statement to output each day
    if (steps >= 10000):
        print("You walked enough")
    else:
        print("You should walk more")

# After the for loop ends, calculates the average and then determines whether to say "good job"
if (total / days >= 10000):
    print("You averaged more than 10,000 steps per day. Good job!")
