import time, random
import pygame
import tkinter 
import tkinter.messagebox
import pickle
import os 
# DEFAULT VALUES
BLOCK_SIZE = 20
FPS = 15
DIFF = "easy"
# COLOURS
BACKGROUND = (255, 255, 255)
BLACK = (0, 0, 0)
APPLE = (255, 0, 0)
SNAKE1 = (0, 155, 0)
PURPLE = (138,43,226)
SILVER = (192,192,192)
GOLD = (255,255,0)
# CLOCK
clock = pygame.time.Clock()

# DISPLAY DIMENSIONS
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# POWERUPS ARRAY
POWERUPS = ["normal"]

def add_powerup(powerup: str):
    """
    Add a powerup to the game
    :param powerup:
    :return:
    """
    global POWERUPS
    POWERUPS.append(powerup)


def remove_powerup(powerup: str):
    """
    Remove a powerup from the game
    :param powerup:
    :return:
    """
    global POWERUPS
    POWERUPS.remove(powerup)


def doPowerup(powerup: str, snakeLen):
    if powerup is "normal":
        return snakeLen + 1
    elif powerup is "bad":
        return snakeLen - 1
    elif powerup is "slice":
        return snakeLen//2
    elif powerup is "golden":
        return snakeLen+2
    elif powerup is "double":
        return snakeLen + 1


def singleplayer(difficulty: str):
    """
    Initializes the gameLoop with the necessary parameters as well as sets the
    difficulty
    :param difficulty:
    :return:
    """
    global FPS
    global DIFF
    DIFF = difficulty
    if difficulty == "easy":
        FPS = 15
    elif difficulty == "medium":
        FPS = 25
    elif difficulty == "hard":
        FPS = 40
    elif difficulty == "nightmare": # difficulty is nightmare
        FPS = 60

    pygame.init()
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Slither")
    gameLoop(False, gameDisplay)


