import random
import game_config as gm

# import modeli i klasy bazowej level
from levels.Level import Level
from models.Border import Border
from models.Doors import Doors
from models.Monster import Monster
from models.Obstacle import Obstacle
from models.Bomb import Bomb


class Level1(Level):
    def __init__(self, player=None):
        super().__init__(player)
        self.monster_max_count = 5
        self.create_board()

    # funkcja tworząca plansze
    def create_board(self):
        borders = []
        spare_fields = []
        player_starter_fields = [[64, 64, 64], [64, 64, 128], [64, 128, 64]]

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

        # usuwamy pola startowe z wolnych pól
        spare_fields = [x for x in spare_fields if x not in player_starter_fields]

        # skoro juz wiemy gdzie sa bordery chcemy wstawic w to miejsce obiekt
        self.append_model(self.set_of_squares, borders, gm.PLATFORM_CELLS[0], 'border')

        # backup dla potworków
        temp_spare_fields = spare_fields

        # musimy natomiast randomo usunac z listy wszystkich wolnych pol obiekty przeszkody destrukcyjne
        # bo bez tego nie mielibysmy pustych pol
        spare_fields = self._random_empty_list(spare_fields, int(len(spare_fields) / 3), int(len(spare_fields) / 2))

        # tutaj wstawiamy destrukcyjne obiekty typu Obstacle
        self.append_model(self.set_of_obstacles, spare_fields, gm.PLATFORM_CELLS[1], 'obstacle')

        # dodawanie drzwi
        self.doors = Doors(gm.LEVEL_DOORS[0], *random.choice(spare_fields))

        # dodawanie jakichś potworków
        spare_fields = self._random_empty_list(self.list_diff(temp_spare_fields, spare_fields), 1, self.monster_max_count)
        self.append_model(self.set_of_monsters, spare_fields, gm.MONSTER[0], 'monster')

    # funkcja usuwajaca losowa ilosc elementow z listy
    def _random_empty_list(self, source_list, start, desired_length):
        return random.sample(source_list, random.randint(start, desired_length))

    def list_diff(level, first_list, second_list):
        return [x for x in first_list if x not in second_list]

    # wypełniamy planszę modelami
    def append_model(self, models_set, fields_list, texture, object_type):
        if object_type == 'monster':
            for field in fields_list:
                # 4 to jest maksymalna liczba potworów do losowego renderowania
                border_object = Monster(texture, 4, *field)
                models_set.add(border_object)
        elif object_type == 'obstacle':
            for field in fields_list:
                border_object = Obstacle(texture, *field)
                models_set.add(border_object)
        elif object_type == 'border':
            for field in fields_list:
                border_object = Border(texture, *field)
                models_set.add(border_object)
