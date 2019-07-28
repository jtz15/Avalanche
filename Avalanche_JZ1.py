import pygame
import time
from GameBoard_JZ1 import gameBoardHeight
from GameBoard_JZ1 import Gameboard
from Shape_JZ1 import Shape

# import a library of functions called pygame
from copy import deepcopy

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)


def keyCheck():
    #keys = event.key.get_pressed()

        if twoPlayer == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if gameBoard1.pause == False:
                        gameBoard1.pause = True
                    else:
                        gameBoard1.pause = False
                if event.key == pygame.K_a:
                    shape1.moveLeft()
                elif event.key == pygame.K_d:
                    shape1.moveRight()
                elif event.key == pygame.K_s:
                    shape1.rotateCCW()
                elif event.key == pygame.K_w:
                    shape1.rotateCW()
                elif event.key == pygame.K_SPACE:
                    gameBoard1.score += gameBoardHeight - shape1.blockList[0].gridYpos
                    shape1.drop()
                elif event.key == pygame.K_EQUALS and gameBoard1.numSlowTime > 0:
                    gameBoard1.numSlowTime -= 1
                    gameBoard1.slowTimeOn = True
                elif event.key == pygame.K_MINUS and gameBoard1.numSwap > 0:
                    gameBoard1.numSwap -= 1
                    gameBoard1.swapOn = True

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if gameBoard1.pause == False or gameBoard2.pause == False:
                        gameBoard1.pause = True
                        gameBoard2.pause = True
                    else:
                        gameBoard1.pause = False
                        gameBoard2.pause = False
                if event.key == pygame.K_a:
                    shape1.moveLeft()
                elif event.key == pygame.K_d:
                    shape1.moveRight()
                elif event.key == pygame.K_s:
                    shape1.rotateCCW()
                elif event.key == pygame.K_w:
                    shape1.rotateCW()
                elif event.key == pygame.K_SPACE:
                    gameBoard1.score += gameBoardHeight - shape1.blockList[0].gridYpos
                    shape1.drop()
                elif event.key == pygame.K_EQUALS and gameBoard1.numSlowTime > 0:
                    gameBoard1.numSlowTime -= 1
                    gameBoard1.slowTimeOn = True
                elif event.key == pygame.K_MINUS and gameBoard1.numSwap > 0:
                    gameBoard1.numSwap -= 1
                    gameBoard1.swapOn = True
                elif event.key == pygame.K_LEFT:
                    shape2.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    shape2.moveRight()
                elif event.key == pygame.K_DOWN:
                    shape2.rotateCCW()
                elif event.key == pygame.K_UP:
                    shape2.rotateCW()
                elif event.key == pygame.K_RETURN:
                    gameBoard2.score += gameBoardHeight - shape2.blockList[0].gridYpos
                    shape2.drop()
                elif event.key == pygame.K_j and gameBoard2.numSlowTime > 0:
                    gameBoard2.numSlowTime -= 1
                    gameBoard2.slowTimeOn = True
                elif event.key == pygame.K_k and gameBoard2.numSwap > 0:
                    gameBoard2.numSwap -= 1
                    gameBoard2.swapOn = True


def checkHS(score, name):
    indexToInsert = -1

    for i in range(4,-1,-1):
        if score > int(scoreList[i]):
            indexToInsert = i

    if indexToInsert >= 0:
        tempList = deepcopy(scoreList)
        tempList1 = deepcopy(nameList)
        tempList[indexToInsert] = score
        tempList1[indexToInsert] = name

        for i in range (indexToInsert + 1, 4, 1):
            tempList[i] = scoreList[i - 1]
            tempList1[i] = nameList[i - 1]
        for i in range (5):
            scoreList[i] = tempList[i]
            nameList [i] = tempList1[i]



    HSfile = open("Highscore.txt", "w")
    for i in range(5):
        HSfile.write(nameList[i] + '\n')

    for i in range (5):
        HSfile.write(str(scoreList[i]) + '\n')

    HSfile.close()

