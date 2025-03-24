import random

SUITS = ['hearts', 'spades', 'diamonds', 'clubs']
CARDS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9':9,
        '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
STAY = {'stay', 's'}
HIT = {'hit', 'h'}

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
    prompt(f'Dealer has: {computer_cards[0]} and unknown card')

    human_cards = [key for value in human.values()
                    for key in value.keys()]
    prompt(f'You have: {human_cards[0]} and {human_cards[1]}')
    print()

def update_hand(card, hand_value):
    prompt(f'The card was a {card}')
    prompt(f'The current total is {hand_value}.')

def calculate_hand(hand):
    if not ace_in_hand(hand):
        return sum([card_value for suit in hand.values()
                for card_value in suit.values()])

    adjust_aces(hand)

    return sum([card_value for suit in hand.values()
                for card_value in suit.values()])

def adjust_aces(hand):
    non_ace_total = sum([card_value for suit in hand.values()
                                    for card, card_value in suit.items()
                                    if card != 'Ace'])
    ace_total = sum([card_value for suit in hand.values()
                                    for card, card_value in suit.items()
                                    if card == 'Ace'])
    sub_total = non_ace_total + ace_total

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
    print()
    if human_score > computer_score:
        prompt('You win!')
        prompt(f'You: {human_score} Dealer: {computer_score}')
    elif computer_score > human_score:
        prompt('Dealer wins!')
        prompt(f'You: {human_score} Dealer: {computer_score}')
    else:
        prompt(f'You both have: {human_score}')
        prompt('Draw! A draw goes to the dealer.')

def play_again():
    prompt("Play again? Enter y or n")
    answer = input().casefold()
    while answer not in {'y', 'yes', 'n', 'no'}:
        prompt('Invalid input. Enter y or n')
        answer = input().casefold()

    if answer in {'y', 'yes'}:
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
            prompt('You busted! Dealer wins.')
            break

        computer_total = computer_turn(computer_hand, deck)
        if bust_check(computer_total):
            prompt('The Dealer busted! You win!')
            break

        declare_winner(human_total, computer_total)
        break


def play_twenty_one():
    while True:
        play_hand()
        answer = play_again()
        if not answer:
            break

play_twenty_one()

# TODO: Different messages for player and dealer when getting cards
# Announce Dealer hits! 
# Best of 5 and then reset?
# Clean up the UI os.system clear jawn