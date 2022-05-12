from curses.ascii import isalnum
import random
from pyfiglet import Figlet
from termcolor import cprint


def print_green(x): return cprint(x, 'green')
def print_red(x): return cprint(x, 'red')

f = Figlet(font='nancyj')

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

names = ['one', 'two', 'threes', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'jack', 'queen', 'king', 'ace']

coats = ['hearts', 'spades', 'diamonds', 'clubs']


deck = []

count = 0

# loop though the coats and names and apply them to the deck
for coat in coats:
    for name in names:
        deck.append({'name': name,
                     'coat': coat})

# loop through the deck applying values to the cards
for i in range(4):
    for n in range(len(values)):
        deck[count]['value'] = values[n]
        count += 1

new_pick = random.choice(deck)

print(f'You have picked the {new_pick["name"]} of {new_pick["coat"]}')


def get_username(user):
    print('Hi, Welcome To BlackJack CLI')
    while True:
        username = input("PLease enter a user_name using letters or numbers more then 3 characters long:  ")
        if validate_username(username) == True:
            break
    user['name'] = username
    return user

def validate_username(username):
    if len(username) < 3:
        print_red('Please enter a username 3 or longer in length')
        return False
    elif username.isalpha():
        return True
    else:
        print_red('Please enter only letters')
            



def main():
    user = {
        'name': '',
        'money': 100
    }
    print_green(f.renderText('BlackJack CLI'))
    get_username(user)
    print('\n')
    print(f"Welcome {user['name']}")
    print(f'Your opening balance is', end=' ')
    print_green(f'{user["money"]}')
    


main()
