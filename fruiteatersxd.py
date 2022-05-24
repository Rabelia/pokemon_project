import pygame, os
import module1 as gm

os.environ['SDL_VIDEO_CENTERED'] = '1' #centrowanie okna

pygame.init()

#ustawienia ekranu
screen = pygame.display.set_mode(gm.SIZESCREEN)
time = pygame.time.Clock()



open_window = True

while open_window:
    screen.fill((0, 0, 0))

    #background image
    screen.blit(gm.BACKGROUND, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                open_window = False

    pygame.display.flip()



pygame.quit()