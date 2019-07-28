from Block_JZ1 import Block
from GameBoard_JZ1 import gameBoardWidth
from GameBoard_JZ1 import gameBoardHeight
import pygame
import random

TSHAPE = [[(gameBoardWidth / 2) - 1, 1], [(gameBoardWidth / 2), 1], [(gameBoardWidth / 2) - 1, 0],
          [(gameBoardWidth / 2) - 2, 1]]

MLSHAPE = [[(gameBoardWidth / 2), 2], [(gameBoardWidth / 2), 0], [(gameBoardWidth / 2), 1],
           [(gameBoardWidth / 2) - 1, 2]]

LSHAPE = [[(gameBoardWidth / 2) - 1, 0], [(gameBoardWidth / 2) - 1, 1], [(gameBoardWidth / 2) - 1, 2],
          [(gameBoardWidth / 2), 2]]

LINESHAPE = [[(gameBoardWidth / 2), 0], [(gameBoardWidth / 2) - 2, 0], [(gameBoardWidth / 2) - 1, 0],
             [(gameBoardWidth / 2) + 1, 0]]

SSHAPE = [[(gameBoardWidth / 2) - 1, 1], [(gameBoardWidth / 2) - 1, 0], [(gameBoardWidth / 2) - 2, 1],
          [(gameBoardWidth / 2), 0]]

SQUARESHAPE = [[(gameBoardWidth / 2), 1], [(gameBoardWidth / 2) - 1, 0], [(gameBoardWidth / 2), 0],
               [(gameBoardWidth / 2) - 1, 1]]

ZSHAPE = [[(gameBoardWidth / 2) - 1, 1], [(gameBoardWidth / 2) - 1, 0], [(gameBoardWidth / 2) - 2, 0],
          [(gameBoardWidth / 2), 1]]

ALLSHAPES = [TSHAPE, MLSHAPE, LSHAPE, LINESHAPE, SSHAPE, SQUARESHAPE, ZSHAPE]

ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)

ALLCOLOURS = [RED, YELLOW, GREEN, TURQUOISE, BLUE, MAGENTA, ORANGE]


