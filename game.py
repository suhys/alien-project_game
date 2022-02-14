import sys
import pygame
import game_function as gf

class Settings():
    """ A clas to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600 
        self.bg_color = (230,230,230)
        
class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        
        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Movement lfag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movment flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

def run_game():
    #Initialize pygame, setting, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion")
    
    #Make a ship
    ship = Ship(screen)
    
    # Start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()
        
run_game()