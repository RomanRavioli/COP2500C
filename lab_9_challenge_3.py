# Roman Manuel
# Lab 9 Challenge 3
# COP 2500C Section 5
# Nov 5, 2023

# Original function from Challenge 1
def grade_up(grade_list):
    count = 0
    for i in range(len(grade_list) - 1):
        if (grade_list[i] < grade_list[i + 1]):
            count += 1
    return count


# This function counts in each class how many times we improve our grade
def counter(class_list):

    # This creates an empty list that we can store the results in
    results = []

    # Loops through the grades in each class
    for grades in range(len(class_list)):

        # Calls the grade_up function from Challenge 1
        count = grade_up(class_list[grades])

        # Stores the count into the results list
        results.append(count)

    # Returns the results back to main()
    return results


# This defines our main() function
def main():

    # A list with the grades for each class. [I got this from the assignment example]
    Semester = [ [95, 92, 93, 96, 92], [100, 100], [70, 80, 90], [95, 85, 75, 70] ]

    # Calls the function called "grade_up" and gives it a list called "Semester"
    results = counter(Semester)

    # Displays the results
    print(results)


# This starts our program
main()