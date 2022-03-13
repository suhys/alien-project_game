import pygame
from pygame.sprite import Sprite, Group
from timer import Timer
import random 
from random import choice 

class UFO:
    ufo_images = [pygame.transform.rotozoom(pygame.image.load(f'images/alienFour{n}.png'), 0 ,2) for n in range(2)]
    # ufo_scores_img1 = [pygame.transform.rotozoom(pygame.image.load(f'images/number{n}.png'), 0 ,2) for n in range(1)]
    # ufo_scores_img2 = [pygame.transform.rotozoom(pygame.image.load(f'images/number{n}.png'), 0 ,2) for n in range(1)]
    # ufo_scores_img3= [pygame.transform.rotozoom(pygame.image.load(f'images/number{n}.png'), 0 ,2) for n in range(1)]
    # ufo_scores_img4 = [pygame.transform.rotozoom(pygame.image.load(f'images/number{n}.png'), 0 ,2) for n in range(1)]
    # ufo_scores_img5 = [pygame.transform.rotozoom(pygame.image.load(f'images/number{n}.png'), 0 ,2) for n in range(1)]

    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.ship = game.ship
        self.settings = game.settings
        self.ufo_fleet = Group()
        self.aliens_UFO_fleet()
        self.delay_check = -1000
        self.int = 0
        self.store_direction = self.settings.ufo_direction

        
    def aliens_UFO_fleet(self):
        ran_score = random.randint(0,4)
        self.img = [pygame.image.load(f"images/number{ran_score}.png")]
        self.points = (ran_score + 1) * 100
        self.ufo = Alien(self.game, image_list = UFO.ufo_images, exploding_image=  self.img, points = self.points)
        self.ufo_create_alien()
        
    def ufo_create_alien(self):
        self.ufo_h = self.ship.rect.height + self.ufo.rect.height
        self.ufo.rect.y = self.ufo_h
        self.ufo_fleet.add(self.ufo)
        
    def empty(self) : self.ufo_fleet.empty()
        
    def update_UFO(self):
        for ufo in self.ufo_fleet.sprites():
            if ufo.check_edges():
                self.delay_check += 10
                if self.delay_check == self.int :
                    self.settings.ufo_direction = -1 * self.store_direction
                    self.store_direction = self.settings.ufo_direction
                    self.int = random.randrange(0,10000,1000)
                    self.delay_check = -1000
                else:
                    self.settings.ufo_direction = 0
            break
        
        if pygame.sprite.spritecollideany(self.ship, self.ufo_fleet):
            if not self.ship.is_dying():
                self.ship.hit()

        # automatically calls each alien's update() method
        for ufo in self.ufo_fleet.sprites():
            ufo.update()  
            
    def ufo_delay(self):
        self.delay_check = -1000
        self.int = 0
        self.settings.ufo_direction = 1
        
            
    def UFOdraw(self):
        self.ufo.blitme()
    
class Aliens:
    exploding_image = [pygame.image.load(f'images/explode{n}.png') for n in range(4)]
    
    alien_0_imgs = [pygame.image.load(f'images/alienOne{n}.png') for n in range(2)]
    alien_1_imgs = [pygame.image.load(f'images/alienTwo{n}.png') for n in range(2)]
    alien_2_imgs = [pygame.image.load(f'images/alienThree{n}.png') for n in range(2)]
    image = pygame.image.load('images/alienOne0.png')
    
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.ship = game.ship
        self.status = game.stats
        self.fleet = Group()
        self.aliens_fleet()
    
    def aliens_fleet(self):      
        self.exclude  = self.ship.rect.height  
        self.alien = Alien(self.game, image_list = Aliens.alien_2_imgs, image = pygame.image.load('images/alienOne0.png'))
        self.height_width(image_list = Aliens.alien_2_imgs)
        self.alien = Alien(self.game, image_list = Aliens.alien_1_imgs, image = pygame.image.load('images/alienTwo0.png'))
        self.height_width(image_list = Aliens.alien_1_imgs)
        self.alien = Alien(self.game, image_list = Aliens.alien_0_imgs, image = pygame.image.load('images/alienThree0.png'))
        self.height_width(image_list = Aliens.alien_0_imgs)


    def height_width(self, image_list):
            self.alien_h = self.alien.rect.height
            self.alien_w = self.alien.rect.width
            self.create_fleet(image_list = image_list)
    
    def empty(self) : self.fleet.empty()
    
    def create_fleet(self, image_list):
        """Create a full fleet of aliens"""
        # Create an alien and find the number of aliens in a row
        #Spacing between each alien is equal to one alien width
        number_aliens_x = self.get_number_aliens_x(alien_width = self.alien_w)
        number_rows = self.get_number_rows(ship_height = self.ship.rect.height, 
                                           alien_height = self.alien_h)
        
        #Create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(row_number = row_number, alien_number = alien_number, image_list = image_list)
        
        self.exclude += self.alien_h + 2 * self.alien_h * row_number
        

    def get_number_aliens_x(self, alien_width):
        """Determine the number of aliens tha fit in a row"""
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x

    def get_number_rows(self, ship_height, alien_height):
        """Determine the number of rows of aliens that fit on the screen"""
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height) - self.exclude
        number_rows = int(available_space_y / ( 2 * alien_height))
        number_rows = number_rows/3
        return int(number_rows)

    def create_alien(self, row_number, alien_number, image_list):
        """Create an alien and place it in the row"""
        alien = Alien(self.game, image_list = image_list)
        alien.x = self.alien_w + 2 * self.alien_w * alien_number
        alien.rect.x = alien.x
        alien.rect.y = self.alien_h * 2 + 2 * self.alien_h * row_number + self.ship.rect.height + self.exclude
        self.fleet.add(alien)
            
    def update_aliens(self):
        """Check if the fleet is at an enge,
            and then update the positions of all aliens in the fleet."""
        self.check_fleet_edges()
        
        if pygame.sprite.spritecollideany(self.ship, self.fleet) or self.check_bottom():
            if not self.ship.is_dying():
                self.ship.hit()

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
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def check_bottom(self):
        for alien in self.fleet.sprites():
            if alien.check_bottom():
                self.ship.hit()
                break

    
    def draw(self):
        for alien in self.fleet.sprites():
            alien.blitme() 

