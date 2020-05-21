import pygame

class Level:
    def __init__(self, player):
        self.set_of_squares = set()
        self.set_of_obstacles = set()
        self.set_of_monsters = set()
        self.set_of_bombs = pygame.sprite.Group()
        self.doors = None
        self.player = player
        self.running = True

    def update(self):
        for p in self.set_of_monsters:
            p.level = self
            p.update()

    def draw(self, surface):
        for p in self.set_of_squares:
            p.draw(surface)
        for p in self.set_of_obstacles:
            p.draw(surface)
        for p in self.set_of_monsters:
            p.draw(surface)
        self.doors.draw(surface)
        self.set_of_bombs.draw(surface)
