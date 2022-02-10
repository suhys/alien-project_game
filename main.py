import pygame as pg
import sys

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

class Alien:
    def __init__(self):pass
    def update(self):pass
    def draw(self):pass

class Laser:
    def __init__(self):pass
    def update(self):pass
    def draw(self):pass

class Ship:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def update(self):pass
    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Game:
    def __init__(self):
        pg.init()
        settings = Settings()
        self.screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
        self.bg_color = settings.bg_color
        pg.display.set_caption("ALien Invasion")
        
        self.ship = Ship(game=self)
        
    def update(self):pass
    
    def draw(self):
        self.screen.fill(self.bg_color)
        self.ship.draw()
        pg.display.flip()
        
    def play(self): 
        finished = False
        while not finished:
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True
        
        pg.exit()
        sys.exit()
 
            
    

def main():
    g = Game()
    g.play()
    
    
if __name__ == '__main__':
    main()