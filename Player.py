import pygame, os
import game_module as gm
import Bomb as bomb

class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = {}
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.n_bomb = 1
        self.player_level = 1
        self.lifes = 3
        self.score = 0
        self.level = None
        self.direction_of_movement = 'right'

    def turn_right(self):
        if self.direction_of_movement == 'left' or 'up':
            self.direction_of_movement = 'right'
        self.movement_x = 9*(self.player_level*0.75)

    def turn_left(self):
        if self.direction_of_movement == 'right' or 'up':
            self.direction_of_movement = 'left'
        self.movement_x = -9*(self.player_level*0.75)

    def go_up(self):
        self.movement_y = -9*(self.player_level*0.75)

    def go_down(self):
        self.movement_y = 9*(self.player_level*0.75)

    def stop(self):
        self.movement_x = 0
        self.movement_y = 0

    def set_bomb(self):
        if self.n_bomb > 0 :
            self.n_bomb -= 1





    def update(self):
        self.rect.x += self.movement_x #odpowiada za ruch na osi x
        self.rect.y += self.movement_y  # odpowiada za ruch na osi y
        #------------KOLIZJA---------------------------
        ##collids= []
        colliding_obstacles = pygame.sprite.spritecollide(self, self.level.set_of_obstacles, False)
        colliding_squares=  pygame.sprite.spritecollide(self, self.level.set_of_squares, False)
        ##collids.append(colliding_squares)

        for p in colliding_obstacles:
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

        for p in colliding_squares:
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

        if self.movement_x > 0: #prawo
            self._move(gm.IMAGES_R)

        if self.movement_x < 0: #lewo
            self._move(gm.IMAGES_L)

        if self.movement_y < 0: #gora
            self._move(gm.IMAGES_UP)

        if self.movement_y > 0:
            self._move(gm.IMAGES_DOWN)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # pygame.draw.rect(surface,(255,0,0),self.rect)

    def get_event(self, event):
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
                self.stop()
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


