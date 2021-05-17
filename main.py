import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800,600])
FPS = 100
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Space Invaders')
icon =pygame.image.load('project.png')

pygame.display.set_icon(icon)



playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.9
enemyY_change = 40


bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"



def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bulletImg,(x+16,y+14))


background = pygame.image.load('bgspace.jpg')

running = True

# Run until the user asks to quit
while running:

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        # Did the user click the window close button?

        playerX += playerX_change
        if playerX <= 0:
            playerX= 0
        elif playerX >= 736:
            playerX = 736

        enemyX += enemyX_change
        if enemyX <= 0:
            enemyX_change = 15
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change = -15
            enemyY += enemyY_change

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(playerX,bulletY)
            bulletY-= bulletY_change

        enemy(enemyX,enemyY)
        player(playerX,playerY)
        pygame.display.update()
        fpsClock.tick(FPS)

