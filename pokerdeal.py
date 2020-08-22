import random

class Card:
    def __init__(self, num, suit):
        self.n = num
        self.s = suit
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

nums = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["H","D","C","S"]
numnums = len(nums)
numsuits = len(suits)

def gencard():
    suitc = random.choice(suits)
    numc = random.choice(nums)
    card = Card(numc,suitc)
    print(card.n,card.s)
    return(card)

def genhand():
    hand = []
    numcards = input("How many cards?")
    print("Card Generation (Allows duplicates)")
    for i in range(0,int(numcards)):
        carddraw = gencard()
        if carddraw in hand:
            i = i
        else: hand.append(carddraw)
    print("")
    print("Hand (unique cards):")
    print(','.join(str(card.n)+str(card.s) for card in hand))
genhand()