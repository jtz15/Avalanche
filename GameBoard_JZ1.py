import pygame


gameBoardWidth = 12
gameBoardHeight = 20

BLACK = (0,0,0)
WHITE = (255, 255, 255)
pygame.init()
lineSound = pygame.mixer.Sound("clearline.wav")

class Gameboard():
    def __init__(self, color, blockSize, x,y):
        self.borderColor = color
        self.multiplier = blockSize
        self.score = 0
        self.numLines = 0
        self.level = 1
        self.lineTracker = 0
        self.numSlowTime = 0
        self.numSwap = 0
        self.swapOn = False
        self.slowTimeOn = False
        self.x = x
        self.y = y
        self.pause = False
        self.activeBoardSpot = [[0 for y in range(gameBoardHeight)] for x in range(gameBoardWidth)]
        self.activeBoardColor = [[0 for y in range(gameBoardHeight)] for x in range(gameBoardWidth)]
        for i in range(gameBoardWidth-1):
            for j in range(gameBoardHeight-1):
                self.activeBoardSpot[i][j] = False
                self.activeBoardColor[i][j] = (0, 0, 0)


    def draw(self,screen):
        pygame.draw.rect( screen, self.borderColor, [self.x * self.multiplier, self.y * self.multiplier, self.multiplier * gameBoardWidth, self.multiplier * gameBoardHeight], 1)
        # code for drawing vertical lines
        for i in range (gameBoardWidth):
            pygame.draw.line(screen,WHITE,[self.multiplier * i-1 + self.x * self.multiplier, self.y * self.multiplier],[self.multiplier * i-1 + self.x * self.multiplier, gameBoardHeight * self.multiplier + self.y * self.multiplier], 1)
        # code for drawing horizontal lines
        for i in range(gameBoardHeight):
            pygame.draw.line(screen, WHITE, [self.x * self.multiplier, self.multiplier * i - 1 + self.y * self.multiplier],[gameBoardWidth * self.multiplier + self.x * self.multiplier, self.multiplier * i - 1 + self.y * self.multiplier],1)
        for i in range(gameBoardWidth):
            for j in range(gameBoardHeight):
                if self.activeBoardSpot[i][j] == True:
                    pygame.draw.rect(screen, self.activeBoardColor[i][j], [i * self.multiplier + self.x * self.multiplier, j * self.multiplier + self.y * self.multiplier, self.multiplier -1 , self.multiplier -1], 0)


    def checkLoss(self):
        for i in range (gameBoardWidth):
            if self.activeBoardSpot[i][0] == True:
                return True

        return False

    def isCompleteLine(self, rownum):
        for i in range (gameBoardWidth):
            if self.activeBoardSpot[i][rownum] == False:
                return False

        return True

    def clearFullRow(self):
        for i in range(gameBoardHeight):
            if self.isCompleteLine(i) == True:
                for c in range(i,1,-1):
                    for j in range (gameBoardWidth):
                        self.activeBoardColor[j][c] = self.activeBoardColor[j][c - 1]
                        self.activeBoardSpot[j][c] = self.activeBoardSpot[j][c - 1]
                self.score += 50
                for k in range (gameBoardWidth):
                    self.activeBoardColor[k][0] = BLACK
                    self.activeBoardSpot[k][0] = False
                self.numLines += 1
                self.lineTracker += 1
                if self.lineTracker == 5:
                    self.level += 1
                    self.numSlowTime += 1
                    self.numSwap += 1
                    self.lineTracker = 0
                lineSound.play()





