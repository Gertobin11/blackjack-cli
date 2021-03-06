import random
from pyfiglet import Figlet
from termcolor import cprint
from time import sleep


def print_green(x): return cprint(x, 'green')
def print_red(x): return cprint(x, 'red')

f = Figlet(font='nancyj')
card_font = Figlet(font='epic')


def create_deck(coats, symbols, names, values, count, deck):
    """ Function to create a deck"""
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
    return deck


def draw_card(user, deck, *hide):
    """ Function to draw a card from the deck and attach it to the user objects hand,
    and display it if hide was not passed as an arg"""
    card = random.choice(deck)
    user['hand'].append(card)
    if hide:
        return user
    else:
        print_cards(user['hand'])
        return user


def get_username(user):
    """ Function to obtain a username """
    print('Hi, Welcome To BlackJack CLI')
    while True:
        username = input("PLease enter a user_name using letters or numbers more then 3 characters long:  ")
        if validate_username(username) == True:
            break
    user['name'] = username
    return user

def validate_username(username):
    """ Function to return the validated usernames """
    if len(username) < 3:
        print_red('Please enter a username 3 or longer in length')
        return False
    elif username.isalpha():
        return True
    else:
        print_red('Please enter only letters')

def place_bet(user):
    """ Function to return the users bet """
    while True:
        bet = input('Please enter an amount to bet, max bet is 10: ')
        if bet.isnumeric() != True:
            print_red('Please enter a number')
        elif  0 >= int(bet) or int(bet) > 10:
            print_red('Please enter a number between 1 and 10')
        else:
            user['money'] -= int(bet)
            return bet


def game_start(user, dealer):
    """ Function for the initial part of the game where the deck is created and first cards are drawn """
    print_green('Game Starting...')
    sleep(0.5)
    print_green('Deck Shuffled')
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    names = ['ace', 'two', 'threes', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'jack', 'queen', 'king']
    coats = ['hearts', 'spades', 'diamonds', 'clubs']
    symbols = ['\u2665', '\u2660', '\u2666', '\u2663' ]
    deck = []
    count = 0
    deck = create_deck(coats, symbols, names, values, count, deck)
    sleep(0.5)
    bet = place_bet(user)
    print('\n')
    print('Dealer gets a card..')
    draw_card(dealer, deck)
    print('\n')
    sleep(1)
    print('Player draws a card')
    draw_card(user, deck)
    sleep(1)
    print('Dealer gets another card..')
    draw_card(dealer, deck, 'hide')
    print(f'It remains face down.......')
    sleep(1)
    print('Player draws a nother card')
    draw_card(user, deck)
    print('\n')
    print_green('Your hand is...')
    print_cards(user['hand'])
    sleep(1)
    player_hand_value = calculate_hand_value(user["hand"])
    print_green('The value of your hand is.....')
    print(player_hand_value)
    print('\n')
    if int(player_hand_value) == 21:
        print_green(f.renderText('BlackJack'))
        print('\n')
        print_green(f'Congratulations {user["name"]} you won!')
        user['money'] += (int(bet) * 2)
        print('\n')
        print_green(f"Your balance is {user['money']}")
        play_again(user, dealer)
    print('\n')
    sleep(1.5)
    print('The Dealers visible card is')
    print_cards(dealer['hand'][:1])
    dealer_hand_value = calculate_hand_value(dealer['hand'][:1])
    print_green('The value of the dealers hand is....')
    print(dealer_hand_value)
    print('\n')
    stick_twist(user, dealer, bet, deck)

def print_cards(hand):
    # Made it dynamic so will print the same no atter the amount of cards
    for _ in hand:
        print(' _____', end=' ')
    print('')
    for card in hand:
        # Getting the face cards and printing their symbols
        if card['name'].startswith('a') or card['name'].startswith('k'):
            print(f"|{card['name'][0].upper()}-{card['symbol']}", end=' | ')
        elif card['name'].startswith('j') or card['name'].startswith('q'):
            print(f"|{card['name'][0].upper()}-{card['symbol']}", end=' | ')
        # Removing a space at the end of 10 cards to maintain the strusture of the printed card
        elif card['value'] == 10:
            print(f"|{card['value']}-{card['symbol']}", end="| ")
        else:
            print(f"|{card['value']}-{card['symbol']}", end=" | ")
    print('')
    for _ in hand:
        print('|    |', end=' ')
    print('')
    for _ in hand:
        print('|    |', end=' ')
    print('')
    for card in hand:
        # Getting the face cards and printing their symbols
        if card['name'].startswith('a') or card['name'].startswith('k'):
            print(f"|{card['name'][0].upper()}-{card['symbol']}", end=' | ')
        elif card['name'].startswith('j') or card['name'].startswith('q'):
            print(f"|{card['name'][0].upper()}-{card['symbol']}", end=' | ')
        # Removing a space at the end of 10 cards to maintain the strusture of the printed card
        elif card['value'] == 10:
            print(f"|{card['value']}-{card['symbol']}", end="| ")
        else:
            print(f"|{card['value']}-{card['symbol']}", end=" | ")
    print('')
    for _ in hand:
        print('------', end=' ')
    print('\n')

