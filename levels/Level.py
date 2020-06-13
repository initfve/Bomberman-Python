import pygame


class Level:
    def __init__(self, player):
        self.set_of_squares = set()
        self.set_of_obstacles = pygame.sprite.Group()
        self.set_of_monsters = set()
        self.set_of_bombs = pygame.sprite.Group()
        self.set_of_explosions = pygame.sprite.Group()
        self.doors = None
        self._doors_active = False
        self.player = player
        self.running = True

    def update(self):
        for p in self.set_of_monsters:
            p.level = self
            p.update()

        if len(self.set_of_monsters) == 0:
            self._doors_active = True

        print(self.player.score)
        for explosion in self.set_of_explosions:
            for monster in self.set_of_monsters.copy():
                if explosion.rect.colliderect(monster.rect):
                    self.set_of_monsters.remove(monster)
                    self.player.score += 1
            self.set_of_obstacles = [obstacle for obstacle in self.set_of_obstacles if not explosion.rect.colliderect(obstacle.rect)]

    def draw(self, surface):
        for p in self.set_of_explosions:
            p.draw(surface)
        for p in self.set_of_squares:
            p.draw(surface)
        for p in self.set_of_obstacles:
            p.draw(surface)
        for p in self.set_of_monsters:
            p.draw(surface)
        self.doors.draw(surface)
        self.set_of_bombs.draw(surface)

    def get_doors_active(self):
        return self._doors_active