class AlienLasers:
    def __init__(self, game):
        self.game = game
        self.settings = self.game.settings
        self.aliens = self.game.aliens
        self.ship = self.game.ship
        self.barriers = self.game.barriers
        self.alien_lasers = Group()
        self.int = 0
        self.delay_check = -1000
        

            
    def alien_shoot(self):
        if len(self.alien_lasers) < self.settings.bullets_allowed:
            random_alien = choice(self.aliens.fleet.sprites())
            laser = AlienLaser(game = self.game, alien = random_alien)                
            self.alien_lasers.add(laser)
    
    def draw(self):
        self.delay_check += 50
        if self.delay_check == self.int :
            self.alien_shoot()
            self.int = random.randrange(0,10000,1000)
            self.delay_check = -1000
        
        for laser in self.alien_lasers:
            laser.draw()
            
    def update(self):
        for laser in self.alien_lasers.copy():
            if laser.rect.top >= self.settings.screen_height:
                self.alien_lasers.remove(laser)
                
        if pygame.sprite.spritecollideany(self.ship, self.alien_lasers):
            self.ship.hit()
            
        collisions = pygame.sprite.groupcollide(self.alien_lasers, self.barriers.barriers, True, False)

        for laser in self.alien_lasers:
            laser.update()    
            
                
            
class AlienLaser(Sprite):
    def __init__(self, game, alien):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.alien = alien
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = self.alien.rect.centerx
        self.rect.bottom = self.alien.rect.bottom
        
        self.y = float(self.rect.y)
        
        self.color = self.settings.alien_bullet_color
        self.speed = self.settings.bullet_speed_factor
            
    
    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        ("update")
  
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect) 
            
       
            
class Alien(Sprite):
    """A class to represent an single alien in the fleet"""  
    
    def __init__(self, game, image_list, image= Aliens.image, exploding_image = Aliens.exploding_image, points = 10):
        """initialize the alien and set its starting position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.ship = game.ship
        self.stats = game.stats
        self.points = points
        self.sound = game.sound
            
        #load the alien image and set its rect attribute
        self.image = image
        self.rect = self.image.get_rect()
        
        #Start each new alien near the top left of the screen
        # adding a space to the left of it alien's width and a space above it to its height
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # #Store the alien's exact position 
        # self.x = float(self.rect.x)
        
        self.image_list = image_list
        self.exploding_timer = Timer(image_list= exploding_image, 
                                     delay = 100, is_loop = False)
        self.normal_timer = Timer(image_list= self.image_list, delay=1000, is_loop=True)
        self.timer = self.normal_timer

        self.dying = False
        self.index = 0
    
    def set_p(self, ul):
        self.rect.x, self.rect.y = ul
        
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
        
    def UFO_check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right - self.ufo.rect.width:
            return True
        elif self.rect.left <= 0 + self.ufo.rect.width:
            return True 
    
    def check_bottom(self):
        """Return True if alien is at the bottom of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        
    def hit(self):
        self.stats.alien_hit(alien=self)
        self.timer = self.exploding_timer
        self.dying = True
        self.sound.bg_speed()
        
        
    def update(self):
        """Move the alien right or left"""
        if self.dying and self.timer.is_expired():
            self.kill()
            
        if self.image_list == UFO.ufo_images:
            self.update_UFO()
        else:
            self.update_aliens()
            
    def update_aliens(self):
        self.rect.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        
    def update_UFO(self):
        self.rect.x += (self.settings.alien_speed_factor * self.settings.ufo_direction)
        
        