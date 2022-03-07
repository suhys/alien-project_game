import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
    #initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))

    # create a display winddow called screen 
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship
    ship = Ship(ai_settings, screen)
     
    # Make a group to store bullets in
    bullets = Group()
    
    # Make a group to store alilens in
    aliens = Group()
    
    # Make a alien
    gf.create_fleet(ai_settings, screen, aliens)
        
    # Start the main loop for the game
    while True:
        # call function check_event for respond keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        # update the ship position based on the check_event
        ship.update()
        gf.update_bullets(bullets)
            
        # call function update_screen for update images on screen and flip to the new screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()