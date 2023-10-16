# Roman Manuel
# COP2500C Section 5
# Program 5 - Set Tracking
# 10/13/2023

# Asks for # of workouts
workouts = int(input("How many workouts do you have data for?\n"))

# Loops for every workout
for i in range(1, workouts + 1):

    # Resets the variables for every workout
    total = 0
    average = 0

    # Asks for # of sets
    sets = int(input("How many sets were completed in workout #" + str(i) + "?\n"))

    # Nested loop: Asks for # of reps within the current set
    for j in range(1, sets + 1):
        reps = int(input("How many reps in set #" + str(j) + "?\n"))
        total += reps

    # Calculates the average. Then prints the result for the current workout
    average = total / sets
    print("Workout #" + str(i) + ": The average number of reps was " +
          str(round(average, 3)) + ".\n")
