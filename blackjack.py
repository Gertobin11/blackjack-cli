import random
from pyfiglet import Figlet
from termcolor import cprint


def print_green(x): return cprint(x, 'green')
def print_red(x): return cprint(x, 'red')

f = Figlet(font='nancyj')
card_font = Figlet(font='epic')
number = 1


values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

names = ['ace', 'two', 'threes', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'jack', 'queen', 'king']

coats = ['hearts', 'spades', 'diamonds', 'clubs']

symbols = ['\u2665', '\u2660', '\u2666', '\u2663' ]

deck = []

count = 0

max_bet = 10

# loop though the coats and names and apply them to the deck
for coat in coats:
    for name in names:
        deck.append({'name': name,
                     'coat': coat})


# loop through the deck applying values  and symbols to the cards
for i in range(4):
    for n in range(len(values)):
        deck[count]['value'] = values[n]
        deck[count]['symbol'] = symbols[i]
        count += 1

print(deck)

def draw_card():
    card = random.choice(deck)
    return card


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

def place_bet(user):
    while True:
        bet = input('Please enter an amount to bet, max bet is 10: ')
        if bet.isnumeric() != True:
            print_red('Please enter a number')
        elif  0 > int(bet) > 10:
            print_red('Please enter a number between 1 and 10')
        else:
            user['money'] -= int(bet)
            return bet


def game_start(user, dealer):
    print_green('Game Starting...')
    bet = place_bet(user)
    print('\n')
    print('Dealer gets a card..')
    dealer_card_one = draw_card()
    dealer['hand'].append(dealer_card_one)
    print(f'It is the {dealer_card_one["name"]} of {dealer_card_one["coat"]}')
    print('\n')
    player_card_one = draw_card()
    user['hand'].append(player_card_one)
    print('Player draws a card')
    print(f'It is the {player_card_one["name"]} of {player_card_one["coat"]}')
    print('Dealer gets another card..')
    dealer_card_two = draw_card()
    dealer['hand'].append(dealer_card_two)
    print(f'It remains face down.......')
    player_card_two = draw_card()
    user['hand'].append(player_card_two)
    print('Player draws a nother card')
    print(f'It is the {player_card_two["name"]} of {player_card_two["coat"]}')
    print('\n')
    for card in user['hand']:
        if card['name'].startswith('a'):
            print(f"{card['name'][0]} -  {card['symbol']}", end=' | ')
        else:
            print(f"{card['value']} - {card['symbol']}", end=" | ")
    print('\n')
    hand_value = int(player_card_one['value']) + int(player_card_two['value'])
    print(f" Younr hand value is {hand_value}")




def main():
    user = {
        'name': '',
        'money': 100,
        'hand': []
    }
    dealer = {
        'hand': []
    }
    print_green(f.renderText('BlackJack CLI'))
    get_username(user)
    print('\n')
    print(f"Welcome {user['name']}")
    print(f'Your opening balance is', end=' ')
    print_green(f'{user["money"]}')
    print('\n')
    game_start(user, dealer)

main()
