import pygame, os

SIZESCREEN = WIDTH, HEIGHT = 720, 512
LIGHTBLUE = pygame.color.THECOLORS['lightblue']

screen = pygame.display.set_mode(SIZESCREEN)

#background

path = os.path.join('images')
file_names = sorted(os.listdir(path))
print(file_names)
file_names.remove('map1.jpg')

BACKGROUND = pygame.image.load(os.path.join(path, 'map1.jpg'))
for file_name in file_names:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)

SKELETON_DOWN = [SKELETON, SKELETON1, SKELETON2, SKELETON3]
SKELETON_UP = [SKELETON_B, SKELETON_B1, SKELETON_B2, SKELETON_B3]
SKELETON_R = [SKELETON_R, SKELETON_R1, SKELETON_R2, SKELETON_R3]
SKELETON_L = [SKELETON_L, SKELETON_L1, SKELETON_L2, SKELETON_L3]
BUILDINGS = [HOSPITAL, LABOLATORIUM]
#GRASS_LIST = [GRASS1, GRASS2, GRASS1, GRASS2]