import pygame, os
import module1 as gm

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
        self.rotate_down = False
        self.press_up = False
        self.press_down = False
        self.eq = {}
        self.level = None
        self._count = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.rotate_left = False
        self.movement_x = 4

    def turn_left(self):
        self.rotate_left = True
        self.movement_x = -4

    def turn_up(self):
        self.rotate_down = False
        self.movement_y = -4

    def turn_down(self):
        self.rotate_down = True
        self.movement_y = 4

    def stop(self):
        self.movement_x = 0
        self.movement_y = 0

    def update(self):
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y

        if self.movement_x > 0:
            self._move(gm.SKELETON_R)

        if self.movement_x < 0:
            self._move(gm.SKELETON_L)

        if self.movement_y < 0:
            self._move(gm.SKELETON_UP)

        if self.movement_y > 0:
            self._move(gm.SKELETON_DOWN)

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
