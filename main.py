import pygame, os
import module as gm

from all_objects import Pokemons_respawn, Champion

def menu():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Pokemon")
    screen = pygame.display.set_mode(gm.SIZESCREEN)
    pygame.init()
    open_window = True
    while open_window:
        screen.fill("black")

        pygame.font.init()
        start_menu = pygame.font.SysFont(None, 75)
        start_text = start_menu.render("To start press ENTER", True, "White")
        screen.blit(start_text,(100, 200))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game().start()
                elif event.key == pygame.K_ESCAPE:
                    open_window = False
            if event.type == pygame.QUIT:
                open_window = False
        pygame.display.flip()
    pygame.quit()


def show_score(surface, score):

    scorefont = pygame.font.SysFont(None, 14)
    scorerender = scorefont.render("POKEMON CAUGHT: " + str(score), True, "BLACK")
    surface.blit(scorerender, (10, 10))


def game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
    pygame.display.set_caption("Pokemon")
    pygame.display.init()

    # ustawienia ekranu
    screen = pygame.display.set_mode(gm.SIZESCREEN)
    time = pygame.time.Clock()

    champion = Champion(gm.SKELETON)
    champion.rect.bottom = gm.HEIGHT - 70
    champion.rect.left = 150
    pokeball = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    score = 0

    #create poksy
    for i in range(10):
        m = Pokemons_respawn()
        mobs.add(m)

    open_window = True
    while open_window:
        screen.fill(gm.LIGHTBLUE)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pokeball.add(champion.create_pokeball())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    open_window = False
            elif event.type == pygame.QUIT:
                open_window = False
        champion.get_event(event)

        for i in pokeball:
            for pok in mobs:
                if i.rect.colliderect(pok.rect):
                    score += 1
                    pok.kill()
                    i.kill()
                    if mobs.__len__() == 0:
                        for i in range(10):
                            m = Pokemons_respawn()
                            mobs.add(m)

        pokeball.draw(screen)
        pokeball.update()
        mobs.draw(screen)
        champion.update()
        champion.draw(screen)
        show_score(screen, score)
        pygame.display.flip()
        time.tick(30)

    pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    menu()