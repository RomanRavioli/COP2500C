# Knightro
# Lab 1: Challenge 3
# COP 2500C Section 5
# Aug 31, 2023

# Ask for Input
hours = float(input("How many hours does Knightro have to run?\n"))
speed = int(input("How fast is Knightro running?\n"))

# Calculate
miles = hours*speed
laps = int(miles/3) # Cast to remove decimals

# Output Result
print("Knightro can run ", laps, " lap(s).")