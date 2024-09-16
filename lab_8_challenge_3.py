# Roman Manuel
# Lab 8 Challenge 3
# COP 2500C Section 5
# Oct 27, 2023

def joke_splicer(jokes):
    jokes = jokes.split("##\n")
    jokes.sort()
    jokes.pop(0)
    return jokes


def main():
    j = '''1. WHAT DID THE OCEAN SAY TO THE PIRATE? NOTHING, IT JUST WAVED.##
5. HOW DO PIRATES PREFER TO COMMUNICATE? AYE TO AYE!##
3. WHERE CAN YOU FIND A PIRATE WHO HAS LOST HIS WOODEN LEGS? RIGHT WHERE YE LEFT HIM.##
7. HOW DID THE PIRATE GET HIS JOLLY ROGER SO CHEAP? HE BOUGHT IT ON SAIL.##
2. WHY IS PIRATING SO ADDICTIVE? THEY SAY ONCE YE LOSE YER FIRST HAND, YE GET HOOKED.##
4. HOW MUCH DID THE PIRATE PAY FOR HIS PEG AND HOOK? AN ARM AND A LEG.##
6. HOW DO YOU MAKE A PIRATE FURIOUS? TAKE AWAY THE P.##
       '''
    answer = joke_splicer(j)
    print(answer)


main()
