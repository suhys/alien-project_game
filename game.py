import sys
import pygame
import game_function as gf
from pygame.sprite import Group  

class Settings():
    """ A clas to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings""" 
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600 
        self.bg_color = (230,230,230)
        
        # ship settings
        self.ship_speed_factor = 1.5
        
        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60 
        
        
class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
        #Movement lfag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movment flag"""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center
        self.rect.centerx = self.center
        
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
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in 
    bullets = Group()
    
    # Start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()
        
run_game()