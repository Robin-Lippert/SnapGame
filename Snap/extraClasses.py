from deckOfCards import *



class Player(DeckOfCards):
    
    def __init__(self, name):
        self.cards = []
        self.name = name
        
        


class PlayDeck(DeckOfCards):
    playerCount = int()

    def __init__(self):
        self.cards = []

    ''' @property
    def topCardsSame(self):
        if (self.cards[-1] == self.cards[-2]):
            return True
        else:
            return False'''
        


        
    