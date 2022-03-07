#exit the game when the player quit
import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

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

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    #Watch for keyboard and mouse events
    for event in pygame.event.get():
        # event is an action that the user performs (pressing a key or moving the mouse)
        # respond to event, event loop to listen for an event 
        # use pygame.event.get() to access the events detected
        if event.type == pygame.QUIT:
            sys.exit()
        
        # each keypress is registered as a KEYDOWN event 
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            
        
        # keypress is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
                
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pas through the loop
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # call the ship's blitme() method 
    ship.blitme()
    aliens.draw(screen)
              
    # Make the most recently drawn screen visible   
    pygame.display.flip()
    
def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet positions.
    bullets.update()
        
    # Get rid of bullets that have disappeared 
    # copy() method enables to modify bullets inside the loop 
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    print(len(bullets))
    
def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in a row
    #Spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    #Create the first row of aliens
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
