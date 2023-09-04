import random

dice = random.randint(1,6)
print(dice)
guess =int (input('Guess the Roll dice?\n'))
while guess != dice:
    print("Try again")
    guess = int(input('Guess the Roll dice?\n'))
else:
    print('Your Guess Is true')

# if guess == dice:
#     print('Your Guess Is true')
# else:
#     print('Your Guess is wrong the dice was',dice)