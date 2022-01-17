import random

def guessing_game():
    r = random.randint(0, 100)
    while True:
        x = raw_input('Enter number from 0 to 100: ')
        if x.isdigit():
            i = int(x)
            if r == i:
                _print('correct number')
                break
            elif r < i:
                _print('too high')
            else:
                _print('too low')
        else:
            _print('not a number')

def _print(value):
    print ('You entered ' + value)

guessing_game()