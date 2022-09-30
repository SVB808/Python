import random as r
n = r.randrange(1,10)
chance=int(10)
print("Welcome to the guessing game!\nLet's start!\n")
guess = int(input('Guess the number: '))
while(guess != n & chance>0):
    if(guess>n):
        print("\nGuess is too high!")
        chance -= 1
        guess = int(input('\nGuess the number: '))
    elif(guess<n):
        print("\nGuess is too low!")
        chance -= 1
        guess = int(input('\nGuess the number: '))
    else:
        print('\nYou guessed it right! Congratulations!!')
        break
if(chance == 0):
    print('\nYou lost the game :(')