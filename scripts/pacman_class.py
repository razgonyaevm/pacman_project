import pygame

from scripts.load_im import load_image

with open('data/map_size.txt') as map_size:
    m = list(map(int, map_size.readline().split()))
    size = width, height = m[0], m[1]


class Pacman(pygame.sprite.Sprite):
    """Класс главного героя"""
    pygame.init()
    image = load_image("pacman.png")

    def __init__(self, name, *group):
        super().__init__(*group)
        with open(f'maps/{name}') as map_file:
            self.map_f = list(map(lambda x: x.strip(), map_file.readlines()))
        self.image = Pacman.image
        self.rect = self.image.get_rect()
        self.rect.x = ((width // 50) // 2) * 50
        self.rect.y = height - 53
        self.key = 1

    def click(self, event):
        """отслеживает нажатия и перемещение героя"""
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_UP]:
                if self.rect.y - 53 > -50:
                    if self.map_f[(self.rect.y - 53) // 53][self.rect.x // 50] != '#':
                        self.rect.y -= 53
                else:
                    self.rect.y = height - 53
                if self.key == 1:
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.key == 3:
                    self.image = pygame.transform.rotate(self.image, 270)
                elif self.key == 4:
                    self.image = pygame.transform.rotate(self.image, 180)
                self.key = 2
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                if self.rect.y + 53 < height:
                    if self.map_f[(self.rect.y + 53) // 53][self.rect.x // 50] != "#":
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
                    if self.map_f[self.rect.y // 53][(self.rect.x - 50) // 50] != '#':
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
                    if self.map_f[self.rect.y // 53][(self.rect.x + 50) // 50] != '#':
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
