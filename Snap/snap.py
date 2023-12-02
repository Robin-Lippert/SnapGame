from deckOfCards import DeckOfCards
from extraClasses import (Player, PlayDeck)
import pygame
import random

random.seed(random.SystemRandom().random())

players = []

def getNumberOfPlayers():
    try:
        numberOfPlayers = int(input("How many players? "))
    except:
        print("please use a whole number")
        numberOfPlayers = getNumberOfPlayers()
    return numberOfPlayers

def getPlayerNames(numberOfPlayers):
    for player in range(numberOfPlayers):
        players.append(Player(input(f"What is player {player + 1}s Name? ")))

deck = DeckOfCards()

deck.shuffle()

playPile = PlayDeck()

#getPlayerNames(getNumberOfPlayers())

#deck.deal(players)

pygame.init()
screen = pygame.display.set_mode((480, 720))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    '''
    for player in players:
        if  len(player.cards) == 0 and len(playPile.cards) == 0:
            players.remove(player)

    if len(players) < 2:
        break

    for index,  player in enumerate(players):
        if len(player.cards) == 0: continue
        playPile.takeOneCardFromOther(player)
       
        print(playPile.cards[-1], player.name)
        #playPile.cards[-2].__str__()
        if playPile.topCardsSame:
            print(players)
            random.seed(random.SystemRandom().random())
            randomPlayer = random.choice(players)
            
            playPile.deal([randomPlayer])
            print(f"{randomPlayer.name} wins this round\n")
            for player in players:
                print(f"{player.name} has {len(player.cards)} cards\n")
            print(f"{len(playPile.cards)} are in the pile")
    '''
    pygame.display.flip()
    clock.tick(60)
    


    
    

for player in players:
    print(f"{player.name} has {len(player.cards)} cards")

print(players[0].name, "wins")
