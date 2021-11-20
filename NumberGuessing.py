print('Number Guessing Game')
print('Enter a number between 1-9 :-')

firstGuess=int(input('Enter your first guess '))

if (firstGuess==5):
    print("Superb! You guessed the Number !!!")
elif (firstGuess<4):
    print("Too low, try a higher number...")
elif (firstGuess==4):
    print("Close... Keep trying")
elif (firstGuess==6):
    print("Close... Keep trying")
elif (firstGuess>6):
    print("Too far, try a lower number...")