import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        
        # enable following line after game class functional
        #self.middle_width, self.middle_height = self.game.display_width / 2, self.game.display_width / 2
        
        # disable & remove following line after game class functional
        self.middle_width, self.middle_height = 480, 320
        
        self.run_display = True
        
        self.cursor_rectangle = pygame.Rect(0, 0, 20, 20)
        self.cursor_offset = -100
    
    
    def draw_cursor(self):
        
        
    
    
    
    
