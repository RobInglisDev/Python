import random

print('---------------------------------------------')
print('-             GUESS THE NUMBER              -')
print('---------------------------------------------')

mynum = random.randint(0, 100)
guess = -1

while guess != mynum:
    guess_txt = input('Guess the number that I am thinking of....(' + str(mynum)+')  ')
    guess = int(guess_txt)
    if guess < mynum:
        print('Too Low')
    elif guess > mynum:
        print('Too High')
    else:
        print('WELL DONE, YOU WIN!')
