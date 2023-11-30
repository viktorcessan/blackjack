print("Welcome to Black Jack Town. Do you think you can beat me?!")

# Deck content (suits and ranks). Using [] because the card deck is an ordered, mutable list
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Deck logic
deck = []
for suit in suits:
    for rank in ranks:
        card = (suit, rank)
        deck.append(card)

# Random generator is imported, and used to shuffle the deck. Paranthesis () is used because the deck should be ordered and immutable once shuffled
import random
random.shuffle(deck)

# Automated test that checks to see if all cards are correctly present. Checks for 52 cards.
expected_cards = set((suit, rank) for suit in suits for rank in ranks)
if len(deck) != 52:
    print("Error! The deck does not contain 52 cards. I suggest you don't play, the odds are not in your favor.")
else:
    # Check if all expected cards are in the deck
    if all(card in deck for card in expected_cards):
        print("No cheats detected! The deck is shuffled and all cards are correctly present.")
    else:
        print("Error: Some cards are missing or duplicated. I suggest you don't play, the odds are not in your favor.")

# Defining the players. Game currently only supports one player and the dealer.
player_hand = []
dealer_hand = []

# Card dealing function
def deal_card(deck):
    return deck.pop()

for _ in range(2):
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))

#Logic for calculating hand value that is called upon when dealing the hand
def calculate_hand_value(hand):
    value = 0
    ace_count = 0

    for card in hand:
        suit, rank = card

        if rank in ['J', 'Q', 'K']:
            value +=10
        elif rank == 'A':
            ace_count +=1
            value +=11 #initially counts ace's a 11 in value
        else:
            value += int(rank) #valid for number cards

#Below adjusts the value of aces in case the total value exceeds 21
    while value > 21 and ace_count:
        value -= 10 #this changes the value of an Ace from 11 to 1 (through the -10 function)
    ace_count -= 1
    return value

print("Your hand:", player_hand, "Total value:", calculate_hand_value(player_hand))
print("Dealer's hand: [", dealer_hand[0], ", Hidden]")
