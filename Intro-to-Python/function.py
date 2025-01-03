# and introduciion to function and how it makes coding easier and clean

def greeting():
    return 'hello'

print(greeting())

def greatingWithName(name):
    return print(f"hello {name}")

greatingWithName('walon')

#classwork
# guessing game

def guess():
    max_guess = 7
    tries = 0
    guess_value = 7

    while tries < max_guess:
        number = int(input('Enter a number: '))
        if number == guess_value:
            print('correct')
            break
        else:
            print('wrong')
            pass
        tries += 1

guess()