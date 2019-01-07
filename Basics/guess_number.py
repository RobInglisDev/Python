import random

print('---------------------------------------------')
print('-             GUESS THE NUMBER              -')
print('---------------------------------------------')

mynum = random.randint(0, 100)
guess = -1
name = input('Please enter your name -> ')

while guess != mynum:
    guess_txt = input('Guess the number that I am thinking of....({0}) -> '.format(mynum))
    guess = int(guess_txt)
    if guess < mynum:
        print('Sorry {}, your guess of {} was Too Low'.format(name,guess))
    elif guess > mynum:
        print('Sorry {}, your guess of {} was Too High'.format(name,guess))
    else:
        print('WELL DONE {}, your guess of {} was Correct!'.format(name,guess))
