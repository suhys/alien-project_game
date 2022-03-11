class GameStats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.reset_stats()
        self.last_ships_left = self.ships_left
        self.game_active = True
        self.score = 0
        self.highscore = 0    # TODO: read from/write to file
        self.level = 0

    def get_score(self): return self.score
    def get_highscore(self): return self.highscore
    def get_level(self): return self.level
    def get_ships_left(self): return self.ships_left
    def save_highscore(self): pass    # TODO
    def reset_stats(self): self.ships_left = self.settings.ship_limit
    def level_up(self): 
        self.level += 1
        print("leveling up: level is now ", self.level)
    def alien_hit(self, alien):
        self.score += alien.points
        self.highscore = max(self.score, self.highscore)
    def ship_hit(self):
        self.ships_left -= 1
        n = self.ships_left
        print(f'SHIP HIT!', end=' ')
        if self.last_ships_left != self.ships_left:
            print(f'{self.ships_left} ship{"s" if n != 1 else ""} left')
            self.last_ships_left = self.ships_left