def gameLoop(gamerunvalue: bool, gameDisplay) -> int:
    """
    Runs the gameloop to display the game
    :param gamerunvalue:
    :param gameDisplay:
    :return: exit status 0 on quit or score on gameover
    """
    global POWERUPS
    gameOver = gamerunvalue

    lead_x = DISPLAY_WIDTH / 2  # x and y locations for the head of the snake
    lead_y = DISPLAY_HEIGHT / 2
    lead_dx = BLOCK_SIZE
    lead_dy = 0
    direction = 'right'

    snakeList = []
    snakeLength = 1
    score = 1

    # Apple coordinates
    randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    randDoubleAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    randDoubleAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    
    # Store current powerup
    current_powerup = None

    # Keep track of powers with nultiple apples on screen
    apple = False
    apple2 = False

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

        if lead_x >= DISPLAY_WIDTH or lead_x < 0 or lead_y >= DISPLAY_HEIGHT or\
                lead_y < 0:
            gameOver = True

        gameDisplay.fill(BACKGROUND)

        # POWERUP SPAWN IN --------------------------------------------------------------
        if current_powerup is None:
            random_powerup = POWERUPS[random.randint(0, len(POWERUPS)-1)]
            if random_powerup == "normal":
                current_powerup = "normal"
                appleThickness = 30
                pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY,
                                                    appleThickness, appleThickness])
            elif random_powerup == "bad":
                current_powerup = "bad"
                appleThickness = 30
                pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY,
                                                    appleThickness, appleThickness])
                pygame.draw.rect(gameDisplay, PURPLE, [randDoubleAppleX, randDoubleAppleY,
                                                    appleThickness, appleThickness])
            elif random_powerup == "slice":
                current_powerup = "slice"
                appleThickness = 30
                pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY,
                                                    appleThickness, appleThickness])
                pygame.draw.rect(gameDisplay, SILVER, [randDoubleAppleX, randDoubleAppleY,
                                                    appleThickness, appleThickness])
            elif random_powerup == "golden":
                current_powerup = "golden"
                appleThickness = 30
                pygame.draw.rect(gameDisplay, GOLD, [randAppleX, randAppleY,
                                                    appleThickness, appleThickness])
            elif random_powerup == "double":
                current_powerup = "double"
                appleThickness = 30
                pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY,
                                                    appleThickness, appleThickness])
                pygame.draw.rect(gameDisplay, APPLE, [randDoubleAppleX, randDoubleAppleY,
                                                    appleThickness, appleThickness])

        # POWERUP CONTINUALLY DISPLAY --------------------------------------------------
        if current_powerup == "normal":
            appleThickness = 30
            pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY,
                                                appleThickness, appleThickness])
        elif current_powerup == "bad":
            appleThickness = 30
            # If apple still on board
            if not apple:
                pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY,
                                                    appleThickness, appleThickness])
            # If apple2 still on board
            if not apple2:
                pygame.draw.rect(gameDisplay, PURPLE, [randDoubleAppleX, randDoubleAppleY,
                                                    appleThickness, appleThickness])
        elif current_powerup == "slice":
            appleThickness = 30
            # If apple still on board
            if not apple:
                pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY,
                                                    appleThickness, appleThickness])
            # If apple2 still on board
            if not apple2:
                pygame.draw.rect(gameDisplay, SILVER, [randDoubleAppleX, randDoubleAppleY,
                                                    appleThickness, appleThickness])
        elif current_powerup == "golden":
            appleThickness = 30
            pygame.draw.rect(gameDisplay, GOLD, [randAppleX, randAppleY,
                                                appleThickness, appleThickness])
        elif current_powerup == "double":
                appleThickness = 30
                # If apple still on board
                if not apple:
                    pygame.draw.rect(gameDisplay, APPLE, [randAppleX, randAppleY,
                                                        appleThickness, appleThickness])
                # If apple2 still on board
                if not apple2:
                    pygame.draw.rect(gameDisplay, APPLE, [randDoubleAppleX, randDoubleAppleY,
                                                        appleThickness, appleThickness])

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
            while len(snakeList) > snakeLength:
                del snakeList[0]

        # check if snake collides with itself
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        for xy in snakeList:
            pygame.draw.rect(gameDisplay, SNAKE1, [xy[0], xy[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        # Handling when snake eats an apple
        # Double powerup
        if current_powerup is "double":
            # First apple
            if randAppleX < lead_x < randAppleX + appleThickness or lead_x + BLOCK_SIZE > randAppleX and lead_x + BLOCK_SIZE < randAppleX + appleThickness:
                if randAppleY < lead_y < randAppleY + appleThickness or lead_y + BLOCK_SIZE > randAppleY and lead_y + BLOCK_SIZE < randAppleY + appleThickness:
                    randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                    randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                    snakeLength = doPowerup(current_powerup, snakeLength)
                    apple = True

            # Second apple
            if randDoubleAppleX < lead_x < randDoubleAppleX + appleThickness or lead_x + BLOCK_SIZE > randDoubleAppleX and lead_x + BLOCK_SIZE < randDoubleAppleX + appleThickness:
                if randDoubleAppleY < lead_y < randDoubleAppleY + appleThickness or lead_y + BLOCK_SIZE > randDoubleAppleY and lead_y + BLOCK_SIZE < randDoubleAppleY + appleThickness:
                    randDoubleAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                    randDoubleAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                    snakeLength = doPowerup(current_powerup, snakeLength)
                    apple2 = True

            # Reset once both are eaten      
            if apple and apple2:
                apple = False
                apple2 = False
                current_powerup = None
                score = snakeLength

        # Power downs
        elif current_powerup is "bad" or current_powerup is "slice":
            # If snake eats the red one
            if randAppleX < lead_x < randAppleX + appleThickness or lead_x + BLOCK_SIZE > randAppleX and lead_x + BLOCK_SIZE < randAppleX + appleThickness:
                if randAppleY < lead_y < randAppleY + appleThickness or lead_y + BLOCK_SIZE > randAppleY and lead_y + BLOCK_SIZE < randAppleY + appleThickness:
                    randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                    randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                    snakeLength = doPowerup("normal", snakeLength)
                    apple = True

            # If snake eats the power down     
            if randDoubleAppleX < lead_x < randDoubleAppleX + appleThickness or lead_x + BLOCK_SIZE > randDoubleAppleX and lead_x + BLOCK_SIZE < randDoubleAppleX + appleThickness:
                if randDoubleAppleY < lead_y < randDoubleAppleY + appleThickness or lead_y + BLOCK_SIZE > randDoubleAppleY and lead_y + BLOCK_SIZE < randDoubleAppleY + appleThickness:
                    randDoubleAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                    randDoubleAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                    snakeLength = doPowerup(current_powerup, snakeLength)
                    apple2 = True
                    if snakeLength == 0:
                        gameOver = True

            # If either one is eaten, reset   
            if apple or apple2:
                # If apple was the one eaten, reset apple2
                if apple :
                    randDoubleAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                    randDoubleAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                # If apple2 was the one eaten, reset apple
                if apple2:
                    randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                    randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                    
                current_powerup = None
                apple = False
                apple2 = False
                
        # Any other powerups
        else:
            # If apple eaten
            if randAppleX < lead_x < randAppleX + appleThickness or lead_x + BLOCK_SIZE > randAppleX and lead_x + BLOCK_SIZE < randAppleX + appleThickness:
                if randAppleY < lead_y < randAppleY + appleThickness or lead_y + BLOCK_SIZE > randAppleY and lead_y + BLOCK_SIZE < randAppleY + appleThickness:
                    randAppleX = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
                    randAppleY = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
                    snakeLength = doPowerup(current_powerup, snakeLength)
                    if snakeLength == 0:
                        gameOver = True
                    else:
                        current_powerup = None

        clock.tick(FPS)

    ###resets the highscores

    #pickle_out = open("score.pickle", "wb")
    #pickle.dump({"EASY":[0,0,0], "MEDIUM": [0,0,0], "HARD": [0,0,0], "YOU AINT GONNA SURVIVE":[0,0,0]}, pickle_out)
    #pickle_out.close()
    new_hs = False

    # Check if score.p exists already
    if os.path.isfile('score.p'):
        # Load high_scores with existing dict
        with open("score.p", "rb") as f:
            high_scores = pickle.load(f)
            new_hs = False  # checks to see if a highscore has been replaced
            for key in high_scores.keys():
                if DIFF.upper() == key:
                    for value in range(len(high_scores[key])):
                        if snakeLength > high_scores[key][value]:
                            high_scores[key].insert(value, snakeLength)
                            high_scores[key].pop()
                            #high_scores[key][value] = snakeLength
                            place = value
                            new_hs = True
                            break
        with open("score.p", 'wb') as pickle_out:
            pickle.dump(high_scores, pickle_out)
    
    # Score.p doesn't exist
    else:
        # Default with empty dict
        with open("score.p","wb") as out:
            pickle.dump({"EASY":[0,0,0], "MEDIUM": [0,0,0], "HARD": [0,0,0], "NIGHTMARE":[0,0,0]}, out)

   


                
    if new_hs:
        if tkinter.messagebox.askyesno(title="New Highscore", message= ("You Scored " + str(snakeLength) +"\nPlacing you #"+str(place+1)+" on the leaderbords\nDo You Want to Replay?")):
            new_hs = False
            singleplayer(DIFF)
        else:
            pygame.quit()   
    else:    
        if tkinter.messagebox.askyesno(title="You Died", message= ("You Scored " + str(snakeLength) +"\nDo You Want to Replay?")):
            singleplayer(DIFF)
        else:
            pygame.quit()
    
    score = snakeLength
    return score
add_powerup("double")
add_powerup("golden")
add_powerup("slice")
add_powerup("bad")
#singleplayer("easy")

