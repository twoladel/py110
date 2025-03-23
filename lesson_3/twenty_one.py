'''
P-
Two players - user and computer
four cards dealt, three exposed (one dealer card hidden)
user always first
Dealter hits until cards >= 17
Either player busts == game over
No bust calculate the highest total
Ace can be 1 or 11
    have to determine the value of an Ace each time a new card is dealt
    to a hand containing an Ace. Complex if multiple Aces (each could be diff)


D-
dict called cards:
    nested dicts for each suit (4)
        each suit dict will have cards as keys A thru 2 and num value as values
Randomly deal cards
    how to use random module with dicts?
    when card is dealt it shoud be removed from the dict
hands should be stored as dicts
    update hand dict with key: value pair chosen (face and value)
sum hand_dict.values() to track both players scores


A- 
Initiallize deck (nested dict comprehension)
Deal four cards alternating between human and computer
    UI: one of dealers cards will display unknown, but program knows the value.
wait for player input to hit or stay
    hit requires another card (helper function)
    recalculate total
        if bust end hand
    wait for player to choose again
        (while loop with a break statement?) if stay: break
computer hits below 17
    hit requires another card (same helper function)
    recalculate total
        if bust end hand
    decide again
        same while loop till break
compare cards and decide winner
'''
import random

SUITS = ['hearts', 'spades', 'diamonds', 'clubs']
# TODO: change ace back to a list with 1 and 11
CARDS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9':9,
        '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
STAY = {'stay', 's'}
HIT = {'hit', 'h'}

def prompt(message):
    print(f'==> {message}')

def initialize_deck():
    return {suit: {card: CARDS[card] for card in CARDS} for suit in SUITS}

def choose_card(hand, deck):
    suit = random.choice(list(deck.keys()))
    if suit not in hand:
        hand[suit] = {}
    card = random.choice(list(deck[suit].keys()))
    hand[suit][card] = deck[suit][card]
    del deck[suit][card]
    return card

def deal_hand(deck):
    hand = {}
    for _ in range(2):
        choose_card(hand, deck)
    return hand

def display_initial_hand(human, computer):
    print()
    computer_cards = [key for value in computer.values()
                        for key in value.keys()]
    prompt(f'Dealer has: {computer_cards[0]} and unknown card')

    human_cards = [key for value in human.values()
                    for key in value.keys()]
    prompt(f'You have: {human_cards[0]} and {human_cards[1]}')
    print()

def update_hand(card, hand_value):    
    prompt(f'The card was a {card}')
    prompt(f'The current total is {hand_value}.')

def calculate_hand(hand):
    # TODO: add Ace value handling in here
    return sum([value for value in hand.values()
                for value in value.values()])

def human_turn(human_hand, deck):
    while True:
        prompt("Enter 'h' to hit or 's' to stay")
        choice = input()

        while choice.casefold() not in STAY and choice.casefold() not in HIT:
            prompt("Invalid input. h to hit or s to stay")
            choice = input()

        if choice.casefold() in STAY:
            total = calculate_hand(human_hand)
            break

        if choice.casefold() in HIT:
            new_card = choose_card(human_hand, deck)
            total = calculate_hand(human_hand)
            update_hand(new_card, total)
            if total > 21:
                break

    return total

def computer_turn(computer_hand, deck):
    total = calculate_hand(computer_hand)
    while total < 17:
        new_card = choose_card(computer_hand, deck)
        total = calculate_hand(computer_hand)
        update_hand(new_card, total)
    
    return total

def bust_check(score):
    if score > 21:
        return True
    return False

def declare_winner(human_score, computer_score):
    if human_score > computer_score:
        prompt('You win!')
    elif computer_score > human_score:
        prompt('Dealer wins!')
    else:
        prompt('Draw! A draw goes to the dealer.')

def play_twenty_one():
    while True:
        deck = initialize_deck()
        human_hand = deal_hand(deck)
        computer_hand = deal_hand(deck)

        display_initial_hand(human_hand, computer_hand)
        human_total = human_turn(human_hand, deck)
        if bust_check(human_total):
            prompt(f'You busted! Dealer wins.')
            break
        computer_total = computer_turn(computer_hand, deck)
        if bust_check(computer_total):
            prompt('The Dealer busted! You win!')
            break
        declare_winner(human_total, computer_total)
        break

play_twenty_one()

