import time, random
import pygame

BLOCK_SIZE = 20
FPS = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 0)

clock = pygame.time.Clock()

def gameLoop(gamerunvalue, gameDisplay):
    gameOver = gamerunvalue

    lead_x = DISPLAY_WIDTH / 2  # x and y locations for the head of the snake
    lead_y = DISPLAY_HEIGHT / 2
    lead_dx = BLOCK_SIZE
    lead_dy = 0
    direction = 'right'
    randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    snakeList = []
    snakeLength = 1
    score = 1

    while gameOver is not True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction is not 'right':
                    lead_dx = -BLOCK_SIZE
                    lead_dy = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction is not 'left':
                    lead_dx = BLOCK_SIZE
                    lead_dy = 0
                    direction = 'right'
                elif event.key == pygame.K_UP and direction is not 'down':
                    lead_dy = -BLOCK_SIZE
                    lead_dx = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction is not 'up':
                    lead_dy = BLOCK_SIZE
                    lead_dx = 0
                    direction = 'down'

        lead_x += lead_dx
        lead_y += lead_dy

        if lead_x >= DISPLAY_WIDTH or lead_x < 0 or lead_y >= DISPLAY_HEIGHT or lead_y < 0:
            gameOver = True

        gameDisplay.fill(WHITE)

        appleThickness = 30
        pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, appleThickness, appleThickness])

        # store the position of the front of the snake in an empty list
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        # add the position of the front of the snake to the list that holds all elements
        # of our snake
        snakeList.append(snakeHead)

        # if the size of the snake list is bigger then the length the snake is supposed to be,
        # delete the 'end' of the snake
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # check if snake collides with itself
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        for xy in snakeList:
            pygame.draw.rect(gameDisplay, GREEN, [xy[0], xy[1], BLOCK_SIZE, BLOCK_SIZE])


        pygame.display.update()
        if randAppleX < lead_x < randAppleX + appleThickness or lead_x + BLOCK_SIZE > randAppleX and lead_x + BLOCK_SIZE < randAppleX + appleThickness:
            if randAppleY < lead_y < randAppleY + appleThickness or lead_y + BLOCK_SIZE > randAppleY and lead_y + BLOCK_SIZE < randAppleY + appleThickness:
                randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                snakeLength += 1
                score += 1

        clock.tick(FPS)
    return score



DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Slither")
gameLoop(False, gameDisplay)
