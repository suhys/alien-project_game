import pygame as pg
from sys import exit
from landing_page import LandingPage
from time import sleep
from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from alien import Aliens
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
        self.sb = Scoreboard(game=self)
        
        # create a display winddow called screen 
        pg.display.set_caption("Alien Invasion")

        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        self.bullets = Bullets(game=self)
    
    def restart(self):
        if self.stats.ships_left == 0: 
            self.game_over()
        elif len(self.aliens.fleet) == 0:
            print("level up")
        else:
            print("restarting game")
        
        
        self.settings.increase_speed()

        self.bullets.empty()
        self.aliens.empty()
        
        self.aliens.create_fleet()
        self.ship.center_bottom()
        self.ship.reset_timer()        
        self.update()
        self.draw()
        sleep(0.5)    
    
    def update(self):
        self.ship.update()
        self.bullets.update_bullets()
        self.aliens.update_aliens()
        self.sb.update()
    
    def draw(self):
        """Update images on the screen and flip to the new screen"""
        # Redraw the screen during each pas through the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw()
        self.bullets.draw()
        self.sb.draw()
        # Make the most recently drawn screen visible   
        pg.display.flip()
    
    def run_game(self):  
        # Start the main loop for the game
        self.finished = False
        while not self.finished:
            # call function check_event for respond keyboard and mouse events
            gf.check_events(game=self)
            self.update()
            # call function update_screen for update images on screen and flip to the new screen
            self.draw()
        self.game_over()
            
    def game_over(self): 
        print('\nGAME OVER!\n\n')  
        self.settings.initialize_dynamic_settings()
        exit()    # can ask to replay here instead of exiting the game

def main():
    game = Game()
    lp = LandingPage(game=game)
    lp.show()
    game.run_game()

if __name__ == '__main__':
    main()