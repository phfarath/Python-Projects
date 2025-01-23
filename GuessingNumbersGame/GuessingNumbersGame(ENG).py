# 1. generating random numbers of X digits

# 2. repetitive structure

# 3. inputs for guessing the number

# 4. treating possible unwelcome inputs

# 5. showing the current guess

# 6. if correct, end of the game

import random

# chosen number of digits
x = 3

# creating a list with x random numbers ('_' is a variable only for this list, we are not going to use it)
passcode = [str(random.randint(0, 9)) for _ in range(x)]
guessing_tries = [('_') for _ in range(x)]

attempt = []

# while true
while True:
    attempt = input(f'Digite um número de {x} dígitos: ')

    # treating unwelcome inputs as different than x and letters 
    if len(attempt) != x or not attempt.isdigit():
        print(f'\033[91mDigite {x} números válidos!\033[0m')
        continue

    # converting to list 
    attempt = list(attempt)

    # printing your current guess
    print('------------------------------')
    print('Sua tentativa é : ')
    print(attempt)
    print('------------------------------')

    # if the numbers are correct, fill the list up with the their indexes, keeping their correct position
    for index, numero in enumerate(attempt): 
        if numero == attempt[index]:
            guessing_tries[index] = numero

    # showing the correct numbers of the guess
    print(f'Números corretos: {guessing_tries}') 

    # if the guess is correct
    if guessing_tries == passcode:
        print('\033[92mVocê acertou! Parabéns!\033[0m')
        break # end of the program