class Shape():
    def __init__(self, x, y, activeBoardSpot, activeBoardColor):
        randomNum = random.randrange(7)
        self.shape = ALLSHAPES[randomNum]
        self.numBlocks = 4
        self.color = ALLCOLOURS[randomNum]
        self.blockList = []
        self.active = True
        self.x = x
        self.y = y
        self.activeBoardSpot = activeBoardSpot
        self.activeBoardColor = activeBoardColor
        for i in range(self.numBlocks):
            self.blockList.append(Block(self.color, self.shape[i][0] + self.x, self.shape[i][1] + self.y))

    def draw(self, screen):
        for i in range(self.numBlocks):
            self.blockList[i].draw(screen)

    def moveLeft(self):
        blocked = False
        for i in range(self.numBlocks):
            if self.blockList[i].gridXpos - self.x == 0 or self.activeBoardSpot[self.blockList[i].gridXpos - 1 - self.x][self.blockList[i].gridYpos - self.y] == True:
                blocked = True
        if blocked == False:
            for i in range(self.numBlocks):
                self.blockList[i].gridXpos -= 1

    def moveRight(self):
        blocked = False
        for i in range(self.numBlocks):
            if self.blockList[i].gridXpos - self.x == gameBoardWidth - 1 or self.activeBoardSpot[self.blockList[i].gridXpos + 1\
                    - self.x][self.blockList[i].gridYpos - self.y] == True:
                blocked = True
        if blocked == False:
            for i in range(self.numBlocks):
                self.blockList[i].gridXpos += 1

    def moveDown(self):
        blocked = False
        for i in range(self.numBlocks):
            if self.blockList[i].gridYpos - self.y == gameBoardHeight - 1 or self.activeBoardSpot[self.blockList[i].gridXpos - \
                    self.x][self.blockList[i].gridYpos + 1 - self.y] == True:
                blocked = True
        if blocked == False:
            for i in range(self.numBlocks):
                self.blockList[i].gridYpos += 1

    def rotateCW(self):
        newBlockX = [0, 0, 0, 0]
        newBlockY = [0, 0, 0, 0]
        if (self.shape != SQUARESHAPE):
            canRotate = True

            for i in range(self.numBlocks):
                # transformation operation
                newBlockX[i] = (self.blockList[i].gridYpos - self.y) - (self.blockList[0].gridYpos - self.y) + (self.blockList[0].gridXpos - self.x)
                newBlockY[i] = -(self.blockList[i].gridXpos - self.x) + (self.blockList[0].gridXpos - self.x) + (self.blockList[0].gridYpos - self.y)

                if newBlockX[i] >= gameBoardWidth or newBlockX[i] < 0:
                    canRotate = False
                elif newBlockY[i] >= gameBoardHeight or newBlockY[i] < 0:
                    canRotate = False
                elif self.activeBoardSpot[newBlockX[i]][newBlockY[i]] == True:
                    canRotate = False

            if canRotate == True:
                for i in range(self.numBlocks):
                    self.blockList[i].gridXpos = newBlockX[i] + self.x
                    self.blockList[i].gridYpos = newBlockY[i] + self.y

    def rotateCCW(self):
        newBlockX = [0, 0, 0, 0]
        newBlockY = [0, 0, 0, 0]
        if (self.shape != SQUARESHAPE):
            canRotate = True

            for i in range(self.numBlocks):
                newBlockX[i] = -(self.blockList[i].gridYpos - self.y) + (self.blockList[0].gridYpos - self.y) + (self.blockList[0].gridXpos - self.x)
                newBlockY[i] = (self.blockList[i].gridXpos - self.x) - (self.blockList[0].gridXpos - self.x) + (self.blockList[0].gridYpos - self.y)

                if newBlockX[i] >= gameBoardWidth or newBlockX[i] < 0:
                    canRotate = False
                elif newBlockY[i] >= gameBoardHeight or newBlockY[i] < 0:
                    canRotate = False
                elif self.activeBoardSpot[newBlockX[i]][newBlockY[i]] == True:
                    canRotate = False

            if canRotate == True:
                for i in range(self.numBlocks):
                    self.blockList[i].gridXpos = newBlockX[i] + self.x
                    self.blockList[i].gridYpos = newBlockY[i] + self.y

    def falling(self):
        for i in range(self.numBlocks):
            if self.blockList[i].gridYpos == gameBoardHeight - 1 \
                    or self.activeBoardSpot[self.blockList[i].gridXpos - self.x][self.blockList[i].gridYpos + 1 - self.y] == True:
                self.hitBottom()

        if self.active == True:
            for i in range(self.numBlocks):
                self.blockList[i].gridYpos = self.blockList[i].gridYpos + 1

    def hitBottom(self):
        self.active = False

        for i in range(self.numBlocks):
            self.activeBoardColor[self.blockList[i].gridXpos - self.x][self.blockList[i].gridYpos - self.y] = self.color
            self.activeBoardSpot[self.blockList[i].gridXpos - self.x][self.blockList[i].gridYpos - self.y] = True

    def drop(self):
        while self.active:
            for i in range(self.numBlocks):
                if self.blockList[i].gridYpos == gameBoardHeight - 1 or self.activeBoardSpot[self.blockList[i].gridXpos - self.x][
                            self.blockList[i].gridYpos + 1 - self.y] == True:
                    self.hitBottom()
            if self.active == True:
                for i in range(self.numBlocks):
                    self.blockList[i].gridYpos = self.blockList[i].gridYpos + 1

    def drawNextShape(self, screen, xpos, ypos):
        for i in range(self.numBlocks):
            pygame.draw.rect(screen, self.blockList[i].color, [self.blockList[i].gridXpos * self.blockList[i].size + xpos, self.blockList[i].gridYpos * self.blockList[i].size + ypos, self.blockList[i].size - 1, self.blockList[i].size - 1],0)
