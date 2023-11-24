# Roman Manuel
# Lab 10 Challenge 3
# COP 2500C Section 5
# Nov 19, 2023

def main():
    database = [{}, {}, {}, {}, {}]
    file = open("Lab10.csv", "r")
    for i in range(5):
        line = file.readline().strip("\n")
        line = line.split(",")
        dictionary = {}
        dictionary["course_code"] = line[0]
        dictionary["course_name"] = line[1]
        dictionary["credit_hours"] = line[2]
        dictionary["teacher"] = line[3]
        dictionary["grade"] = line[4]
        database[i] = dictionary
        print("\nDictionary #" + str(i + 1) + ":")
        for key in dictionary:
            print(str(key).title() + ": " + str(dictionary[key]))
    file.close()
main()