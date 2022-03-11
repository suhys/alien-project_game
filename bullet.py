import pygame as pg
#sprites allow to group related elements in the game and act on all the grouped elements at once
from pygame.sprite import Sprite, Group
from copy import copy
from alien import Aliens
import random
# from alien import Alien

class Bullets:
    def __init__(self, game):
        self.game = game
        self.settings = self.game.settings
        self.aliens = self.game.aliens
        self.stats = game.stats
        
        self.bullets = Group()
        
    def empty(self): self.bullets.empty()
        
    def fire_bullet(self):
        """Fire a bullet if limit not reached yet"""
        # Create a new bullet and add it to the bullets group.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.game)
            self.bullets.add(new_bullet)
    
    def update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        
        # Get rid of bullets that have disappeared 
        # copy() method enables to modify bullets inside the loop 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        collisions = pg.sprite.groupcollide(self.aliens.fleet, self.bullets, False, True)
        for alien in collisions: 
            if not alien.dying: 
                if alien.image_list == Aliens.alien_2_imgs:
                    alien.points = 40
                elif alien.image_list == Aliens.alien_1_imgs:
                    alien.points = 20
                elif alien.image_list == Aliens.alien_0_imgs:
                    alien.points = 10
                elif alien.image_list == Aliens.alien_3_imgs:
                    alien.points = int(random.choice(Aliens.ran_score))
                print (alien.points)
                alien.hit()
            
        if len(self.aliens.fleet) == 0:
            self.stats.level_up()
            self.game.restart()
        
        # Update bullet positions
        for bullet in self.bullets:
            bullet.update()
                            
    def draw(self):
        for bullet in self.bullets:
            bullet.draw_bullet()

class Bullet(Sprite):
    """A class to manage bullet fired from the ship"""
    
    def __init__(self, game):
        """Create a bullet object at the ship's current position"""
        # call super() to inherit properly from Sprite 
        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings
        self.ship = game.ship
        self.aliens = game.aliens
        
        # Make a group to store bullets in
        self.bullets = Group()

        
        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top
        
        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = self.settings.bullet_color
        self.speed_factor = self.settings.bullet_speed_factor
        
    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pg.draw.rect(self.screen, self.color, self.rect) 
    
    