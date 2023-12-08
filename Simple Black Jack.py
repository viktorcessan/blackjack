print("Welcome to Programmatic Black Jack.")

deck = []
for number in range(1,5):
    for number in range(1, 11):
        deck.append(number)

for number in range(1,13):
    deck.append(10)

print(deck)

import random
random.shuffle(deck)

print(deck)
print(len(deck))