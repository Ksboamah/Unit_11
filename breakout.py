import pygame, sys
from pygame.locals import *
import paddle
import brick
import ball


def GAME_OVER(main_surface):
    main_surface.fill((0, 0, 0))
    my_font = pygame.font.SysFont("Helvetica", 50)
    label = my_font.render(" GAME OVER ", 1, ((255, 255, 255)))
    main_surface.blit(label, (100, 275))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def GAME_WNNER(main_surface):
    main_surface.fill((0, 0, 0))
    myFont = pygame.font.SysFont("Helvetica", 50)
    label = myFont.render(" WINNER ", 1, ((255, 255, 255)))
    main_surface.blit(label, (100, 275))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


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

        for x in range(2):

            for x in range(BRICKS_PER_ROW):
                MY_BRICK = brick.Brick(main_surface, BRICK_WIDTH, BRICK_HEIGHT, color)
                MY_BRICK.rect.x = x_pos
                MY_BRICK.rect.y = y_pos
                main_surface.blit(MY_BRICK.image, MY_BRICK.rect)
                brick_group.add(MY_BRICK)
                x_pos += BRICK_SEP + BRICK_WIDTH

            y_pos += BRICK_HEIGHT + BRICK_SEP
            x_pos = BRICK_SEP

    paddle_group = pygame.sprite.Group()
    MY_PADDLE = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    MY_PADDLE.rect.x = APPLICATION_WIDTH / 2
    MY_PADDLE.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    paddle_group.add(MY_PADDLE)

    main_surface.blit(MY_PADDLE.image, MY_PADDLE.rect)

    MY_BALL = ball.Ball(BLACK, (APPLICATION_WIDTH), (APPLICATION_HEIGHT), RADIUS_OF_BALL)
    MY_BALL.rect.x = APPLICATION_WIDTH / 2
    MY_BALL.rect.y = APPLICATION_HEIGHT / 2
    main_surface.blit(MY_BALL.image, MY_BALL.rect)

    while True:
        main_surface.fill(WHITE)
        MY_PADDLE.move(pygame.mouse.get_pos())
        main_surface.blit(MY_PADDLE.image, MY_PADDLE.rect)
        MY_BALL.move()
        main_surface.blit(MY_BALL.image, MY_BALL.rect)
        MY_BALL.collide(brick_group)
        MY_BALL.paddle_collide(paddle_group)
        for x in brick_group:
            main_surface.blit(x.image, x.rect)
        if MY_BALL.rect.y >= APPLICATION_HEIGHT:
            NUM_TURNS += -1
            if NUM_TURNS == 0:
                break
            else:
                MY_BALL.rect.x = APPLICATION_WIDTH / 2
                MY_BALL.rect.y = APPLICATION_HEIGHT / 2
        if NUM_TURNS == 0:
            GAME_OVER(main_surface)
        if len(brick_group) == 0:  # when is no more bricks in the game the program will show WINNER
            GAME_WNNER(main_surface)
        main_surface.blit(MY_BALL.image, MY_BALL.rect)
        MY_BALL.paddle_collide(paddle_group)
        MY_BALL.brick_collide(brick_group)
        if NUM_TURNS == 0:
            break
        if brick_group == 0:
            break
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

main()
