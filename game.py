import pygame, sys
from pygame.locals import *

# initialize game engine
pygame.init()

window_width=1440
window_height=960

animation_increment=10
clock_tick_rate=20


size = (window_width, window_height)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Game")

mainChar = pygame.image.load('bully.png')





dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("background2.jpg").convert()

while(dead==False):

    angle = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    events = pygame.event.get()
    for event in events:
        if event.key == pygame.K_LEFT:

            
             

    

    screen.blit(background_image, [0, 0])
    screen.blit(mainChar, [630,520])

    pygame.display.flip()
    clock.tick(clock_tick_rate)
