#exit the game when the player quit
import sys
import pygame
from pygame.sprite import Sprite


def check_keydown_events(event, ship, bullets):
    """Respond to keypresses"""
    # check if the key pressed is the right arrow key (pygame.K_RIGHT)
    if event.key == pygame.K_RIGHT:
        # set it to True so update function will move the ship to the Right  
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # set it to True so update function will move the ship to the left 
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True 
    elif event.key == pygame.K_SPACE:
        bullets.fire_bullet()
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False 

def check_events(game):
    """Respond to keypresses and mouse events"""
    ship = game.ship
    bullets = game.bullets
    
    #Watch for keyboard and mouse events
    for event in pygame.event.get():
        # event is an action that the user performs (pressing a key or moving the mouse)
        # respond to event, event loop to listen for an event 
        # use pygame.event.get() to access the events detected
        if event.type == pygame.QUIT:
            sys.exit()
        
        # each keypress is registered as a KEYDOWN event 
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets)
        
        # keypress is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            


            
