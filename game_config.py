import os
import pygame

pygame.init()

# kolory
DARKRED = pygame.color.THECOLORS['darkred']
LIGHTRED = pygame.color.THECOLORS['palevioletred']
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
BLACK = pygame.color.THECOLORS['black']
LIGHTGREEN = pygame.color.THECOLORS['lightgreen']

# okno główne
os.environ['SDL_VIDEO_CENTERED'] = '1'    # centrowanie okna
SIZESCREEN = WIDTH, HEIGHT = 1366, 740
SQUARE_SIZE = 64
screen = pygame.display.set_mode(SIZESCREEN)

# grafika  - wczytywanie znaków
file_names = sorted(os.listdir('png'))
file_names.remove('background.png')
BACKGROUND = pygame.image.load(os.path.join('png', 'background.png')).convert()
for file_name in file_names:
    image_name = file_name[:-4]
    if '_L' in image_name or '_R' in image_name:
        image_name = image_name.upper()
    elif 'L' in image_name:
        image_name = image_name.replace('L', '_L').upper()
    elif 'R' in image_name:
        image_name = image_name.replace('R', '_R').upper()
    else:
       image_name = image_name.upper()
    if 'PLAYER_' in image_name:
        image_name = image_name.replace('PLAYER_', '').upper()
    globals().__setitem__(image_name, pygame.image.load(
        os.path.join('png', file_name)).convert_alpha(BACKGROUND))

# grafika postać
PLATFORM_CELLS = [GROUND_06, CRATE_01]

# grafika postać
IMAGES_R = [WALK_R1, WALK_R2, WALK_R3]
IMAGES_L = [WALK_L1, WALK_L2, WALK_L3]
IMAGES_UP = [UP_R,UP_L]
IMAGES_DOWN = [DOWN_R,DOWN_L]

# grafika stwory
MONSTERS_ELEPHANT = []
MONSTERS_MONKEY = []
MONSTERS_PIG = []

MONSTER_STAND_L = [MONKEY]
MONSTER_STAND_R = [PIG]

# grafika bomb
BOMB_SET = [BOMB_SET1]
FIRE_SET = []
