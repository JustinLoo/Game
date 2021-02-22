import pygame, sys
from pygame.locals import *

# initialize game engine
pygame.init()

window_width=1440
window_height=960


size = (window_width, window_height)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Game")



mainRect = mainChar.get_rect(center = (300,300))

angle = 0
clock = pygame.time.Clock()


#images
mainChar = pygame.image.load('bully.png')

background_image = pygame.image.load("background2.jpg").convert()





def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle,1)
    rotated_rect = rotated_surface.get_rect(center = (720,620))
    return rotated_surface,rotated_rect


def main():
    while True:
   
    angle += 1

    mainChar_rotated, mainRect_rect = rotate(mainChar, angle)

    screen.blit(background_image, [0, 0])

    screen.blit(mainChar_rotated, mainRect_rect)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
    
    pygame.display.flip()
    clock.tick(30)




