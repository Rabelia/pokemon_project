import pygame, os
import module1 as gm
import champion

os.environ['SDL_VIDEO_CENTERED'] = '1' #centrowanie okna

pygame.init()

#ustawienia ekranu
screen = pygame.display.set_mode(gm.SIZESCREEN)
time = pygame.time.Clock()

champion = champion.Champion(gm.SKELETON)
champion.rect.bottom = gm.HEIGHT - 70
champion.rect.left = 150

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
        champion.get_event(event)

    champion.update()
    champion.draw(screen)
    pygame.display.flip()
    time.tick(30)

pygame.display.flip()



pygame.quit()