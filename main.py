import os.path
import sys

import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pac_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Pacman(pygame.sprite.Sprite):
    image = load_image("pacman.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Pacman.image
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - 25
        self.rect.y = height - 53
        self.key = 1

    def click(self, event):
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_UP]:
                if self.rect.y - 10 >= 0:
                    self.rect.y -= 10
                if self.key == 1:
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.key == 3:
                    self.image = pygame.transform.rotate(self.image, 270)
                elif self.key == 4:
                    self.image = pygame.transform.rotate(self.image, 180)
                self.key = 2
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                if self.rect.y + 10 <= height - 53:
                    self.rect.y += 10
                if self.key == 1:
                    self.image = pygame.transform.rotate(self.image, 270)
                elif self.key == 2:
                    self.image = pygame.transform.rotate(self.image, 180)
                elif self.key == 3:
                    self.image = pygame.transform.rotate(self.image, 90)
                self.key = 4
            elif pygame.key.get_pressed()[pygame.K_LEFT]:
                if self.rect.x - 10 >= 0:
                    self.rect.x -= 10
                if self.key == 1:
                    self.image = pygame.transform.rotate(self.image, 180)
                elif self.key == 2:
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.key == 4:
                    self.image = pygame.transform.rotate(self.image, 270)
                self.key = 3
            elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                if self.rect.x + 10 <= width - 50:
                    self.rect.x += 10
                if self.key == 2:
                    self.image = pygame.transform.rotate(self.image, 270)
                elif self.key == 3:
                    self.image = pygame.transform.flip(self.image, True, False)
                elif self.key == 4:
                    self.image = pygame.transform.rotate(self.image, 90)
                self.key = 1


pacman = Pacman(pac_sprites)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for pac in pac_sprites:
            pac.click(event)
    screen.fill((0, 0, 0))
    pac_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
