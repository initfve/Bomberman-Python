from random import choice

import pygame
import game_config as gm


# Klasa przeciwnika
class Monster(pygame.sprite.Sprite):
    def __init__(self, file_image, life_count, side, rect_x, rect_y):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.movementX = -1
        self.movementY = 0
        self._count = 0
        self._lifeCount = life_count
        self.level = None
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.direction = choice(self.directions)
        self.side = side
        self.rect.x = rect_x
        self.rect.y = rect_y
        self._animation_frame = 0

    def update(self, *args):
        self._move(self.direction, 4)
        self.rect.x += self.movementX
        self.rect.y += self.movementY

        colliding_obstacles = pygame.sprite.spritecollide(self, self.level.set_of_obstacles, False)
        colliding_squares = pygame.sprite.spritecollide(self, self.level.set_of_squares, False)
        colliding_player = pygame.sprite.spritecollide(self, {self.level.player}, False)

        if colliding_player:
            self.level.running = False

        self._define_direction([colliding_obstacles, colliding_squares, colliding_player])

        for p in (colliding_obstacles + colliding_squares):
            if self.movementX > 0:
                self.rect.right = p.rect.left
            if self.movementX < 0:
                self.rect.left = p.rect.right
            if self.movementY > 0:
                self.rect.bottom = p.rect.top
            if self.movementY < 0:
                self.rect.top = p.rect.bottom

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def stop(self):
        self.movementX = 0
        self.movementY = 0

    # direction should be f. e. { x: 1, y: 1} is right, down, { x: -1, y: -1} is left, up
    def _move(self, direction, speed):
        if self._animation_frame == 0:
            self.image = gm.MONSTER[0]
        elif self._animation_frame == 1:
            self.image = gm.MONSTER[1]
        elif self._animation_frame == 2:
            self.image = gm.MONSTER[1]
        elif self._animation_frame == 3:
            self.image = gm.MONSTER[1]
        elif self._animation_frame == 4:
            self.image = gm.MONSTER[1]

        if self._animation_frame == 4:
            self._animation_frame = 0
        else:
            self._animation_frame += 1

        dx, dy = direction
        self.movementX = dx * speed
        self.movementY = dy * speed

    def _define_direction(self, conditions):
        for condition in conditions:
            if condition:
                self.direction = choice(self.directions)
            elif self.has_to_change_dir():
                dice = choice(self.directions)
                if (dice[0] == self.direction[0] and dice[1] == -self.direction[1]) \
                        or (dice[0] == -self.direction[0] and dice[1] == self.direction[1]):
                    return 'Same'
                self.direction = dice

    def _die(self):
        pass

    def has_to_change_dir(self):
        if self.rect.y > gm.SQUARE_SIZE \
                and self.rect.y % gm.SQUARE_SIZE == 0 \
                and self.rect.x > gm.SQUARE_SIZE \
                and self.rect.x % gm.SQUARE_SIZE == 0 \
                and self.movementX != 0:
            return choice([True, False])

        return False
