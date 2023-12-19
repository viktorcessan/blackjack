import random

#Global variables
deck = []
total = 0

def welcome_message():
    print("Welcome to Programmatic Black Jack")

def deck_check():
    print(deck)

def deck_length():
    print("Length of deck: " + str(len(deck)))

def create_deck():
    #creates deck using only integers
    for number in range(1, 5):
        for number in range(1, 11):
            deck.append(number)
    for number in range(1,13):
        deck.append(10)
    random.shuffle(deck)

def start_game():
    create_deck()
    welcome_message()
#    deck_check()
#    deck_length()

start_game()

#todo rework deck_check, and deck_length to automated test that only returns OK or NO.
#todo add a function for dealing cards, and for calculating value using the global variable total

#def calculate_value():
#    #check if value is >21

#def deal_cards():
#    #as long as the total is <= 21 offer more cards
