import pygame, os
import module1 as gm
from pokeball import Pokeball
class Champion(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.movement_x = 0
        self.movement_y = 0
        self.press_left = False
        self.press_right = False
        self.rotate_left = False
        self.rotate_down = True
        self.rotate_right = False
        self.rotate_up = False
        self.press_up = False
        self.press_down = False
        self._count = 0
        self.pokeball_group = pygame.sprite.Group()


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.rotate_right = True
        self.rotate_left = 0
        self.rotate_down = 0
        self.rotate_up = 0
        self.movement_x = 4

    def turn_left(self):
        self.rotate_left = True
        self.rotate_right = 0
        self.rotate_down = 0
        self.rotate_up = 0
        self.movement_x = -4

    def turn_up(self):
        self.rotate_up = True
        self.rotate_down = 0
        self.rotate_left = 0
        self.rotate_right = 0
        self.movement_y = -4

    def turn_down(self):
        self.rotate_down = True
        self.rotate_up = 0
        self.rotate_left = 0
        self.rotate_right = 0
        self.movement_y = 4

    def create_pokeball(self):
        return Pokeball(gm.POKEBALL,self.rect.x, self.rect.y,
                        [self.rotate_down, self.rotate_up, self.rotate_left, self.rotate_right])
    def stop(self):
        self.movement_x = 0
        self.movement_y = 0

    def update(self):
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        #print(self.rect.x, self.rect.y)
        self.pokeball_group.update()

        if self.movement_x > 0:
            self._move(gm.SKELETON_R)

        if self.movement_x < 0:
            self._move(gm.SKELETON_L)

        if self.movement_y < 0:
            self._move(gm.SKELETON_UP)

        if self.movement_y > 0:
            self._move(gm.SKELETON_DOWN)

        colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

        for p in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom


    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.press_right = True
                self.turn_right()
            if event.key == pygame.K_LEFT:
                self.press_left = True
                self.turn_left()
            if event.key == pygame.K_UP:
                self.press_up = True
                self.turn_up()
            if event.key == pygame.K_DOWN:
                self.press_down = True
                self.turn_down()
            if event.key == pygame.K_SPACE:
                self.pokeball_group.add(self.create_pokeball())


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.press_right = False
                self.stop()
            if event.key == pygame.K_LEFT:
                self.press_left = False
                self.stop()
            if event.key == pygame.K_UP:
                self.press_up = False
                self.stop()
            if event.key == pygame.K_DOWN:
                self.press_down = False
                self.stop()

    def _move(self, image_list):
        self.image = image_list[self._count // 4]
        self._count = (self._count + 1) % 16

