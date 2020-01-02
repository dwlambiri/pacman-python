import pygame
import time
import random

class Snake:
    direction = 'x'
    poslist = [[0,0]]
    points = 0
    bored = [[0 for i in range(40)] for i in range(20)]
    bored[poslist[0][0]][poslist[0][1]] = 1
    apple = [0,0]
    def __init__(self):
        self.newApple()
        self.poslist[0][0] = random.randint(0,19)
        self.poslist[0][1] = random.randint(0, 39)
    def draw(self):
        print(self.direction)
        print(self.poslist)
        if self.direction == 'Left':
            self.poslist.insert(0, [self.poslist[0][0], self.poslist[0][1]-1])
        elif self.direction == 'Right':
            self.poslist.insert(0, [self.poslist[0][0], self.poslist[0][1]+1])
        elif self.direction == 'Up':
            self.poslist.insert(0, [self.poslist[0][0]-1, self.poslist[0][1]])
        elif self.direction == 'Down':
            self.poslist.insert(0, [self.poslist[0][0]+1, self.poslist[0][1]])
        else:
            self.poslist.insert(0, [self.poslist[0][0], self.poslist[0][1]])

        if self.poslist[0][1] < 0 or self.poslist[0][0] < 0 or self.poslist[0][0]  > 19 or self.poslist[0][1]  > 39:
            quit()

        if self.bored[self.poslist[0][0]][self.poslist[0][1]] == 2:
            self.newApple()
        elif self.bored[self.poslist[0][0]][self.poslist[0][1]] == 1 and len(self.poslist) > 2:
            quit()
        else:
            del (self.poslist[-1])

        self.bored = [[0 for i in range(40)] for i in range(20)]
        for i in self.poslist:
            self.bored[i[0]][i[1]] = 1
        self.bored[self.apple[0]][self.apple[1]] = 2
        drawbored(screen, self.bored)

    def newApple(self):
        while True:
            self.apple[0] = random.randint(0,19)
            self.apple[1] = random.randint(0, 39)
            if self.bored[self.apple[0]][self.apple[1]] != 1:
                break

def drawbored(screen, bored):
    for i, list in enumerate(bored):
        for ii, value in enumerate(list):
            if value == 0:
                pygame.draw.rect(screen, (0,0,0), (ii*30, i*30, 30, 30))
            elif value == 1:
                pygame.draw.rect(screen, (0, 255, 0), (ii * 30, i * 30, 30, 30))
            elif value == 2:
                pygame.draw.rect(screen, (0, 0, 255), (ii * 30, i * 30, 30, 30))


pygame.init()

player1 = Snake()
screen = pygame.display.set_mode((30 * len(player1.bored[0]), (30 * len(player1.bored))))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player1.direction != "Down":
                player1.direction = "Up"
            elif event.key == pygame.K_LEFT and player1.direction != "Right":
                player1.direction = "Left"
            elif event.key == pygame.K_DOWN and player1.direction != "Up":
                player1.direction = "Down"
            elif event.key == pygame.K_RIGHT and player1.direction != "Left":
                player1.direction = "Right"
    player1.draw()
    pygame.display.update()
    time.sleep(0.03)


