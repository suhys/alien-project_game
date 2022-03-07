import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an single alien in the fleet"""
    
    alien_one_imgs = [pygame.image.load(f'images/alienOne{n}.png') for n in range(2)]
    alien_two_imgs = [pygame.image.load(f'images/alienTwo{n}.png') for n in range(2)]
    alien_Three_imgs = [pygame.image.load(f'images/alienThree{n}.png') for n in range(2)]
    alien_Four_imgs = [pygame.image.load(f'images/alienFour{n}.png') for n in range(2)]
    
    
    def __init__(self,ai_settings, screen):
        """initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alienOne0.png')
        self.rect = self.image.get_rect()
        
        #Start each new alien near the top left of the screen
        # adding a space to the left of it alien's width and a space above it to its height
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact position 
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw teh alien at its current position"""
        self.screen.blit(self.image, self.rect)
        