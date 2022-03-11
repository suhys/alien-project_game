from tkinter import PAGES
import pygame as pg
from timer import Timer
from pygame.sprite import Sprite

class Ship(Sprite):
    
    exploding_image = [pg.image.load(f'images/explode{n}.png') for n in range(4)]
    images = [pg.image.load(f'images/ship.bmp') for n in range(1)]
    
    def __init__(self, game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.stats = game.stats
        
        # Load the ship image and get its rect
        #returns a surface representing the ship, and store in self.image
        self.image = pg.image.load('images/ship.bmp')
        
        # use get_rect() to access the surface's rect attribute
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Start each new ship at the bottom center of the screen
        self.center_bottom()


        
        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        self.exploding_timer = Timer(image_list=Ship.exploding_image, delay=200, is_loop=False)
        self.normal_timer = Timer(image_list=Ship.images, delay=1000, is_loop=True)
        self.timer = self.normal_timer
        self.dying = False
    
    def center_bottom(self):
        """Center the ship on the screen"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = self.rect.centerx
        self.bottom = self.rect.bottom
        
    def reset_timer(self):
        self.exploding_timer.reset()
        self.normal_timer.reset()
        self.timer = self.normal_timer
       
    def hit(self):
        self.timer = self.exploding_timer
        self.dying = True
    
    def is_dying(self): return self.dying
    
    def die(self):
        self.stats.ship_hit()
        if self.stats.ships_left == 0:
            self.game.finshed = True
        self.dying = False
        self.game.restart()
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        # Chick if the ship got hit
        if self.dying and self.timer.is_expired():
            self.die()

        # check self.moving_right is True (right arrow key is pressed) and did not reaches the edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # move ship to the right 
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.settings.ship_speed_factor
            
        # Update rect object from self.center
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom
        
    def blitme(self):
        """Draw the ship at its current location"""
        # blitme() method, which will draw the image to the screen at the position specified by self.rect
        image = self.timer.image()
        rect = image.get_rect()
        rect.x, rect.y = self.rect.x, self.rect.y
        self.screen.blit(image, rect)