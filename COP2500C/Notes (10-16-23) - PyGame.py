import random


def print_board(b):
    print()
    print("Board:")

    size = len(b)
    for i in range(size):
        print(b[i], end="")
    print()


def main():

    board = []
    for i in range(8):
        board.append(random.randint(0, 9))
    print_board(board)

    kyle_score = 0
    class_score = 0
    turn = 0

    while (len(board) > 0):
        print("Kyle:", kyle_score, "-vs- Class:", class_score)
        print("It is player #"+str(turn % 2+1)+"'s turn")
        print_board(board)
        side = input("What side do you choose?\n")
        if (side == "left"):
            score = board[0]
            if (turn % 2 == 0):
                kyle_score += score
            else:
                kyle_score += score
            turn += 1
            board.pop(-1)

        print("Final Results")
        print("Kyle:", kyle_score)
        print("Class:", class_score)
        if (kyle_score > class_score):
            print("I told you... He won by", kyle_score-class_score)
        elif (kyle_score == class_score):
            print("You tied")
        else:
            print("Class wins! This will never happen ")


main()
