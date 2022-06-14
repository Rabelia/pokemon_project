
import pygame, os
import module1 as gm

class OurMap(pygame.sprite.Sprite):
    def __init__(self, image_list, width, height, pos_x, pos_y):
        super().__init__()
        self.image_list = image_list
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def draw(self, surface):
        if self.width <= 80:
            surface.blit(self.image_list[0], self.rect)
        else:
            surface.blit(self.image_list[1], self.rect)

        #surface.blit(self.image_list[1], [self.rect.x + self.width - 70, self.rect.y])

class Level:
    def __init__(self, player):
        self.player = player
        self.set_of_platforms = set()
        self.set_of_pokemons = set()
        self.world_shift = 0

    def draw(self, surface):
        for platform in self.set_of_platforms:
            platform.draw(surface)
        for pokemons in self.set_of_pokemons:
            pokemons.draw(surface)


    def update(self):
        if self.player.rect.right >= 500:
            diff = self.player.rect.right - 500
            self.player.rect.right = 500
            self._shift_world_LR(-diff)

        if self.player.rect.left <= 150:
            diff = 150 - self.player.rect.left
            self.player.rect.left = 150
            self._shift_world_LR(diff)


        if self.player.rect.top >= 300:
            diff = self.player.rect.top - 300
            self.player.rect.top = 300
            self._shift_world_TD(-diff)

        if self.player.rect.bottom <= 150:
            diff = 150 - self.player.rect.bottom
            self.player.rect.bottom = 150
            self._shift_world_TD(diff)

    def _shift_world_LR(self, shift_x):
        for p in self.set_of_platforms:
            p.rect.x += shift_x
        for pok in self.set_of_pokemons:
            pok.rect.x += shift_x

    def _shift_world_TD(self, shift_y):
        for p in self.set_of_platforms:
            p.rect.y += shift_y
        for pok in self.set_of_pokemons:
            pok.rect.y += shift_y

class Level1(Level):
    def __init__(self, player = None):
        super().__init__(player)
        self._create_platforms()
        self._create_pokemons()

    def _create_platforms(self):
        # lista [width, height, pos-x, pos-y]
        building = [[80, 65, 100, 200],
                    [85, 60, 400, 300]]

        for build in building:
            self.set_of_platforms.add(OurMap(gm.BUILDINGS, *build))
    def _create_pokemons(self):
        pokemons = [[50,50,200,300],[60,50,300,150]]

        for poke in pokemons:
            self.set_of_pokemons.add(OurMap(gm.POKEMONS, *poke))