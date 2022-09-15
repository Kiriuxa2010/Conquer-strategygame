import pygame
from pygame import mixer



# sc
WIDTH = 800
HEIGHT = 600

#Colors
GREEN = 000,255,000
WHITE = 255,255,255

# music
mixer.init()
mixer.music.load('/home/kirill/vscode/python/Conquer/GameFiles/menu.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()

# main
pygame_icon = pygame.image.load('/home/kirill/vscode/python/Conquer/GameFiles/icon.png')
scr = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
pygame.display.set_caption('Conquer TEST 0.1')
clock = pygame.time.Clock()
sprite01 = pygame.image.load('/home/kirill/vscode/python/Conquer/GameFiles/Sprite.png')
pygame.display.set_icon(pygame_icon)

# sprites
def sprite(x,y):
    scr.blit(sprite01, (x,y))

x = (WIDTH * 0.50)
y = (HEIGHT * 0.10)



pygame.display.flip()

running = True

# loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scr.fill(WHITE)
    sprite(x,y)

    pygame.display.update()
    clock.tick(60)
