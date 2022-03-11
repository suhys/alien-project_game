class Settings():
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)
        
        # Ship settings
        self.ship_limit =3
        
        # Bullet settings
        self.bullet_width =50
        self.bullet_height =50
        self.bullet_color = 100,100,100
        self.bullets_allowed = 10
        
        # Alien Settings
        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initizlie settings that change throughout the game."""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1
            
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
            
    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale    