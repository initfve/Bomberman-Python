import random
import game_config as gm

# import modeli i klasy bazowej level
from levels.Level import Level
from models.Border import Border
from models.Obstacle import Obstacle


class Level1(Level):
    def __init__(self, player=None):
        super().__init__(player)
        self.create_board()

    # funkcja tworząca plansze
    def create_board(self):
        borders = []
        spare_fields = []

        # generacja pól
        for i in range(int(gm.WIDTH / gm.SQUARE_SIZE)):
            for j in range(int(gm.HEIGHT / gm.SQUARE_SIZE)):
                if i == 0 or j == 0 or i == range(int(gm.WIDTH / gm.SQUARE_SIZE))[-1] or j == \
                        range(int(gm.HEIGHT / gm.SQUARE_SIZE))[-1] or (i % 2 == 0 and j % 2 == 0):
                    # dodawanie ramek oraz nie destrukcyjnych kwadratów w parzystych indeksach
                    borders.append([gm.SQUARE_SIZE, i * gm.SQUARE_SIZE, j * gm.SQUARE_SIZE])
                    continue

                # reszte pol dodajemy do listy wolnych pol
                spare_fields.append([gm.SQUARE_SIZE, i * gm.SQUARE_SIZE, j * gm.SQUARE_SIZE])

        # skoro juz wiemy gdzie sa bordery chcemy wstawic w to miejsce obiekt
        for border in borders:
            border_object = Border(gm.PLATFORM_CELLS[0], *border)
            self.set_of_squares.add(border_object)

        # tutaj wstawiamy destrukcyjne obiekty typu Obstacle
        for field in spare_fields:
            obstacle_object = Obstacle(gm.PLATFORM_CELLS[1], *field)
            self.set_of_obstacles.add(obstacle_object)

        # musimy natomiast randomo usunac z listy wszystkich wolnych pol obiekty przeszkody destrukcyjne
        # bo bez tego nie mielibysmy pustych pol
        self.set_of_obstacles = self._random_empty_list(self.set_of_obstacles)

    # funkcja usuwajaca losowa ilosc elementow z listy
    def _random_empty_list(self, source_list):
        list_len = len(source_list)
        output_list = random.sample(source_list, random.randint(0, int(list_len / 2)))

        return output_list
