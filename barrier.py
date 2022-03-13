from pygame.sprite import Sprite, Group
import pygame as pg

class Barrier(Sprite):
    
    def __init__(self, game, image):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.image = image

        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def draw(self):
        self.screen.blit(self.image, self.rect)


class Barriers():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.ship = game.ship
        
        self.image = (pg.transform.rotozoom(pg.image.load(f'images/barrier.png'), 0 ,4))

        self.barriers = Group()
        
        self.barrier = Barrier(self, image =self.image)
        
        self.barrier_h = self.barrier.rect.height
        self.barrier_w = self.barrier.rect.width
        self.create_barriers()
        
    def create_barriers(self):
        number_barriers_x = self.get_number_barrier_x(barrier_width = self.barrier_w)
        number_rows = 1
        
        for row in range(number_rows):
            for barrier_number in range(number_barriers_x):
                self.create_barrier(barrier_number = barrier_number, image = self.image)
            
        
    def get_number_barrier_x(self, barrier_width):
        available_space_x = self.settings.screen_width
        number_barriers_x = int(available_space_x / (barrier_width))
        return number_barriers_x
        
    def create_barrier(self, barrier_number, image):
        """Create an alien and place it in the row"""
        barrier = Barrier(self.game, image = image)
        barrier.x = 20 + 2 * self.barrier_w * barrier_number
        barrier.rect.x = barrier.x
        barrier.rect.y = self.settings.screen_height - self.ship.rect.height *3
        self.barriers.add(barrier)
        
    def draw(self):
        for barrier in self.barriers.sprites():
            barrier.draw()
