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

def is_flush(cards):
    x = []
    for i in cards:
        x.append(i[1])
    y = set(x)
    if len(y) == 1 : 
        return True
    else :
        return False
    pass
    
def is_straight(cards):
    x = []
    for i in cards:
        x.append(values[i[0]])
        if max(x) - min(x) == 4:
            return 'Straight'
        else:
            return False
    pass
    
def classify_by_rank(cards):
    rank_dic = {}
    for i in ranks:
        x = []
        for j in cards:
            if j[0] == i:
                x.append(j)
            rank_dic[i] = x
    return rank_dic
    pass

def find_a_kind(cards):
    cards_by_ranks = classify_by_rank(cards)
    two_count = 0
    three_count = 0
    for key in cards_by_ranks.keys():
        if len(cards_by_ranks[key]) == 2:
            two_count += 1
        elif len(cards_by_ranks[key]) == 3:
            three_count += 1
        elif len(cards_by_ranks[key]) == 4:
            return 'Four card'
        if (two_count == 1) and (three_count == 1):
            return 'Full house'
        elif (two_count == 0) and (three_count == 1):
            return 'Three of a kind'
        elif (two_count == 1) and (three_count == 0):
            return 'One pair'
        elif (two_count == 2) and (three_count == 0):
            return "Two pair"
        else:
            x = []
            for i in cards_by_ranks.keys():
                if len(cards_by_ranks[i]) > 0:
                    x.append(values.get(i))
            sorted(x)
            y = x[4]
            for key, value in values.items():
                if value == y:
                    return key + str(" top")               
    pass

def tell_hand_ranking(cards):
    countf=0
    counts=0 
    countr=0
    countb=0
    if is_flush(cards) == True:
        countf += 1
        countr += 1
        countb += 1
    if is_straight(cards) == True:
        cards.sort(reverse = True)
        if cards[0][0] == 'T' and cards[4][0] == 'A':
            countr += 1
        elif cards[0][0] == 'A':
            countb += 1
        counts += 1
    if countr == 2:
        return 'royal straight flush'
    elif countb == 2:
        return 'back straight flush'
    elif countf == 1 and counts == 1:
        return 'straight flush'
    elif countf == 1:
        return 'flush'
    elif countb == 1:
        return 'back straight'
    elif counts == 1:
        return 'straight'
    return find_a_kind(cards)
   
if __name__ == "__main__":    # Only if this script runs as a main,
    pass                      # test code here will run.

print("flush : ",is_flush(my_card))
print("straight : ",is_straight(my_card))
print(classify_by_rank(my_card))
print(find_a_kind(my_card))
print(tell_hand_ranking(my_card))
print("---------------------------------------------------")
