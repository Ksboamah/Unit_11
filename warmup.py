import pygame, sys
from pygame.locals import *
import block


pygame.init()
main_window = pygame.display.set_mode((500, 500), 32, 0)
pygame.display.set_caption("Animation")

BLUE = (0, 0, 255)
WIDTH = 25
HEIGHT = 25



while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()




