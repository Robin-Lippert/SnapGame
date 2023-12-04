from deckOfCards import DeckOfCards
from extraClasses import (Player, PlayDeck)
import pygame
import random
import sys

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
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
base_font = pygame.font.Font(None,32)
user_text = ''

input_rect = pygame.Rect(200,200,140,32)
color_active = pygame.Color('darkblue')
color_pasive = pygame.Color('grey15')
color = color_pasive
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text= user_text[:-1]
            else:
                user_text += event.unicode
    

    screen.fill("purple")

    pygame.draw.rect(screen,color,input_rect,2)

    text_surface = base_font.render(user_text,True,(0,0,0))
    screen.blit(text_surface,(input_rect.x + 5,input_rect.y + 5 ))

    input_rect.w =max(100,text_surface.get_width() + 10) 
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
