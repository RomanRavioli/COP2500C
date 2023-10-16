# Roman Manuel
# String Notes
# COPY 2500C Section 5
# Oct 16, 2023

def first_part():
    name = "       Kyle SteVen DenCker"
    other = "kyle steven dencker"

    # Cleaning data is the process of converting it to a useable format
    # Puts all of name lower case
    a = name.lower()
    print(a, name)

    # Puts all the letters uppercase
    a = name.upper()
    print(a)

    # First letter is capital and everything else is lower
    a = name.capitalize()
    print(a)

    a = name.title()
    print(a)

    # Strip command - It remmoves whitespace before and after the string
    a = name.strip()
    print(a)

    clean = name.strip().upper()
    print(clean)

    words = clean.split()
    print(words)

    # Get the size of the list
    size = len(words)
    for i in range(1, size, 2):
        words[i] = words[i].lower()
    print(words)

    for i in range(size):
        if(i%2 == 0):
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    print(words)

    rebuild = ""
    # For each loop
    for w in words:
        rebuild += w + " "
    print(rebuild)

    if (name.lower() == other):
        print("They are the same")
    else:
        print("These are different")

def main():
    # first_part()

    # Substrings
    name = "Kyle STEVEN Dencker"

    # Gets a single letter
    a = name[7]
    print(a)
    a = name[2]
    print(a)

    count = 0
    for letter in name:
        if letter.lower() == "e":
            count += 1
    print(count)

    # Goes from 1 to 7, does not include 7
    print(name[1:7])

    # Goes from the beginning to 7
    print(name[:7])

    # Goes from 7 to the end
    print(name[7:])

    a = name.find("Den")
    print(a)

    first = name[:a]
    middle = "Sir McMuffin"
    last = name[a+3:]

    new_name = first+middle+last
    print(new_name)

main()