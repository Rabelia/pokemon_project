import pygame, os
import module1 as gm
import champion
import map
from champion import Champion
os.environ['SDL_VIDEO_CENTERED'] = '1' #centrowanie okna
pygame.display.set_caption("Pokemon")
pygame.init()

#ustawienia ekranu
screen = pygame.display.set_mode(gm.SIZESCREEN)
time = pygame.time.Clock()

champion = champion.Champion(gm.SKELETON)
champion.rect.bottom = gm.HEIGHT - 70
champion.rect.left = 150
our_level = map.Level1(champion)
our_level.draw(screen)
champion.level =our_level
bullet_group = pygame.sprite.Group()

open_window = True

while open_window:
    screen.fill(gm.LIGHTBLUE)

    #background image
    #screen.blit(gm.BACKGROUND, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                open_window = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(champion.create_pokeball())
        champion.get_event(event)

    champion.update()
    champion.draw(screen)
    our_level.update()
    our_level.draw(screen)
    bullet_group.draw(screen)
    bullet_group.update()
    pygame.display.flip()
    time.tick(30)

pygame.display.flip()



pygame.quit()