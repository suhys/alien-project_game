import pygame
from pygame.sprite import Sprite, Group
from alien import Alien

class Aliens:
    
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.ai_settings = game.settings
        self.ship = game.ship
        alien = Alien(self.game)
        self.alien_h = alien.rect.height
        self.alien_w = alien.rect.width
        self.fleet = Group()
        
        self.create_fleet()
        
    def empty(self) : self.fleet.empty()
    
    def create_fleet(self):
        """Create a full fleet of aliens"""
        # Create an alien and find the number of aliens in a row
        #Spacing between each alien is equal to one alien width
        number_aliens_x = self.get_number_aliens_x(alien_width = self.alien_w)
        number_rows = self.get_number_rows(ship_height = self.ship.rect.height, 
                                           alien_height = self.alien_h)
            
        #Create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(row_number = row_number, alien_number = alien_number)

    def get_number_aliens_x(self, alien_width):
        """Determine the number of aliens tha fit in a row"""
        available_space_x = self.ai_settings.screen_width - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x

    def get_number_rows(self, ship_height, alien_height):
        """Determine the number of rows of aliens that fit on the screen"""
        available_space_y = (self.ai_settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / ( 2 * alien_height))
        return number_rows

    def create_alien(self, row_number, alien_number):
        """Create an alien and place it in the row"""
        alien = Alien(self.game)
        alien.x = self.alien_w + 2 * self.alien_w * alien_number
        alien.rect.x = alien.x
        alien.rect.y = self.alien_h + 2 * self.alien_h * row_number
        self.fleet.add(alien)
        
    def update_aliens(self):
        """Check if the fleet is at an enge,
            and then update the positions of all aliens in the fleet."""
        self.check_fleet_edges()
        
        if pygame.sprite.spritecollideany(self.ship, self.fleet) or self.check_bottom():
            if not self.ship.is_dying(): 
                self.ship.hit()
            print("bottom hit")

        # automatically calls each alien's update() method
        for alien in self.fleet.sprites():
            alien.update()

    def check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.fleet.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break
            
    def change_fleet_direction(self):
        """Drop the entire fleet and chnage the fleet's direction"""
        for alien in self.fleet.sprites():
            alien.rect.y += self.ai_settings.fleet_drop_speed
        self.ai_settings.fleet_direction *= -1
    
    def check_bottom(self):
        for alien in self.fleet.sprites():
            if alien.check_bottom():
                self.ship.hit()
                break
    
    def draw(self):
        for alien in self.fleet.sprites():
            alien.blitme()
