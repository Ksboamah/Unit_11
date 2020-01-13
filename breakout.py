import pygame, sys
from pygame.locals import *
import paddle
import brick

def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    main_surface.fill((255, 255, 255))


    brick_colors = [RED, ORANGE, YELLOW, GREEN, CYAN]
    brick_group = pygame.sprite.Group()

    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET


    for color in brick_colors:
        MY_BRICK = brick.Brick(main_surface, BRICK_WIDTH, BRICK_HEIGHT, color)
        for x in range(2):
            MY_BRICK.rect.x = x_pos
            MY_BRICK.rect.y = y_pos
            for x in range(BRICKS_PER_ROW + 1):
                main_surface.blit(MY_BRICK.image, (((x_pos + BRICK_WIDTH) * x), y_pos))
                brick_group.add(MY_BRICK)
            x_pos = BRICK_SEP
            y_pos += BRICK_HEIGHT + BRICK_SEP


    paddle_group = pygame.sprite.Group()
    MY_PADDLE = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    MY_PADDLE.rect.x = APPLICATION_WIDTH / 2
    MY_PADDLE.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    paddle_group.add(MY_PADDLE)

    main_surface.blit(MY_PADDLE.image, MY_PADDLE.rect)

    while True:
        main_surface.fill(WHITE)
        for x in brick_group:
            main_surface.blit(x.image, x.rect)
        MY_PADDLE.move(pygame.mouse.get_pos())
        main_surface.blit(MY_PADDLE.image, MY_PADDLE.rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

main()
