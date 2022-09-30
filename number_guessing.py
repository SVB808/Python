import random as r
n = r.randrange(1,10)
chance = 10
guess = int(input("Enter any number: "))
while (n!= guess & chance>0):
    if guess < n:
        print("Too low")
        chance -= 1
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        chance -= 1
        guess = int(input("Enter number again: "))
    else:
      print("You guessed it right!")
      chance -= 1
      break
if(chance == 0):
    print("You lost the game :(")