def drawFunction():
    screen.fill(BLACK)

    gameBoard1.draw(screen)
    shape1.draw(screen)
    nextShape1.drawNextShape(screen, 300, 115)

    stx1 = 310
    sty1 = 360
    scoreText = myFont.render("Score: " + str(gameBoard1.score), 1, WHITE)
    screen.blit(scoreText, (stx1, sty1))

    ltx1 = 310
    lty1 = 460
    linesText = myFont.render("Lines: " + str(gameBoard1.numLines), 1, WHITE)
    screen.blit(linesText, (ltx1, lty1))

    lvx1 = 310
    lvy1 = 260
    levelText = myFont.render("Level: " + str(gameBoard1.level), 1, WHITE)
    screen.blit(levelText, (lvx1, lvy1))

    nsx1 = 360
    nsy1 = 50
    nextShapeText = myFont.render("Next: ", 1, WHITE)
    screen.blit(nextShapeText, (nsx1, nsy1))

    #square around next shape
    sqx1 = 340
    sqy1 = 40
    pygame.draw.rect(screen, WHITE, [sqx1, sqy1, 185, 200 ], 1)

    pux1 = 10
    puy1 = 530
    powerUpsText = myFont.render("Power Ups: ", 1, WHITE)
    screen.blit(powerUpsText, (pux1, puy1))

    nstx1 = 200
    nsty1 = 530
    numSlowTimeText = myFont.render("x " + str(gameBoard1.numSlowTime), 1, WHITE)
    screen.blit(numSlowTimeText, (nstx1, nsty1))

    stix1 = 250
    stiy1 = 520
    slowTimeimage = pygame.image.load("Clock.png")
    screen.blit(slowTimeimage, (stix1, stiy1))

    nswx1= 200
    nswy1= 620
    numSwapText = myFont.render("x" + str(gameBoard1.numSwap), 1, WHITE)
    screen.blit(numSwapText, (nswx1, nswy1))

    six1 = 250
    siy1 = 610
    swapImage = pygame.image.load("Swap.png")
    screen.blit(swapImage, (six1, siy1))

    highScoreText = myFont.render("High Score:", 1, WHITE)
    screen.blit(highScoreText, (545, 50))

    pygame.draw.rect(screen, WHITE, (525, 40, 200, 200), 1) # box around highscore

    nameText = myFont.render("Name: " + str(player1Name), 1, WHITE)
    screen.blit(nameText, (310, 0))
    for i in range(5):
        hsScoreText = hsFont.render(str(scoreList[i]), 1, WHITE)
        screen.blit(hsScoreText, (650, i * 25 + 100))
        hsNameText = hsFont.render(str(nameList[i]), 1, WHITE)
        screen.blit(hsNameText, (540, i * 25 + 100))

    if twoPlayer == True:
        gameBoard2.draw(screen)
        shape2.draw(screen)
        nextShape2.drawNextShape(screen, -300, 115)
        pygame.draw.line(screen, WHITE, (625, 0), (625, 40))  # drawing first part of line to the top of highscore box
        pygame.draw.line(screen, WHITE, (625, 240), (625, 700))  # drawing second part of the line from the bottom of highscore box to bottom of screen

        scoreText = myFont.render("Score: " + str(gameBoard2.score), 1, WHITE)
        screen.blit(scoreText, (stx1 + 325, sty1))

        linesText = myFont.render("Lines: " + str(gameBoard2.numLines), 1, WHITE)
        screen.blit(linesText, (ltx1 + 325, lty1))

        levelText = myFont.render("Level: " + str(gameBoard2.level), 1, WHITE)
        screen.blit(levelText, (lvx1 + 325, lvy1))

        nextShapeText = myFont.render("Next: ", 1, WHITE)
        screen.blit(nextShapeText, (nsx1 + 375, nsy1))

        # square around next shape
        pygame.draw.rect(screen, WHITE, [sqx1 + 385, sqy1, 190, 200], 1)

        powerUpsText = myFont.render("Power Ups: ", 1, WHITE)
        screen.blit(powerUpsText, (pux1 + 625, puy1))

        numSlowTimeText = myFont.render("x " + str(gameBoard2.numSlowTime), 1, WHITE)
        screen.blit(numSlowTimeText, (nstx1 + 625, nsty1))

        slowTimeimage = pygame.image.load("Clock.png")
        screen.blit(slowTimeimage, (stix1 + 625, stiy1))

        numSwapText = myFont.render("x" + str(gameBoard2.numSwap), 1, WHITE)
        screen.blit(numSwapText, (nswx1 + 625, nswy1))

        swapImage = pygame.image.load("Swap.png")
        screen.blit(swapImage, (six1 + 625, siy1))

        nameText = myFont.render("Name: " + str(player2Name), 1, WHITE)
        screen.blit(nameText, (635, 0))

        for i in range(5):
            hsNameText = hsFont.render(str(nameList[i]), 1, WHITE)
            screen.blit(hsNameText, (540, i * 25 + 100))
            hsScoreText = hsFont.render(str(scoreList[i]), 1, WHITE)
            screen.blit(hsScoreText, (650, i * 25 + 100))

    pygame.display.flip()


    #checkHS()

