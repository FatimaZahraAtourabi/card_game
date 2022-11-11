from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit,rank)
                self.add_card(card)
            

    def __str__(self):
        str_card=''
        for card in self.cards:
            str_card += ' | ' + str(card) 
        str_card += ' | '
        return str_card
           
    def __len__(self):
         return len(self.cards)

    def add_card(self,card):
        return self.cards.append(card)

    def shuffle(self):
        shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop(0)

d=Deck()
print(d)      
print(len(d.cards))   
print(shuffle(d.cards))