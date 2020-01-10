import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, surface, width, height, color):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.surface = surface
        self.width = width
        self.height = height
        self.color = color

        # Create a surface with the correct height and width
        self.image = pygame.Surface((width, height))

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        self.image.fill(color)

    def draw(self, loc_x, loc_y):
        pygame.draw.rect(self.surface, self.color, (loc_x, loc_y, self.width, self.height), 0)