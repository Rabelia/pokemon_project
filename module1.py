import pygame, os

SIZESCREEN = WIDTH, HEIGHT = 720, 720

screen = pygame.display.set_mode(SIZESCREEN)

#background

path = os.path.join('images')
file_names = sorted(os.listdir(path))
print(file_names)
file_names.remove('map1.jpg')
BACKGROUND = pygame.image.load(os.path.join(path, 'map1.jpg'))




