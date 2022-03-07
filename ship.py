import pygame
from timer import Timer

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the ship image and get its rect
        #returns a surface representing the ship, and store in self.image
        self.image = pygame.image.load('images/ship.bmp')
        # use get_rect() to access the surface's rect attribute
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen
        # initializing the x-coordinate of the ship's center (x, 0)
        self.rect.centerx = self.screen_rect.centerx
        # initializing the y-coordinate of the ship's bottom  (0, y)
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    # def hit(self):
    #     self.timer = self.exploding_timer()
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        # check self.moving_right is True (right arrow key is pressed) and did not reaches the edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # move ship to the right 
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
            
        
        # Update rect object from self.center
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom
        
    def blitme(self):
        """Draw the ship at its current location"""
        # blitme() method, which will draw the image to the screen at the position specified by self.rect
        self.screen.blit(self.image, self.rect)