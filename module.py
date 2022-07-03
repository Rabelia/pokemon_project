import pygame, os

SIZESCREEN = WIDTH, HEIGHT = 720, 512
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
path = os.path.join('images')
file_names = sorted(os.listdir(path))

#BACKGROUND = pygame.image.load(os.path.join(path, 'map1.jpg'))

for file_name in file_names:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(path, file_name))

SKELETON_DOWN = [SKELETON, SKELETON1, SKELETON2, SKELETON3]
SKELETON_UP = [SKELETON_B, SKELETON_B1, SKELETON_B2, SKELETON_B3]
SKELETON_R = [SKELETON_R, SKELETON_R1, SKELETON_R2, SKELETON_R3]
SKELETON_L = [SKELETON_L, SKELETON_L1, SKELETON_L2, SKELETON_L3]
#BUILDINGS = [HOSPITAL, LABOLATORIUM]
POKEMONS = [POKEMON1 ,POKEMON2]
POKEBALL = [BALL]
