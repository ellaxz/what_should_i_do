import random

def start():
    print('Welcome')
    n = ''
    while n.strip() == '':
        n = input('What you wanna do? Please separated by space:')
    lst = n.split(' ')
    print(lst)
    try:
        f = int(input(
            'Is that correct? Please enter 1 if that is correct. Enter 2 if you wanna start again: '))
        if f == 1:
            do = random.choice(lst)
            print(do)
        elif f == 2:
            print('Please enter again')
            start()
    except ValueError:
        print('Wth was that, goodbye.')

start()
