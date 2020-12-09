# This is a guess the number game. 
import random
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times. 
for guess_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is to low.')
    elif guess > secret_number:
        print('Your guess is to high.')
    else:                                   # if it isn't too high or too low, it must be the correct number. 
        break 

if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guess_taken) + ' guesses.')
else: 
    print('Nope. The number I was thinking of was ' + str(secret_number))

