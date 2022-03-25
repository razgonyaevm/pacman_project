import sys

from main import main
import pygame
from scripts.generate_map import generate_map


game = main('first_map.txt', 1)
i = 2
if game == 1:
    try:
        while pygame.event.wait().type != pygame.QUIT:
            generate_map('new_map.txt', 20, 18, 3)
            game = main('new_map.txt', i)
            if game == 0:
                break
            i += 1
    except pygame.error:
        sys.exit()
