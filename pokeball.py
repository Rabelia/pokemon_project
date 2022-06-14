import pygame, sys

class Pokeball(pygame.sprite.Sprite):
    def __init__(self, file_image,pos_x, pos_y, rotate):
        super().__init__()
        self.image = pygame.image.load("images/poke.png")
        #self.image.fill((255,0,0))
        #self.image.fill(pygame.image.load("images"))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
        print("stworzono")
        print(pos_x, pos_y)
        self.rotate_down = rotate[0]
        self.rotate_up = rotate[1]
        self.rotate_left = rotate[2]
        self.rotate_right = rotate[3]
        print("Lewo: ", self.rotate_left, "Prawo: ", self.rotate_right,"\n", "doł: ", self.rotate_down, "Gora: ",
              self.rotate_up)

    def update(self):
        #mamy buga jak idziesz do gory strzela w lewo XD


        # TU JEST PROBLEM
        if self.rotate_left == True:
            self.rect.x -= 5
        #rotacja w prawo?
        elif self.rotate_right == True:
            self.rect.x += 5
        #dziala dobrze
        elif self.rotate_down == True :
            self.rect.y += 5
        #leci w dol ok
        elif self.rotate_up == True:
            self.rect.y -= 5
