import pygame
#sprites allow to group related elements in the game and act on all the grouped elements at once
from pygame.sprite import Sprite, Group

class Bullet(Sprite):
    """A class to manage bullet fired from the ship"""
    
    def __init__(self, ai_settings, screen, ship, aliens):
        """Create a bullet object at the ship's current position"""
        # call super() to inherit properly from Sprite 
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.ai_settings = ai_settings
        self.screen = screen
        self.ship = ship
        self.aliens = aliens
        
        # Make a group to store bullets in
        self.bullets = Group()

        
        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect) 
    

class Bullets(Sprite):
    def __init__(self, ai_settings, screen, ship, aliens):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen = screen
        self.ship = ship
        self.aliens = aliens
        
        self.bullets = Group()
        
    def fire_bullet(self):
        """Fire a bullet if limit not reached yet"""
        # Create a new bullet and add it to the bullets group.
        if len(self.bullets) < self.ai_settings.bullets_allowed:
            new_bullet = Bullet(self.ai_settings, self.screen, self.ship, self.aliens)
            self.bullets.add(new_bullet)
    
    def update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        
        # Get rid of bullets that have disappeared 
        # copy() method enables to modify bullets inside the loop 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        print(len(self.bullets))
        
        self.check_bullet_alien_collisions()
        
        # Update bullet positions.
        for bullet in self.bullets:
            bullet.update()
    
    def check_bullet_alien_collisions(self):
        """Respond to bullet- alien collisions"""
        # Remove any bullets and aliens that have collied 
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens.fleet, False, True)
            
        if len(self.aliens.fleet) == 0:
            # Destory existing bullets and create new fleet
            self.bullets.empty()
            self.aliens.create_fleet()
            
    def draw(self):
        for bullet in self.bullets:
            bullet.draw_bullet()
    