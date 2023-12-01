import random
import math

class Card:

    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    def get_info(self):
        return[self.rank, self.suit, self.colour]
    
    def __str__(self):
        return f"{self.rank} of {self.suit} {self.uniCard}"
    
    @property
    def rank(self):
        return self.__rank
    
    @property
    def suit(self):
        return self.__suit
    
    @property
    def colour(self):
        match self.suit:
            case "Hearts" | "Diamonds":
                return "Red"
            case "Spades" | "Clubs":
                return "Black"
            
    @property
    def uniCard(self):
        _card = 0x1F000
        match self.suit:
            case "Spades":
                _card += 0xA0
            case "Hearts":
                _card += 0xB0
            case "Diamonds":
                _card += 0xC0
            case "Clubs":
                _card += 0xD0
        match self.rank:
            case "Ace":
                _card += 0x1
            case "2":
                _card += 0x2
            case "3":
                _card += 0x3
            case "4":
                _card += 0x4
            case "5":
                _card += 0x5
            case "6":
                _card += 0x6
            case "7":
                _card += 0x7
            case "8":
                _card += 0x8
            case "9":
                _card += 0x9
            case "10":
                _card += 0xA
            case "Jack":
                _card += 0xB
            case "Queen":
                _card += 0xD
            case "King":
                _card += 0xE
        #print(_card)
        
        return chr(_card)
            
      

class DeckOfCards:

    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    ranks = ("Ace", "2", "3", "4","5","6","7","8","9","10","Jack","Queen","King")

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))
    '''
    def createDeck(self):
        if not self.cards == []: 
            print("Deck already created")
            return
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))'''

    def __str__(self):
        return str(self.cards[0])

    def displayCards(self):
        'Prints every card'
        for card in self.cards:
            print(card.uniCard)

    def displayCardsInfo(self):
        for card in self.cards:
            print(card.get_info())
    
    def shuffle(self):
        random.shuffle(self.cards)

    def append(self, card):
        self.cards.append(card)

    def deal(self, players):
        numberOfPlayers = len(players)
        cardsPerPlayer = math.ceil(len(self.cards) /numberOfPlayers)
        
        deal_list = []

        for cards in range(cardsPerPlayer):
            for hand in range(numberOfPlayers):
                if len(self.cards) == 0: return deal_list
                players[hand].append(self.cards.pop(0))
                

        return deal_list

        print(cardsPerPlayer)

    def takeOneCardFromOther(self, other):
        self.append(other.cards.pop(0))

    @property
    def topCardsSame(self):
        if (len(self.cards) < 2): return False
        return (self.cards[-1].rank == self.cards[-2].rank)
            


        