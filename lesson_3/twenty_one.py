import os
import random

SUITS = ['hearts', 'spades', 'diamonds', 'clubs']
CARDS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9':9,
        '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
STAY = {'stay', 's'}
HIT = {'hit', 'h'}
HUMAN = 'Your'
DEALER = 'The dealer'

def prompt(message):
    print(f'==> {message}')

def initialize_deck():
    return {suit: {card: card_value for card, card_value in CARDS.items()}
                                    for suit in SUITS}

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
    prompt(f'{DEALER} has: {computer_cards[0]} and unknown card')

    human_cards = [key for value in human.values()
                    for key in value.keys()]
    prompt(f'You have: {human_cards[0]} and {human_cards[1]}')
    print()

def update_hand(card, hand_value, player):
    prompt(f'The card was a {card}')
    prompt(f'{player} current total is {hand_value}.')
    print()

def calculate_hand(hand):
    if not ace_in_hand(hand):
        return sum([card_value for suit in hand.values()
                for card_value in suit.values()])

    adjust_aces(hand)

    return sum([card_value for suit in hand.values()
                for card_value in suit.values()])

def adjust_aces(hand):
    sub_total = sum([card_value for suit in hand.values()
                                for card_value in suit.values()])

    for suit, cards in hand.items():
        for card, value in cards.items():
            if card == 'Ace' and value == 1:
                if sub_total + 10 <= 21:
                    hand[suit][card] = 11


def ace_in_hand(hand):
    return [card for suit in hand.values()
            for card in suit.values()
            if 'Ace' in suit.keys()]

def human_turn(human_hand, deck):
    while True:
        prompt("Enter 'h' to hit or 's' to stay")
        choice = input()

        while choice.casefold() not in STAY and choice.casefold() not in HIT:
            prompt("Invalid input. h to hit or s to stay")
            choice = input()

        if choice.casefold() in STAY:
            total = calculate_hand(human_hand)
            os.system('clear')
            break

        if choice.casefold() in HIT:
            new_card = choose_card(human_hand, deck)
            total = calculate_hand(human_hand)
            update_hand(new_card, total, HUMAN)
            if total > 21:
                break

    return total

def computer_turn(computer_hand, deck):
    total = calculate_hand(computer_hand)
    while total < 17:
        prompt(f'{DEALER} hits!')
        new_card = choose_card(computer_hand, deck)
        total = calculate_hand(computer_hand)
        update_hand(new_card, total, DEALER)

    return total

def bust_check(score):
    if score > 21:
        return True
    return False

def declare_winner(human_score, computer_score):
    print()
    if human_score > computer_score:
        prompt('You win!')
        prompt(f'You: {human_score} Dealer: {computer_score}')
    elif computer_score > human_score:
        prompt(f'{DEALER} wins!')
        prompt(f'You: {human_score} Dealer: {computer_score}')
    else:
        prompt(f'You both have: {human_score}')
        prompt('Draw!')

def display_final_hands(player_hand, computer_hand):
    lst_player_hand = [f'{card} of {suit}' 
                        for suit, cards in player_hand.items()
                        for card in cards.keys()]
    
    lst_computer_hand = [f'{card} of {suit}' 
                        for suit, cards in computer_hand.items()
                        for card in cards.keys()]
    
    prompt(f'{HUMAN} hand: {', '.join(lst_player_hand)}')
    prompt(f"{DEALER}'s hand: {', '.join(lst_computer_hand)}")


def play_again():
    prompt("Play again? Enter y or n")
    answer = input().casefold()
    while answer not in {'y', 'yes', 'n', 'no'}:
        prompt('Invalid input. Enter y or n')
        answer = input().casefold()

    if answer in {'y', 'yes'}:
        os.system('clear')
        return True
    return False


def play_hand():
    while True:
        deck = initialize_deck()
        human_hand = deal_hand(deck)
        computer_hand = deal_hand(deck)

        display_initial_hand(human_hand, computer_hand)

        human_total = human_turn(human_hand, deck)
        if bust_check(human_total):
            prompt(f'You busted! {DEALER} wins.')
            break

        computer_total = computer_turn(computer_hand, deck)
        if bust_check(computer_total):
            prompt(f'{DEALER} busted! You win!')
            break
        
        display_final_hands(human_hand, computer_hand)
        declare_winner(human_total, computer_total)
        break


def play_twenty_one():
    while True:
        play_hand()
        answer = play_again()
        if not answer:
            break

play_twenty_one()