def checkPlayerNumber(): #returns false if user quit, returns true if user selected an option
    shift = 0
    playerSelected = False
    global twoPlayer
    while not playerSelected:
        backDropImage = pygame.image.load("Backdrop.png")

        screen.blit(backDropImage, (0, 0))

        pygame.draw.polygon(screen, YELLOW, [[300, 200 + shift], [300, 220 + shift], [328, 210 + shift], 1])
        onePlayerText = myFont.render("1 Player", 1, WHITE)
        screen.blit(onePlayerText, (330, 200))
        twoPlayerText = myFont.render("2 Player", 1, WHITE)
        screen.blit(twoPlayerText, (330, 250))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                twoPlayer = not twoPlayer
                if twoPlayer == True:
                    shift = +50
                else:
                    shift = 0

def inputPlayerName(playerText):
    global name
    global exit
    name = ""

    while (not exit):
        backDropImage = pygame.image.load("Backdrop.png")

        screen.blit(backDropImage, (0, 0))

        enterNameText = myFont.render(str(playerText) + " Name: " + str(name), 1, WHITE)
        screen.blit(enterNameText, (200, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key >= 33 and event.key <= 126 and len(name) <= 10:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
                        name += chr(event.key).upper()
                    else:
                        name += chr(event.key)
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                if event.key == pygame.K_RETURN:
                    if name == "":
                        name = playerText
                    return name

#START OF CODE

delay = 0
timer= 0
timeLeft = 7000
start = False
exit = False
twoPlayer = False
player1Name = ""
player2Name = ""
grid1x = 0
grid1y = 0
grid2x = 0
grid2y= 0

if __name__ == "__main__":
    pygame.init()
    size = (800, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Avalanche by Jenita")


    myFont = pygame.font.Font('freesansbold.ttf', 30)
    hsFont = pygame.font.Font('freesansbold.ttf', 20)
    nameList = [0 for y in range(5)]
    scoreList = [0 for y in range(5)]
    hsFile = open("HighScore.txt", "r")
    for i in range(5):
        nameList[i] = hsFile.readline().rstrip('\n')
    for i in range(5):
        scoreList[i] = hsFile.readline().rstrip('\n')
    hsFile.close()

    slowTimeDelay = 0

    pygame.mixer.init()
    pygame.mixer.music.load('AvalancheBGM.mp3')
    pygame.mixer.music.play(-1)

    if( checkPlayerNumber() == False):
        exit = True
    else:
        exit = False


    if twoPlayer == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        player1Name = inputPlayerName("Player 1")

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        player1Name = inputPlayerName("Player 1")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        player2Name = inputPlayerName("Player 2")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

    playerReading = True

    while (playerReading):

        screen.fill(BLACK)
        gameInstructionText = myFont.render("Instructions", 1, WHITE)
        screen.blit(gameInstructionText, (350, 10))

        objectiveText = myFont.render("Objective:", 1, WHITE)
        screen.blit(objectiveText, (0, 60))

        objectiveExplanationPart1 = myFont.render("Clear rows by completing a row of blocks as quickly as", 1, WHITE)
        screen.blit(objectiveExplanationPart1, (0, 110))

        objectiveExplanationPart2 = myFont.render("possible to achieve the highest score.", 1, WHITE)
        screen.blit(objectiveExplanationPart2, (0, 160))

        gameOverText = myFont.render("Game Over:", 1, WHITE)
        screen.blit(gameOverText, (0, 260))

        gameOverExplanation = myFont.render("When the shapes reach the top gameboard, YOU DIE!", 1, WHITE)
        screen.blit(gameOverExplanation, (0, 310))

        powerUpText = myFont.render("Power Ups:", 1, WHITE)
        screen.blit(powerUpText, (0, 410))

        powerUpExplainTextPart1 = myFont.render("You have two power ups which you gain when", 1, WHITE)
        screen.blit(powerUpExplainTextPart1, (0, 460))

        powerUpExplainTextPart2 = myFont.render("you clear 5 lines.", 1, WHITE)
        screen.blit(powerUpExplainTextPart2,(0, 510))

        continueText = myFont.render("Press ENTER to begin...", 1, WHITE)
        screen.blit(continueText, (300, 600))


        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    playerReading = False
            if event.type == pygame.QUIT:
                exit = True
                playerReading = False

    gameBoard1 = Gameboard(WHITE, 25, grid1x, grid1y)
    shape1 = Shape(grid1x, grid1y, gameBoard1.activeBoardSpot, gameBoard1.activeBoardColor)
    nextShape1 = Shape(grid1x, grid1y, gameBoard1.activeBoardSpot, gameBoard1.activeBoardColor)

    if twoPlayer == True:
        size = (1250, 700)
        screen = pygame.display.set_mode(size)

        grid2x = 38
        grid2y = 0

        gameBoard2 = Gameboard(WHITE, 25, grid2x, grid2y)
        shape2 = Shape(grid2x, grid2y, gameBoard2.activeBoardSpot, gameBoard2.activeBoardColor)
        nextShape2 = Shape(grid2x, grid2y, gameBoard2.activeBoardSpot, gameBoard2.activeBoardColor)

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                keyCheck()

        delay += 1
        timer += 1
        if timer >= 10:
            timer = 0
            timeLeft -= 1
        if twoPlayer == False:
            if timeLeft <= 0:
                gameBoard1.pause = True
            if delay >= 10 and gameBoard1.pause == False:
                shape1.falling()
        else:
            if timeLeft <= 0:
                gameBoard1.pause = True
                gameBoard2.pause = True

            if delay >= 10 and gameBoard1.pause == False and gameBoard2.pause == False:
                shape1.falling()
                shape2.falling()
                delay = 0

        if twoPlayer == False and gameBoard1.checkLoss() == True:
            gameOver = True
            while (gameOver):
                xStartPos = 150
                yStartPos = 140
                Length = 500
                Width = 350

                pygame.draw.rect(screen, YELLOW, [xStartPos - 20, yStartPos - 20, Length + 40, Width + 40], 0)

                pygame.draw.rect(screen, BLACK, [xStartPos, yStartPos, Length, Width], 0)

                gameOverText = myFont.render("GAME OVER!", 1, WHITE)
                screen.blit(gameOverText, (307, 150))

                winnerText = myFont.render("WINNER: " + str(player1Name), 1, WHITE)
                screen.blit(winnerText, (180, 220))

                p1scoreDisplay = myFont.render(str(player1Name) + "'s Score: " + str(gameBoard1.score), 1, WHITE)
                screen.blit(p1scoreDisplay, (180, 290))

                playAgainText = myFont.render("Press ENTER to Play Again", 1, WHITE)
                screen.blit(playAgainText, (202, 405))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameOver = False

            checkHS(gameBoard1.score, player1Name)
            gameBoard1 = Gameboard(WHITE, shape1.blockList[0].size, grid1x, grid1y)
            shape1 = Shape(grid1x, grid1y, gameBoard1.activeBoardSpot, gameBoard1.activeBoardColor)
            slowTimeDelay = 0
            delay = 0

        delay +=1

        if twoPlayer == True and gameBoard1.checkLoss() == True:
                gameOver1 = True
                while (gameOver1):
                    xStartPos = 377
                    yStartPos = 140
                    Length = 500
                    Width = 350

                    pygame.draw.rect(screen, YELLOW, [xStartPos - 20, yStartPos - 20, Length + 40, Width + 40], 0)

                    pygame.draw.rect(screen, BLACK, [xStartPos, yStartPos, Length, Width], 0)

                    gameOverText = myFont.render("GAME OVER!", 1, WHITE)
                    screen.blit(gameOverText, (525, 150))

                    winnerText = myFont.render("WINNER: " + str(player2Name), 1, WHITE)
                    screen.blit(winnerText, (525, 220))

                    p1scoreDisplay = myFont.render(str(player1Name) + "'s Score: " + str(gameBoard1.score), 1, WHITE)
                    screen.blit(p1scoreDisplay, (407, 290))

                    p2scoreDisplay = myFont.render(str(player2Name) + "'s Score: " + str(gameBoard2.score), 1, WHITE)
                    screen.blit(p2scoreDisplay, (407, 325))

                    playAgainText = myFont.render("Press ENTER to Play Again", 1, WHITE)
                    screen.blit(playAgainText, (426, 405))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit = True
                            gameOver1 = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                gameOver1 = False

                checkHS(gameBoard1.score, player1Name)
                gameBoard1= Gameboard(WHITE, shape1.blockList[0].size, grid1x, grid1y)
                shape1 = Shape(grid1x, grid1y, gameBoard1.activeBoardSpot, gameBoard1.activeBoardColor)
                slowTimeDelay = 0
                delay = 0

                checkHS(gameBoard2.score, player2Name)
                gameBoard2 = Gameboard(WHITE, shape1.blockList[0].size, grid2x, grid2y)
                shape2 = Shape(grid2x, grid2y, gameBoard2.activeBoardSpot, gameBoard2.activeBoardColor)

        delay += 1

        if twoPlayer == True and gameBoard2.checkLoss() == True:
            gameOver2 = True
            while (gameOver2):
                xStartPos = 377
                yStartPos = 140
                Length = 500
                Width = 350

                pygame.draw.rect(screen, YELLOW, [xStartPos - 20, yStartPos - 20, Length + 40, Width + 40], 0)

                pygame.draw.rect(screen, BLACK, [xStartPos, yStartPos, Length, Width], 0)

                gameOverText = myFont.render("GAME OVER!", 1, WHITE)
                screen.blit(gameOverText, (525, 150))

                winnerText = myFont.render("WINNER: " + str(player1Name), 1, WHITE)
                screen.blit(winnerText, (525, 220))

                p1scoreDisplay = myFont.render(str(player1Name) + " Score: " + str(gameBoard1.score), 1, WHITE)
                screen.blit(p1scoreDisplay, (407, 290))

                p2scoreDisplay = myFont.render(str(player2Name) + " Score: " + str(gameBoard2.score), 1, WHITE)
                screen.blit(p2scoreDisplay, (407, 325))

                playAgainText = myFont.render("Press ENTER to Play Again", 1, WHITE)
                screen.blit(playAgainText, (426, 405))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit = True
                        gameOver2 = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameOver2 = False

            checkHS(gameBoard1.score, player1Name)
            gameBoard1 = Gameboard(WHITE, shape1.blockList[0].size, grid1x, grid1y)
            shape1 = Shape(grid1x, grid1y, gameBoard1.activeBoardSpot, gameBoard1.activeBoardColor)
            slowTimeDelay = 0
            delay = 0

            checkHS(gameBoard2.score, player2Name)
            gameBoard2 = Gameboard(WHITE, shape1.blockList[0].size, grid2x, grid2y)
            shape2 = Shape(grid2x, grid2y, gameBoard2.activeBoardSpot, gameBoard2.activeBoardColor)

        delay += 1

        if shape1.active == False:
            gameBoard1.clearFullRow()
            shape1 = nextShape1
            nextShape1 = Shape(grid1x, grid1y, gameBoard1.activeBoardSpot, gameBoard1.activeBoardColor)
        if twoPlayer == True and shape2.active == False:
            gameBoard2.clearFullRow()
            shape2 = nextShape2
            nextShape2 = Shape(grid2x, grid2y, gameBoard2.activeBoardSpot, gameBoard2.activeBoardColor)

        if gameBoard1.slowTimeOn == True:
            slowTimeDelay += 1
            if slowTimeDelay > 50:
                gameBoard1.slowTimeOn = False
                slowTimeDelay = 0

        if twoPlayer == True and gameBoard2.slowTimeOn == True:
            slowTimeDelay += 1
            if slowTimeDelay > 50:
                gameBoard2.slowTimeOn = False
                slowTimeDelay = 0

        if gameBoard1.swapOn == True:
            shape1 = nextShape1
            nextShape1 = Shape(grid1x, grid1y, gameBoard1.activeBoardSpot, gameBoard1.activeBoardColor)
            gameBoard1.swapOn = False

        if twoPlayer == True and gameBoard2.swapOn == True:
            shape2 = nextShape2
            nextShape2 = Shape(grid2x, grid2y, gameBoard2.activeBoardSpot, gameBoard2.activeBoardColor)
            gameBoard2.swapOn = False

        drawFunction()

        if (0.11 - gameBoard1.level * 0.01 >= 0):
            time.sleep(0.11 - gameBoard1.level * 0.01 + gameBoard1.slowTimeOn * 0.1)









