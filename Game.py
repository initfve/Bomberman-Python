import os
import pygame
import game_config as gm
import pygame_gui as gui

from models.Player import Player
from levels.Level1 import Level1


class Game:
    def __init__(self, lives=3, score=0):
        # centrowanie okna
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption('Bomberman')

        # ustawienia ekranu i gry
        self.screen = pygame.display.set_mode(gm.SIZESCREEN)
        self.clock = pygame.time.Clock()
        self.player = Player(gm.STAND_R)
        self.player.score = score
        self.player.current_health = lives
        self.current_level = Level1(self.player)
        self.player.level = self.current_level
        # ustawiamy gracza w lewym górnym
        self.player.rect.x = 64
        self.player.rect.y = 64

        # ustawienia gry, manager ui oraz własności czy gra się toczy czy jest spauzowana
        self.manager = gui.UIManager((gm.WIDTH, gm.HEIGHT), 'theme.json')
        self.running = True
        self.paused = False

    def _toggle_pause(self):
        self.paused = not self.paused

    def start(self):
        # UI
        start_button = gui.elements.UIButton(
            relative_rect=pygame.Rect(gm.WIDTH - 100, gm.HEIGHT - gm.UIHEIGHT, 100, gm.UIHEIGHT),
            text='PAUSE',
            manager=self.manager)

        gui.elements.UIScreenSpaceHealthBar(
            relative_rect=pygame.Rect(0, gm.HEIGHT - gm.UIHEIGHT, 100, gm.UIHEIGHT),
            manager=self.manager,
            sprite_to_monitor=self.player)

        lost_modal = gui.elements.UITextBox('Przegrałeś - Koniec gry',
                                            relative_rect=pygame.Rect(int(gm.WIDTH / 2) - 100,
                                                                      int(gm.HEIGHT / 2) - 20, 200, 40),
                                            manager=self.manager)

        restart_modal = gui.elements.UITextBox('Restart...',
                                               relative_rect=pygame.Rect(int(gm.WIDTH / 2) - 80,
                                                                         int(gm.HEIGHT / 2) - 20, 140,
                                                                         40),
                                               manager=self.manager)

        restart_modal.hide()
        lost_modal.hide()

        clock = pygame.time.Clock()

        restart = False
        lost = False

        # głowna pętla gry
        while self.running:
            score = gui.elements.UITextBox(f'Wynik: {self.player.score}',
                                           relative_rect=pygame.Rect(int(gm.WIDTH / 2) - 40,
                                                                     gm.HEIGHT - gm.UIHEIGHT, 120,
                                                                     gm.UIHEIGHT),
                                           manager=self.manager)
            score.disable()

            time_delta = clock.tick(60) / 1000.0
            self.screen.blit(gm.BACKGROUND, [0, 0])

            # pętla zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                elif event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == pygame.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == start_button:
                            self._toggle_pause()
                            if self.paused:
                                start_button.set_text('PLAY')
                            else:
                                start_button.set_text('PAUSE')

                self.manager.process_events(event)
                self.player.get_event(event)

            self.manager.update(time_delta)

            if not self.paused:
                # aktualizacja obiektów
                self.player.update()
                self.current_level.update()

            # rysowanie obiektów
            self.player.draw(self.screen)
            self.current_level.draw(self.screen)

            # rysowanie ui
            self.manager.draw_ui(self.screen)

            # aktualizacja okna pygame
            pygame.display.flip()
            self.clock.tick(30)

            if restart:
                pygame.time.wait(2000)
                Game(self.player.current_health, self.player.score).start()
                pygame.quit()
            elif lost:
                pygame.time.wait(2000)
                pygame.quit()

            # koniec gry jak nas monster zlapie np.
            if not self.current_level.running:
                self._toggle_pause()
                if self.player.current_health > 0:
                    restart_modal.show()
                    restart = True
                else:
                    lost_modal.show()
                    lost = True

            score.kill()


game = Game()
game.start()
