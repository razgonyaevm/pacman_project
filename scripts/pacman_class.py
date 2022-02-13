import pygame

from main import height, width
from scripts.load_im import load_image


class Pacman(pygame.sprite.Sprite):
    image = load_image("pacman.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Pacman.image
        self.rect = self.image.get_rect()
        self.rect.x = 50 * 10
        self.rect.y = height - 53
        self.key = 1

    def click(self, event):
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_UP]:
                if self.rect.y - 53 > -50:
                    self.rect.y -= 53
                else:
                    self.rect.y = height - 51
                if self.key == 1:
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.key == 3:
                    self.image = pygame.transform.rotate(self.image, 270)
                elif self.key == 4:
                    self.image = pygame.transform.rotate(self.image, 180)
                self.key = 2
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                if self.rect.y + 53 < height:
                    self.rect.y += 53
                else:
                    self.rect.y = 0
                if self.key == 1:
                    self.image = pygame.transform.rotate(self.image, 270)
                elif self.key == 2:
                    self.image = pygame.transform.rotate(self.image, 180)
                elif self.key == 3:
                    self.image = pygame.transform.rotate(self.image, 90)
                self.key = 4
            elif pygame.key.get_pressed()[pygame.K_LEFT]:
                if self.rect.x - 50 > -48:
                    self.rect.x -= 50
                else:
                    self.rect.x = width - 50
                if self.key == 1:
                    self.image = pygame.transform.rotate(self.image, 180)
                elif self.key == 2:
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.key == 4:
                    self.image = pygame.transform.rotate(self.image, 270)
                self.key = 3
            elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                if self.rect.x + 50 < width:
                    self.rect.x += 50
                else:
                    self.rect.x = 0
                if self.key == 2:
                    self.image = pygame.transform.rotate(self.image, 270)
                elif self.key == 3:
                    self.image = pygame.transform.flip(self.image, True, False)
                elif self.key == 4:
                    self.image = pygame.transform.rotate(self.image, 90)
                self.key = 1