def calculate_hand_value(hand):
    """ Returns the total of the hand"""
    total = 0
    for card in hand:
        total += int(card['value'])
    return total

def dealer_2nd_card_reveal(dealer, dealers_score):
    """ Function to show the dealers second card which is faced down"""
    if len(dealer['hand']) == 2:
        print('The Dealer turns his second card...')
        print_cards(dealer['hand'])
        print_green('The dealers hand is ....')
        print(dealers_score)
        print('\n')
    

def stick_twist(user, dealer, bet, deck):
    """ Function where the player decides on whether to stick with his cards or recieve another"""
    user['stick'] = 'no'
    dealer['stick'] = 'no'
    while True:
        if user['stick'] == 'no':
            choice = input('Do you want another card? y/n :' )
        dealers_score = calculate_hand_value(dealer['hand'])
        sleep(1.5)
        if choice.lower() == 'y' and user['stick'] != 'yes':
            dealer_2nd_card_reveal(dealer, dealers_score)
            draw_card(user, deck)
        elif choice.lower() == 'n':
            user['stick'] = 'yes'
            dealer_2nd_card_reveal(dealer, dealers_score)
        else:
            print_red('Please enter y or n ')
        sleep(0.5)
        if calculate_game_over(user['hand']):
            print('\n')
            print(f'Unlucky {user["name"]} you went Bust your score was over 21')
            print_red(f"Your balance is {user['money']}")
            play_again(user, dealer)
        sleep(0.5)
        if int(dealers_score) <= 16:
            print('The Dealer turns his next card...')
            draw_card(dealer, deck)
            if calculate_game_over(dealer['hand']):
                print_green(f'Congratulations {user["name"]} won, The Dealer went Bust')
                user['money'] += (int(bet) * 2)
                print('\n')
                print_green(f"Your balance is {user['money']}")
                play_again(user, dealer)
        else:
            dealer['stick'] = 'yes'
        sleep(1.5)
        
        # If the player and user stick with their cards this determines the winner 
        if user['stick'] == 'yes' and dealer['stick'] == 'yes':
            if int(calculate_hand_value(user['hand'])) > int(calculate_hand_value(dealer['hand'])):
                print_green(f'Congratulations {user["name"]} won')
                print_cards(user['hand'])
                print_green('BEATS')
                print_cards(dealer['hand'])
                user['money'] += (int(bet) * 2)
                print('\n')
                print_green(f"Your balance is {user['money']}")
                play_again(user, dealer)
            else:
                print_red(f"Unlucky {user['name']} but the dealer won this time")
                print_cards(dealer['hand'])
                print_red('BEATS')
                print_cards(user['hand'])
                print('\n')
                print_red(f"Your balance is {user['money']}")
                play_again(user, dealer)
        print('end')


def calculate_game_over(hand):
    """ Checks to see if the player / dealer is bust """
    total = calculate_hand_value(hand)
    if int(total) > 21:
        # Reassigns the value of an ace to 1 if the player/ dealer is bust
        for card in hand:
            if card['name'].startswith('a'):
                card['value'] = 1
        total = calculate_hand_value(hand)
        if int(total) > 21:
            return True
    else:
        return False

def play_again(user, dealer):
    """ Allows user to restart or quit the game """
    user['hand'] = []
    dealer['hand'] = []
    while True:
        replay = input('Do you want to play again? y/n: ')
        if replay.lower() == 'y':
            game_start(user, dealer)
        elif replay.lower() == 'n':
            if user['money'] == 100:
                print('You broke evem!')
            elif user['money'] > 100:
                profit = user['money'] - 100
                print_green(F"Congratulations you made a profit of {profit}")
            else:
                loss = 100 - user['money']
                print_red(f"Unlucky you made a loss of {loss}")
            quit()
        else:
            print('Please enter y or n ')
    

def main():
    """ Start the game """

    user = {
        'name': '',
        'money': 100,
        'hand': []
    }
    dealer = {
        'hand': [],
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
