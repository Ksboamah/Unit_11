import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius
        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((radius, radius))
        self.rect = self.image.get_rect()
        self.image.fill(color)
        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, (0, 0, 0), (int(windowWidth/2), int(windowHeight/2)), radius, 0)
        self.x_speed = 3
        self.y_speed = 4

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left < 0 or self.rect.right > self.windowWidth:
            self.x_speed = -self.x_speed
        if self.rect.top < 0:
            self.y_speed = -self.y_speed

    def collide(self, sprite_group):
        if pygame.sprite.spritecollide(self, sprite_group, True):
            self.y_speed = -self.y_speed

    def paddle_collide(self, sprite_group):
        if pygame.sprite.spritecollide(self, sprite_group, False):
            self.y_speed = -self.y_speed