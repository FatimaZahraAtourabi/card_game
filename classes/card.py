class Card:
    suits = ['C','D','H','S']
    ranks = ['2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']

    def __init__(self,suit, rank):                          #suit est l'index de l'élément dans la liste suits ( same for rank)
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suits[self.suit] + self.ranks[self.rank]

    def __lt__(self,other):
        if self.suit != other.suit:
            return self.suit < other.suit
        return self.rank < other.rank    
        
        


c =Card(2,12)
c1 =Card(0,3)
c2 = Card(2,12)
c3 = Card(2,11)
print(c)
c1 > c2
c3 < c2


