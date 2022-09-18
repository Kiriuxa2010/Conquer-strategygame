import pygame
from pygame import mixer
from sprites import *
from settings import *

pygame.init()

X = 400
Y = 400

# music
mixer.init()
mixer.music.load('GameFiles/music/Menu3.mp3')
mixer.music.set_volume(0.4)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('GameFiles/music/Menu3.mp3'))

# main

scr = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
pygame.display.set_caption('Conquer TEST 0.3')
clock = pygame.time.Clock()
pygame.display.set_icon(pygame_icon)
pygame.BUTTON_LEFT

font = pygame.font.Font('GameFiles/fonts/font.ttf', 32)

text = font.render('Conquer | SpAcE 0.3', True, WHITE, RED)
text2 = font.render('PRESS ESC TO EXIT', True, WHITE, RED)
textRect = text.get_rect()
textRect2 = text2.get_rect()

textRect.center = (X // 3,Y // 2)
textRect2.center = (X //3, Y// 1)
# sprites
def sprite(x,y):
    scr.blit(sprite01, (x,y))

x = (WIDTH * 0.50)
y = (HEIGHT * 0.10)

pygame.display.flip()

running = True
# loop
while running:
    scr.blit(bg, (300, 10))
    sprite(x,y)
    scr.blit(text,textRect)
    scr.blit(text2, textRect2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 290:
        x -= 2
    

    if keys[pygame.K_RIGHT] and x < 1180:
        x += 2

    if keys[pygame.K_UP] and y > 10:
        y -= 2

    if keys[pygame.K_DOWN] and y < 880:
        y += 2

    if keys[pygame.K_ESCAPE]:
        quit()

    if keys[pygame.K_c]:
        line1()

    clock.tick(60)
