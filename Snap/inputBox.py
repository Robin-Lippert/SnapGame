import pygame


class InputBox:

    def __init__(self, input_rect : pygame.rect, color_active : pygame.Color, color_pasive: pygame.Color):
        self.active = False
        self.base_font = pygame.font.Font(None,32)
        self.user_text = ''

        self.input_rect = input_rect
        self.color_active = color_active
        self.color_pasive = color_pasive
        self.color = self.color_pasive

    def show(self, screen):
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_pasive

        pygame.draw.rect(screen,self.color, self.input_rect,2)

        text_surface = self.base_font.render(self.user_text,True,(255,255,255))
        screen.blit(text_surface,(self.input_rect.x + 5,self.input_rect.y + 5 ))

        self.input_rect.w = max(100,text_surface.get_width() + 10) 

    def getEvent(self,event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False

            if event.type == pygame.KEYDOWN:
                if self.active == True:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text= self.user_text[:-1]
                    else:
                        self.user_text += event.unicode

class PlayerButton:
    def __init__(self, text, buttonRect, font,value):
        self.text = font.render(text,True, 'white')
        self.buttonRect = buttonRect
        self.font = font
        self.value = value
    
    def clickEvent(self,event):
        if self.buttonRect.collidepoint(event.pos):
            return True
        else:
            return False
            
    def draw(self, screen):
        a,b = pygame.mouse.get_pos()
        if self.buttonRect.x <= a <= self.buttonRect.x + self.buttonRect.w and self.buttonRect.y <= b <= self.buttonRect.y + self.buttonRect.h:
            pygame.draw.rect(screen, (180,180,180), self.buttonRect)
        else:
            pygame.draw.rect(screen, (110,110,110), self.buttonRect)
        screen.blit(self.text, (self.buttonRect.x + 10, self.buttonRect.y+10))    

