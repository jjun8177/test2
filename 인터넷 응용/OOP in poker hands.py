suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2, 2+len(ranks))))

deck = []
for i in ranks:
    for j in suits:
        deck.append(i+j)

import random
random.shuffle(deck)
my_card = []
for i in range(5):
    my_cards = deck.pop()
    my_card.append(my_cards)
print(my_card)