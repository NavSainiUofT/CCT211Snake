import time, random
import pygame
from tkinter import *
import tkinter 
import tkinter.messagebox
BLOCK_SIZE = 20
FPS = 15

BACKGROUND = (255, 255, 255)
BLACK = (0, 0, 0)
APPLE = (255, 0, 0)
SNAKE1 = (0, 155, 0)
SNAKE2 = (0, 0, 255)

clock = pygame.time.Clock()

winning_snake = ''
def gameLoop(gamerunvalue, gameDisplay):
    gameOver = gamerunvalue

    snake_1_head_x = (DISPLAY_WIDTH / 2) + 10  # x and y locations for the head of the snake
    snake_1_head_y = (DISPLAY_HEIGHT / 2) + 10
    snake_2_head_x = (DISPLAY_WIDTH / 2) - 10  # x and y locations for the head of the snake
    snake_2_head_y = (DISPLAY_HEIGHT / 2) - 10

    lead_dx_1 = BLOCK_SIZE
    lead_dy_1 = 0

    lead_dx_2 = BLOCK_SIZE
    lead_dy_2 = 0
    direction1 = 'right'
    direction2 = 'left'
    randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    snakelist1 = []
    snakelist2 = []
    snake_1_length = 1
    snake_2_length = 1
    score = 1

    while gameOver is not True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction1 is not 'right':
                    lead_dx_1 = -BLOCK_SIZE
                    lead_dy_1 = 0
                    direction1 = 'left'
                elif event.key == pygame.K_RIGHT and direction1 is not 'left':
                    lead_dx_1 = BLOCK_SIZE
                    lead_dy_1 = 0
                    direction1 = 'right'
                elif event.key == pygame.K_UP and direction1 is not 'down':
                    lead_dy_1 = -BLOCK_SIZE
                    lead_dx_1 = 0
                    direction1 = 'up'
                elif event.key == pygame.K_DOWN and direction1 is not 'up':
                    lead_dy_1 = BLOCK_SIZE
                    lead_dx_1 = 0
                    direction1 = 'down'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and direction2 is not 'right':
                    lead_dx_2 = -BLOCK_SIZE
                    lead_dy_2 = 0
                    direction2 = 'left'
                elif event.key == pygame.K_d and direction2 is not 'left':
                    lead_dx_2 = BLOCK_SIZE
                    lead_dy_2 = 0
                    direction2 = 'right'
                elif event.key == pygame.K_w and direction2 is not 'down':
                    lead_dy_2 = -BLOCK_SIZE
                    lead_dx_2 = 0
                    direction2 = 'up'
                elif event.key == pygame.K_s and direction2 is not 'up':
                    lead_dy_2 = BLOCK_SIZE
                    lead_dx_2 = 0
                    direction2 = 'down'

        snake_1_head_x += lead_dx_1
        snake_1_head_y += lead_dy_1
        
        snake_2_head_x += lead_dx_2
        snake_2_head_y += lead_dy_2

        gameDisplay.fill(BACKGROUND)

        appleThickness = 30
        pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY, appleThickness, appleThickness])

        for xy in snakelist1:
            pygame.draw.rect(gameDisplay, SNAKE1, [xy[0], xy[1], BLOCK_SIZE, BLOCK_SIZE])

        for xy in snakelist2:
            pygame.draw.rect(gameDisplay,SNAKE2, [xy[0], xy[1], BLOCK_SIZE, BLOCK_SIZE])
            
        for xy in snakelist1:
            if snake_2_head == xy:
                winning_snake = 'snake 1'
                gameOver = True

        for xy in snakelist2:
            if snake_1_head == xy:
                winning_snake = 'snake 2'
                gameOver = True

        if snake_1_head_x >= DISPLAY_WIDTH or snake_1_head_x < 0 or snake_1_head_y >= DISPLAY_HEIGHT or snake_1_head_y < 0:
            gameOver = True

        if snake_2_head_x >= DISPLAY_WIDTH or snake_2_head_x < 0 or snake_2_head_y >= DISPLAY_HEIGHT or snake_2_head_y < 0:
            gameOver = True

        # store the position of the front of the snake in an empty list
        snake_1_head = []
        snake_1_head.append(snake_1_head_x)
        snake_1_head.append(snake_1_head_y)

        snake_2_head = []
        snake_2_head.append(snake_2_head_x)
        snake_2_head.append(snake_2_head_y)
        # add the position of the front of the snake to the list that holds all elements
        # of our snake
        snakelist1.append(snake_1_head)
        snakelist2.append(snake_2_head)

        # if the size of the snake list is bigger then the length the snake is supposed to be,
        # delete the 'end' of the snake
        if len(snakelist1) > snake_1_length:
            del snakelist1[0]

        if len(snakelist2) > snake_2_length:
            del snakelist2[0]

        # check if snake collides with itself
        for eachSegment in snakelist1[:-1]:
            if eachSegment == snake_1_head:
                gameOver = True

        for eachSegment in snakelist2[:-1]:
            if eachSegment == snake_2_head:
                
                gameOver = True

        if randAppleX < snake_1_head_x < randAppleX + appleThickness or snake_1_head_x + BLOCK_SIZE > randAppleX and snake_1_head_x + BLOCK_SIZE < randAppleX + appleThickness:
            if randAppleY < snake_1_head_y < randAppleY + appleThickness or snake_1_head_y + BLOCK_SIZE > randAppleY and snake_1_head_y + BLOCK_SIZE < randAppleY + appleThickness:
                randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                snake_1_length += 1
                score += 1
        if randAppleX < snake_2_head_x < randAppleX + appleThickness or snake_2_head_x + BLOCK_SIZE > randAppleX and snake_2_head_x + BLOCK_SIZE < randAppleX + appleThickness:
            if randAppleY < snake_2_head_y < randAppleY + appleThickness or snake_2_head_y + BLOCK_SIZE > randAppleY and snake_2_head_y + BLOCK_SIZE < randAppleY + appleThickness:
                randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                snake_2_length += 1
                score += 1
        pygame.display.update()
        clock.tick(FPS)
        winner= "Tie Game"
        winnerScore = 0
        if snake_2_length > snake_1_length:
            winner = "Blue Snake Win"
            winnerScore = snake_2_length
        elif snake_1_length > snake_2_length:
            winner = "Green Snake Win"
            winnerScore = snake_1_length
        else:
            winnerScore = snake_1_length
            
    if tkinter.messagebox.askyesno(title=winner , message= ("Score is "+ str(winnerScore)+"\nDo You Want to Replay")):
        pygame.init()
        gameDisplay = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Snake")
        gameLoop(False, gameDisplay)
    else:
        pygame.quit()
    return score


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

