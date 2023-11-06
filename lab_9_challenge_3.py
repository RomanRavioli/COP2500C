# Roman Manuel
# Lab 9 Challenge 3
# COP 2500C Section 5
# Nov 5, 2023

# This function counts in each class how many times we get a better grade than the last grade
def grade_up(grade_list):

    # This creates an empty list that we can store the results in
    results = []

    # Loops through each row of classes
    for row in range(len(grade_list)):

        # Loops through each column of grades
        counter = 0
        for column in range(len(grade_list[row]) - 1):

            # If current grade is better than the next grade, adds 1 to the counter
            if (grade_list[row][column] < grade_list[row][column + 1]):
                counter += 1

        # Stores the count into the results list
        results.append(counter)

    # Returns the results back to main()
    return results


# This defines our main() function
def main():

    # A list with the grades for each class. [I got this from the assignment example]
    Semester = [[95, 92, 93, 96, 92],
                [100, 100],
                [70, 80, 90],
                [95, 85, 75, 70]]

    # Calls the function called "grade_up" and gives it a list called "Semester"
    results = grade_up(Semester)

    # Displays the results
    print(results)




# This starts our program
main()