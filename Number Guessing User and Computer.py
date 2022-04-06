import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        #print(guess)
        if guess < random_number:
            print('Sorry the number is too low so guess again')
        elif guess > random_number:
            print('Sorry too high guess again')
    print('Congarts You have guessed correct number: ' + str(random_number))


def c_guess(x):
    low = 1
    high = x
    fback = ''
    while fback != 'C' and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        fback = input(f'Is {guess} too high (H), too low (L), Correct (C)??').lower()
        if fback == 'h':
            high = guess - 1
        elif fback == 'l':
            low = guess + 1
    print(f'The computer guessed your number, {guess}, correctly!')

c_guess(10)
guess(10)