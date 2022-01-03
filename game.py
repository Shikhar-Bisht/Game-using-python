import pygame
import math
import random
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("SPACE BATTEL")
icon = pygame.image.load('gundam.png')
pygame.display.set_icon(icon)
spaceship = pygame.image.load('space-invaders.png')
stars = pygame.image.load('stars.png')
bullet = pygame.image.load('bullet.png')
monster = pygame.image.load('monster.png')
background = pygame.image.load('background.jpg')
mixer.music.load("background.mp3")
mixer.music.play(-1)
spaceshipX = 550
spaceshipY = 550
spaceshipX_change = 0
spaceshipY_change = 0
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 40)
textX = 10
textY = 10
monsterX = {}
for i in range(0, 5):
    monsterX[i] = random.randint(0, 1200)
monsterY = {}
for i in range(0, 5):
    monsterY[i] = random.randint(0, 10)
monsterX_change = [3.5, 3.5, 3.5, 3.5, 3.5]
monsterY_change = [3.5, 3.5, 3.5, 3.5, 3.5]
bulletX = 0
bulletY = 550
bullet_changeY = 10
bullet_state = "ready"
distance = 0

def show_score(x,y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def spaceshipf(x, y):
    screen.blit(spaceship, (x, y))


def monsterf(x, y):
    screen.blit(monster, (x, y))


def backgroundf():
    screen.blit(background, (0, 0))


def bulletf(a, b):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (a + 24, b + 10))


def collisionf(X, Y, X1, Y1):
    distance = math.sqrt((math.pow(X - X1, 2)) + (math.pow(Y - Y1, 2)))
    if distance < 27:
        return True
    else:
        return False


Running = True
while Running:
    backgroundf()
    if spaceshipX <= 0:
        spaceshipX = 0
    if spaceshipX >= 1134:
        spaceshipX = 1134
    if spaceshipY <= 0:
        spaceshipY = 0
    if spaceshipY >= 634:
        spaceshipY = 634
    for i in range(0, 5):
        if monsterX[i] <= 0:
            monsterX_change[i] = 3
        if monsterX[i] >= 1134:
            monsterX_change[i] = -3
        if monsterY[i] <= 0:
            monsterY_change[i] = 3
        if monsterY[i] >= 400:
            monsterY_change[i] = -3
        if bulletY <= 0:
            bulletY = spaceshipY
            bullet_state = "ready"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceshipX_change = -5
            if event.key == pygame.K_RIGHT:
                spaceshipX_change = 5
            if event.key == pygame.K_UP:
                spaceshipY_change = -5
            if event.key == pygame.K_DOWN:
                spaceshipY_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    mixer.music.load("bullet.wav")
                    mixer.music.play(1)
                    bulletX = spaceshipX-8
                    bulletf(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spaceshipX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                spaceshipY_change = 0

    spaceshipX += spaceshipX_change
    spaceshipY += spaceshipY_change
    if bullet_state == "fire":
        bulletf(bulletX, bulletY)
        bulletY -= bullet_changeY
    for i in range(0, 5):
        collision = collisionf(monsterX[i], monsterY[i], bulletX, bulletY)
        if collision:
            mixer.music.load("explosion.wav")
            mixer.music.play(1)
            bulletY = spaceshipY
            bullet_state = "ready"
            score_value += 1

            monsterX[i] = random.randint(0, 1200)
            monsterY[i] = random.randint(0, 50)
    for i in range(0, 5):
        monsterX[i] += monsterX_change[i]
        monsterY[i] += monsterY_change[i]
        monsterf(monsterX[i], monsterY[i])
    show_score(textX, textY)
    spaceshipf(spaceshipX, spaceshipY)
    pygame.display.update()
