import os
import pygame
import game_config as gm


from models.Player import Player
from levels.Level1 import Level1


class Game:
    def __init__(self):
        # centrowanie okna
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption('Bomberman')

        # ustawienia ekranu i gry
        self.screen = pygame.display.set_mode(gm.SIZESCREEN)
        self.clock = pygame.time.Clock()
        self.player = Player(gm.STAND_R)
        self.current_level = Level1(self.player)
        self.player.level = self.current_level
        self.player.rect.center = self.screen.get_rect().center

    def start(self):
        # głowna pętla gry
        window_open = True
        while window_open:
            self.screen.blit(gm.BACKGROUND,[0,0])
            # pętla zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        window_open = False
                elif event.type == pygame.QUIT:
                    window_open = False

                self.player.get_event(event)

            # rysowanie i aktualizacja obiektów
            self.player.update()
            self.current_level.update()
            self.player.draw(self.screen)
            self.current_level.draw(self.screen)

            # aktualizacja okna pygame
            pygame.display.flip()
            self.clock.tick(30)

            # koniec gry jak nas monster zlapie np.
            if not self.current_level.running:
                window_open = False

        pygame.quit()


game = Game()
game.start()
