import os
import pygame
import random

import game_module as gm
from Border import Border
from Obstacle import Obstacle
from Player import Player


os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
pygame.init()

## ustawienia ekranu i gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
pygame.display.set_caption('Bomberman')
clock = pygame.time.Clock()


class Level:
    def __init__(self, player):
        self.set_of_squares = set()
        self.set_of_obstacles = set()
        self.player = player

    def update(self):
        for p in self.set_of_squares:
            p.update()
        for p in self.set_of_obstacles:
            p.update()

    def draw(self, surface):
        for p in self.set_of_squares:
            p.draw(surface)
        for p in self.set_of_obstacles:
            p.draw(surface)


class Level_1(Level):
    def __init__(self, player=None):
        super().__init__(player)
        self.create_platforms()

    def create_platforms(self):
        borders = []
        spare_fields = []

        for i in range(int(gm.WIDTH / gm.SQUARE_SIZE)):
            for j in range(int(gm.HEIGHT / gm.SQUARE_SIZE)):
                if i == 0 or j == 0 or i == range(int(gm.WIDTH / gm.SQUARE_SIZE))[-1] or j == \
                        range(int(gm.HEIGHT / gm.SQUARE_SIZE))[-1] or (i % 2 == 0 and j % 2 == 0):
                    borders.append([gm.SQUARE_SIZE, i * gm.SQUARE_SIZE, j * gm.SQUARE_SIZE])
                    continue

                spare_fields.append([gm.SQUARE_SIZE, i * gm.SQUARE_SIZE, j * gm.SQUARE_SIZE])

        for border in borders:
            border_object = Border(gm.PLATFORM_CELLS[0], *border)
            self.set_of_squares.add(border_object)

        for field in spare_fields:
            obstacle_object = Obstacle(gm.PLATFORM_CELLS[1], *field)
            self.set_of_obstacles.add(obstacle_object)

        self.set_of_obstacles = self._random_empty_list(self.set_of_obstacles)

    def _random_empty_list(self, source_list):
        list_len = len(source_list)
        output_list = random.sample(source_list, random.randint(0, int(list_len/2)))

        return output_list
player = Player(gm.STAND_R)
# konkretyzacja obiektów
current_level = Level_1(player)
player.level = current_level


player.rect.center = screen.get_rect().center

# głowna pętla gry
window_open = True
while window_open:
    screen.fill(gm.LIGHTBLUE)
    # pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif event.type == pygame.QUIT:
            window_open = False

        player.get_event(event)

    # rysowanie i aktualizacja obiektów
    player.update()
    player.draw(screen)
    current_level.draw(screen)

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)
#zmieniam cos
pygame.quit()
