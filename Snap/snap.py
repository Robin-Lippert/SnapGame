from deckOfCards import DeckOfCards
from extraClasses import (Player, PlayDeck)
import pygame
import random
import sys
from inputBox import InputBox , PlayerButton
import time
 
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


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


def displayTextCenter(surface, text, ypos, font, color):
    text_surface = font.render(text, True, color)
    text_width = text_surface.get_width()

    surface.blit(text_surface, (screen.get_width() / 2 - text_width /2 , ypos))

def displayText(surface, text, pos, font, color):
    text_surface = font.render(text, True, color)
    text_width = text_surface.get_width()

    surface.blit(text_surface, pos)

def howManyPlayers():

    textYPos = 50
    fontSize = 48
    introText1 = "Welcome to Snap"
    introText2 ="Please select how many players there are"

    screenWidth = screen.get_width()

    buttonWidth, buttonHeight = 175, 60

    base_font = pygame.font.Font(None,fontSize)

    two_player = PlayerButton('2 Players' ,pygame.Rect(screenWidth / 2 - buttonWidth/2, textYPos + buttonHeight*2, buttonWidth, buttonHeight), base_font,2)
    three_player = PlayerButton('3 Players' ,pygame.Rect(screenWidth / 2 - buttonWidth/2, textYPos + buttonHeight*3 + 5, buttonWidth, buttonHeight), base_font,3)
    four_player = PlayerButton('4 Players' ,pygame.Rect(screenWidth / 2 - buttonWidth/2, textYPos + buttonHeight*4 + 10, buttonWidth, buttonHeight), base_font,4)
    five_player = PlayerButton('5 Players' ,pygame.Rect(screenWidth / 2 - buttonWidth/2, textYPos + buttonHeight*5 + 15, buttonWidth, buttonHeight), base_font,5)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
                running = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if two_player.clickEvent(event):
                    return two_player.value
                if three_player.clickEvent(event):
                    return three_player.value
                if four_player.clickEvent(event):
                    return four_player.value
                if five_player.clickEvent(event):
                    return five_player.value

        screen.fill("purple")

        displayTextCenter(screen, introText1, textYPos, base_font, (0,0,0))
        displayTextCenter(screen, introText2, textYPos + fontSize, base_font, (0,0,0))
        
        two_player.draw(screen)
        three_player.draw(screen)
        four_player.draw(screen)
        five_player.draw(screen)


        pygame.display.flip()
        clock.tick(60)


def getNames(numberOfPlayers):
    screenWidth = screen.get_width()
    title_font = pygame.font.Font(None,48)
    small_font = pygame.font.Font(None,32)

    for player in range(numberOfPlayers):
        players.append(Player())

    textBox1 = InputBox(pygame.Rect(500,200,140,30),pygame.Color("black"), pygame.Color("azure3"))
    textBox2 = InputBox(pygame.Rect(500,250,140,30),pygame.Color("black"), pygame.Color("azure3"))
    textBox3 = InputBox(pygame.Rect(500,300,140,30),pygame.Color("black"), pygame.Color("azure3"))
    textBox4 = InputBox(pygame.Rect(500,350,140,30),pygame.Color("black"), pygame.Color("azure3"))
    textBox5 = InputBox(pygame.Rect(500,400,140,30),pygame.Color("black"), pygame.Color("azure3"))
    
    
    nextButton = PlayerButton("Next", pygame.Rect(screenWidth/2 - 50, 500, 100, 50), title_font, 1)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()  
                return


            textBox1.getEvent(event)
            textBox2.getEvent(event)
            textBox3.getEvent(event)
            textBox4.getEvent(event)
            textBox5.getEvent(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextButton.clickEvent(event):
                    return

        

        screen.fill("purple")

        displayTextCenter(screen, "Name the players", 50, title_font, (0,0,0))
        if numberOfPlayers >= 2:
            textBox1.show(screen)
            players[0].name = textBox1.user_text
            displayText(screen, "What is player 1s name?", (200,205),small_font,'black')
            textBox2.show(screen)
            players[1].name = textBox2.user_text
            displayText(screen, "What is player 2s name?", (200,255),small_font,'black')
        if numberOfPlayers >= 3:
            textBox3.show(screen)
            players[2].name = textBox3.user_text
            displayText(screen, "What is player 3s name?", (200,305),small_font,'black')
        if numberOfPlayers >= 4:
            textBox4.show(screen)
            players[3].name = textBox4.user_text
            displayText(screen, "What is player 4s name?", (200,355),small_font,'black')
        if numberOfPlayers >= 5:
            textBox5.show(screen)
            players[4].name = textBox5.user_text
            displayText(screen, "What is player 5s name?", (200,405),small_font,'black')

        nextButton.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    
def game():

    title_font = pygame.font.Font(None,48)
    running = True

    winner = ""
    roundWon = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()  
                running = False
                return
                
            
        screen.fill("purple")
        
        for playerr in players:
            #print(playerr.name)
            if  len(playerr.cards) == 0 and len(playPile.cards) == 0:
                players.remove(playerr)


        for index,  player in enumerate(players):

            if len(player.cards) == 0: continue

            if len(players) < 2:
                running = False
                return
        
            screen.fill("purple")

            playPile.takeOneCardFromOther(player)
            
            displayTextCenter(screen ,f"{playPile.cards[-1]} {player.name}",100, title_font, 'black')
            #playPile.cards[-2].__str__()
            if len(playPile.cards) == 52:
                randomPlayer = random.choice(players)
                playPile.deal([randomPlayer])

                for playerr in players:
                    #print(playerr.name)
                    if  len(playerr.cards) == 0 and len(playPile.cards) == 0:
                        players.remove(playerr)
                
            if playPile.topCardsSame:
                roundWon = True
                random.seed(random.SystemRandom().random())
                randomPlayer = random.choice(players)
                winner = randomPlayer.name

                playPile.deal([randomPlayer])
                displayTextCenter(screen ,f"{randomPlayer.name} wins this round\n",200, title_font, 'black')
                print(f"{randomPlayer.name} wins this round\n")
                
                for playerr in players:
                    if  len(playerr.cards) == 0 and len(playPile.cards) == 0:
                        players.remove(playerr)
                        
            if roundWon == True:
                displayTextCenter(screen ,f"{winner} wins this round\n",200, title_font, 'black')

            displayTextCenter(screen, f"{len(playPile.cards)} cards are in the pile", 250, title_font, 'black')

            for index,  player in enumerate(players):
                displayTextCenter(screen, f"{player.name} has {len(player.cards)} cards", 300 + index * 50, title_font, 'black')
            
            
            #time.sleep(2)

            pygame.display.flip()
            clock.tick(2.5)

        pygame.display.flip()
        clock.tick(60)
    

def winScreen():
    
    title_font = pygame.font.Font(None,48)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
                running = False
                return
        
        #print("woring")
        screen.fill("purple")

        displayTextCenter(screen ,f"{players[0].name} wins",400, title_font, 'black')
        
        pygame.display.flip()
        clock.tick(60)
        

getNames(howManyPlayers())

deck.deal(players)

print(players[0].name)

game()

winScreen()

pygame.quit()
sys.exit()  
    