import pygame
from pygame.sprite import Sprite
from timer import Timer


class Alien(Sprite):
    """A class to represent an single alien in the fleet"""
    
    alien_0_imgs = [pygame.image.load(f'images/alienOne{n}.png') for n in range(2)]
    alien_1_imgs = [pygame.image.load(f'images/alienTwo{n}.png') for n in range(2)]
    alien_2_imgs = [pygame.image.load(f'images/alienThree{n}.png') for n in range(2)]
    alien_3_imgs = [pygame.image.load(f'images/alienFour{n}.png') for n in range(2)]
    
    
    def __init__(self, game):
        """initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alienOne1.png')
        self.rect = self.image.get_rect()
        
        #Start each new alien near the top left of the screen
        # adding a space to the left of it alien's width and a space above it to its height
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact position 
        self.x = float(self.rect.x)
        
        self.image_list = Alien.alien_0_imgs
        self.timer = Timer(image_list = self.image_list, delay=1000, is_loop=True)
        self.dying = False
        
    def blitme(self):
        """Draw the alien at its current position"""
        image = self.timer.image()
        rect = image.get_rect()
        rect.x, rect.y = self.rect.x, self.rect.y
        self.screen.blit(image, rect)
        
    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True 
    
    def check_bottom(self):
        """Return True if alien is at the bottom of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        
    def update(self):
        """Move the alien right or left"""
        if self.dying and self.timer.is_expired():
            self.ship.die()
            print("ship die")
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
        