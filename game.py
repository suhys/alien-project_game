import pygame as pg
from sys import exit
from landing_page import LandingPage
from time import sleep
from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from alien import Aliens, UFO
from bullet import Bullets
from sound import Sound
from barrier import Barriers
from alien import AlienLasers
 
class Game:
    
    def __init__(self):
        #initialize pygame, settings, and screen object
        pg.init()
        self.settings = Settings()
        self.stats = GameStats(game=self)
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.sound = Sound()
        self.sb = Scoreboard(game=self)
        
        # create a display winddow called screen 
        pg.display.set_caption("Space Invasion")

        self.ship = Ship(game=self)
        self.UFO = UFO(game=self)
        self.aliens = Aliens(game=self)
        self.barriers = Barriers(game = self)
        self.bullets = Bullets(game=self)
        self.alienlasers = AlienLasers(game=self)


    
    def restart(self):
        if self.stats.ships_left == 0: 
            self.game_over()
        elif len(self.aliens.fleet) == 0: 
            print("level up")
        else:
            print("restarting game")
        
        while self.sound.busy():
            pass
        
        
        self.settings.increase_speed()

        self.bullets.empty()
        self.aliens.empty()
        self.UFO.empty()
        
        self.UFO.aliens_UFO_fleet()
        self.UFO.ufo_delay()
        self.aliens.aliens_fleet()
        self.ship.center_bottom()
        self.ship.reset_timer()        
        self.update()
        self.draw()
        sleep(0.5)    
    
    def update(self):
        self.ship.update()
        self.bullets.update_bullets()
        self.aliens.update_aliens()
        self.UFO.update_UFO()
        self.sb.update()
        self.alienlasers.update() 
    
    def draw(self):
        """Update images on the screen and flip to the new screen"""
        # Redraw the screen during each pas through the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw()  
        self.UFO.UFOdraw()
        self.bullets.draw()
        self.barriers.draw()
        self.sb.draw()
        self.alienlasers.draw()
        # Make the most recently drawn screen visible   
        pg.display.flip()
    
    def run_game(self):  
        # Start the main loop for the game
        self.finished = False
        self.sound.play_bg()
        while not self.finished:
            # call function check_event for respond keyboard an d mouse events
            gf.check_events(game=self)
            self.update()  
             # call function update_screen for update images on screen and flip to the new screen
            self.draw()
        self.game_over() 
            
    def game_over(self): 
        print('\nGAME OVER!\n\n')  
        self.sound.play_game_over()
        self.settings.initialize_dynamic_settings()
        main() # can ask to replay here instead of exiting the game

def main():
    game = Game()
    lp = LandingPage(game=game)
    lp.show()
    game.run_game()

if __name__ == '__main__':
    main()