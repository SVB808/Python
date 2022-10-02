def sums(a, b, c): 
    return a+b+c

def printBoard(xstate, ostate):
    zero = 'X' if xstate[0] else ('O' if ostate[0] else 0)
    one = 'X' if xstate[1] else ('O' if ostate[1] else 1)
    two = 'X' if xstate[2] else ('O' if ostate[2] else 2)
    three = 'X' if xstate[3] else ('O' if ostate[3] else 3)
    four = 'X' if xstate[4] else ('O' if ostate[4] else 4)
    five = 'X' if xstate[5] else ('O' if ostate[5] else 5)
    six = 'X' if xstate[6] else ('O' if ostate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if ostate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if ostate[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f" {three} | {four} | {five} ")
    print(f" {six} | {seven} | {eight} ")

def winner(xstate, ostate):
    wins= [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for w in wins: 
        if(sums(xstate[w[0]], xstate[w[1]], xstate[w[2]]) == 3):
            print("X won the game!")
            return 1
        if(sums(ostate[w[0]], ostate[w[1]], ostate[w[2]]) == 3):
            print("O won the game!")
            return 0
    return -1

if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ostate = [0, 0 , 0, 0, 0, 0, 0, 0, 0]
    turn = 1 #1 for X and 0 for O
    while(True):
        if(sum(ostate)+sum(xstate)== 9):
            printBoard(xstate, ostate)
            print("It's a draw!")
            break
        printBoard(xstate, ostate)
        if turn == 1:
            print("X's chance: ")
            position = int(input("Enter position: "))
            while(ostate[position] == 1):
                print("Invalid position!")
                position = int(input("Enter a valid position: "))
            xstate[position] = 1
        else:
            print("O's chance: ")
            position = int(input("Enter position: "))
            while(xstate[position] == 1):
                print("Invalid position!")
                position = int(input("Enter a valid position: "))
            ostate[position] = 1
        a=winner(xstate, ostate)
        if(a != -1):
            printBoard(xstate, ostate)
            print("Game complete!")
            break
        turn = 1 - turn 