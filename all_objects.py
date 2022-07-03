import pygame
import module as gm
import random
class Base(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.mask = pygame.mask.from_surface(file_image)
        self.rect = file_image.get_rect()
        self.movement_x = 0
        self.movement_y = 0
        self.press_left = False
        self.press_right = False
        self.press_up = False
        self.press_down = False
        self._count = 0


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _move(self, image_list):
        self.image = image_list[self._count // 4]
        self._count = (self._count + 1) % 16

    def update(self):
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y

    def stop(self):
        self.movement_x = 0
        self.movement_y = 0

    def get_event(self, event):
       pass

    def collision(self, object, level):
        pass

    def animations(self):
        pass



class Champion(Base):
    def __init__(self, image):
        super().__init__(image)
        self.rect.center = 150, 300
        self.press_left = False
        self.press_right = False
        self.rotate_down = True
        self.rotate_up = False
        self.rotate_left = False
        self.rotate_right = False

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

    def create_pokeball(self):
        return Pokeball(gm.POKEBALL)

    def turn_right(self):
        self.rotate_right = True
        self.rotate_left = False
        self.rotate_down = False
        self.rotate_up = False
        self.movement_x = 4

    def turn_left(self):
        self.rotate_left = True
        self.rotate_right = False
        self.rotate_down = False
        self.rotate_up = False
        self.movement_x = -4

    def turn_up(self):
        self.rotate_up = True
        self.rotate_down = False
        self.rotate_left = False
        self.rotate_right = False
        self.movement_y = -4

    def turn_down(self):
        self.rotate_down = True
        self.rotate_up = False
        self.rotate_left = False
        self.rotate_right = False
        self.movement_y = 4

    def create_pokeball(self):
        return Pokeball(self.rect.x, self.rect.y,[self.rotate_down, self.rotate_up, self.rotate_left, self.rotate_right])

    def stop(self):
        self.movement_x = 0
        self.movement_y = 0

class Pokeball(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, rotate):
        super().__init__()
        self.image = pygame.image.load("images/poke.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
        # print(self.rect.x, self.rect.y)
        self.rotate_down = rotate[0]
        self.rotate_up = rotate[1]
        self.rotate_left = rotate[2]
        self.rotate_right = rotate[3]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        if self.rotate_left == True:
            self.rect.x -= 5

        elif self.rotate_right == True:
            self.rect.x += 5

        elif self.rotate_down == True :
            self.rect.y += 5

        elif self.rotate_up == True:
            self.rect.y -= 5

    def collide(self, ob):
        if self.rect.colliderect(ob.rect):
            ob.kill()


class Pokemons_respawn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"sprites/{str(random.randint(2,386))}.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(gm.WIDTH - self.rect.width)
        self.rect.y = random.randrange(150, 400)
        self.score = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def collide(self, ob):
        if self.rect.colliderect(ob.rect):
            ob.kill()

    # def scoreboard(self):
    #     if self.rect.colliderect(ob.rect):
    #         self.score += 1
    #         return self.score


