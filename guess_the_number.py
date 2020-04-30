
#This Is A Guess The Number Game.

import random

guessesTaken = 0

print('Hey. What is your name?')
print('')
myName=input()

#Generate random number

secretNumber = random.randint(1,20)
print('')
print('Hey ' + myName + ', I am Guess King, and I am thinking of a number between 1 and 20.')

print('I will give you 5 chances to get it right.')

while guessesTaken < 5:
    print('Take a guess.')
    guess=input()
    guess=int(guess)

    guessesTaken = guessesTaken + 1

    if guess < secretNumber:
        print('Your guess is too low.')

    if guess > secretNumber:
        print('Your guess is too high.')

    if guess == secretNumber:
        break
if guess == secretNumber:
    guessesTaken = str(guessesTaken)
    print('Nice one, ' + myName + ' You guessed my number in ' + guessesTaken + ' guesses.')

if guess != secretNumber:
    secretNumber=str(secretNumber)
    print('Sorry the number I was thinking of was ' + secretNumber)


