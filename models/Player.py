import pygame
import game_config as gm
from models.Bomb import Bomb


# Klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = {}
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.bombs_count = 3
        self.player_level = 1
        self.lifes = 3
        self.score = 0
        self.level = None
        self.direction_of_movement = 'right'

    def turn_right(self):
        if self.direction_of_movement == 'left' or 'up':
            self.direction_of_movement = 'right'
        self.movement_x = 9 * (self.player_level * 0.75)

    def turn_left(self):
        if self.direction_of_movement == 'right' or 'up':
            self.direction_of_movement = 'left'
        self.movement_x = -9 * (self.player_level * 0.75)

    def go_up(self):
        self.movement_y = -9 * (self.player_level * 0.75)

    def go_down(self):
        self.movement_y = 9 * (self.player_level * 0.75)

    def stop(self):
        self.movement_x = 0
        self.movement_y = 0

    def set_bomb(self):
        print(len(self.level.set_of_bombs))
        if len(self.level.set_of_bombs) < 3:
            x = int(self.rect.x / gm.SQUARE_SIZE) * gm.SQUARE_SIZE
            y = int(self.rect.y / gm.SQUARE_SIZE) * gm.SQUARE_SIZE
            # sprawdzamy czy juz postawilismy bombe
            for bomb in self.level.set_of_bombs:
                if bomb.rect.x == x and bomb.rect.y == y:
                    return
            bomb = Bomb(gm.BOMB_ITEM[0], x, y)
            self.level.set_of_bombs.add(bomb)
            pygame.time.set_timer(bomb.explosion_event, 2000)

    def update(self):
        self.rect.x += self.movement_x  # odpowiada za ruch na osi x
        self.rect.y += self.movement_y  # odpowiada za ruch na osi y

        # ----------------------- KOLIZJA --------------------------- #
        colliding_obstacles = pygame.sprite.spritecollide(self, self.level.set_of_obstacles, False)
        colliding_squares = pygame.sprite.spritecollide(self, self.level.set_of_squares, False)
        colliding_bombs = pygame.sprite.spritecollide(self, self.level.set_of_bombs, False)
        print(colliding_bombs)
        for bomb in self.level.set_of_bombs:
            if not (bomb.rect.x + gm.SQUARE_SIZE / 4 <= self.rect.x <= bomb.rect.x - gm.SQUARE_SIZE * 3 / 4) and not (bomb.rect.y + gm.SQUARE_SIZE / 4 >= self.rect.y >= bomb.rect.y - gm.SQUARE_SIZE * 3 / 4):
                self._collide(colliding_bombs)

        self._collide(colliding_squares)
        self._collide(colliding_obstacles)

        if self.movement_x > 0:  # prawo
            self._move(gm.IMAGES_R)

        if self.movement_x < 0:  # lewo
            self._move(gm.IMAGES_L)

        if self.movement_y < 0:  # gora
            self._move(gm.IMAGES_UP)

        if self.movement_y > 0:
            self._move(gm.IMAGES_DOWN)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def get_event(self, event):
        for bomb in self.level.set_of_bombs:
            if event.type == bomb.explosion_event:
                pygame.time.set_timer(bomb.explosion_event, 0)
                bomb.kill()
                # explosion = Explosion(x, y)
                # self.level.set_of_explosions.add(explosion)

        for explosion in self.level.set_of_explosions:
            if event.type == explosion.explosion_event:
                pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.stop()
                self.turn_right()
            if event.key == pygame.K_a:
                self.stop()
                self.turn_left()
            if event.key == pygame.K_w:
                self.stop()
                self.go_up()
            if event.key == pygame.K_s:
                self.stop()
                self.go_down()
            if event.key == pygame.K_SPACE:
                self.set_bomb()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop()
                self.image = gm.STAND_R
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop()
                self.image = gm.STAND_L
            if event.key == pygame.K_w and self.movement_y < 0:
                self.stop()
                self.image = gm.STAND_R
            if event.key == pygame.K_s and self.movement_y > 0:
                self.stop()
                self.image = gm.STAND_L

    def _move(self, image_list):
        if self._count < 4:
            self.image = image_list[0]
        elif self._count < 8:
            self.image = image_list[1]

        if self._count >= 8:
            self._count = 0
        else:
            self._count += 1

    def _collide(self, objects):
        for p in objects:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
                if self.direction_of_movement == 'left' and self.movement_x == 0:
                    self.image = gm.STAND_L
                if self.direction_of_movement == 'right' and self.movement_x == 0:
                    self.image = gm.STAND_R
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom