import pygame as pg
from sys import exit
# from landing_page import LandingPage
from time import sleep
from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from aliens import Aliens
from bullet import Bullets

class Game:
    
    def __init__(self):
        #initialize pygame, settings, and screen object
        pg.init()
        self.settings = Settings()
        self.stats = GameStats(game=self)
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        
        # create a display winddow called screen 
        pg.display.set_caption("Alien Invasion")

        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        self.bullets = Bullets(game=self)
    
    def restart(self):
        if self.stats.ships_left == 0: 
            self.game_over()
        print("restarting game")
        self.bullets.empty()
        self.aliens.empty()
        self.aleins.create_fleet()
        self.ship.center_bottom()
        self.ship.reset_timer()
        self.update()
        self.draw()
        sleep(0.5)    
    
    def update(self):
        self.ship.update()
        self.bullets.update_bullets()
        self.aliens.update_aliens()
    
    def draw(self):
        """Update images on the screen and flip to the new screen"""
        # Redraw the screen during each pas through the loop
        self.screen.fill(self.bg_color)
        # Redraw all bullets behind ship and aliens
        self.bullets.draw()
        # call the ship's blitme() method 
        self.ship.blitme()
        self.aliens.draw()
        # Make the most recently drawn screen visible   
        pg.display.flip()
    
    def run_game(self):
        self.finished = False
        # Start the main loop for the game
        while not self.finished:
            # call function check_event for respond keyboard and mouse events
            gf.check_events(game=self)
            self.update()    
            # call function update_screen for u pdate images on screen and flip to the new screen
            self.draw()
        self.game_over()
            
    def game_over(self): 
        print('\nGAME OVER!\n\n')  
        exit()    # can ask to replay here instead of exiting the game

def main():
    game = Game()
    # lp = LandingPage()
    game.run_game()

if __name__ == '__main__':
    main()