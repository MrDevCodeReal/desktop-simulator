import pygame
from pygame.locals import *
import time

pygame.init()
#create window, clock, and delta time variables
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
prevTime = time.time()

#create a canvas and set it to the desired screen resolution
#this will be the playground
screenSize = screen.get_size()
resolution = 5
canvas = pygame.surface.Surface((screenSize[0]//resolution, screenSize[1]//resolution))

#load cursor images for wallpapers cursors etc and hide cursor
pygame.mouse.set_visible(False)
cursorImage = pygame.image.load("cursor.png")
wallpaper = pygame.image.load("wallpaper.png")

#game loop
running = True
while running:
    #clear the canvas to for next frame
    canvas.blit(pygame.transform.scale(wallpaper, canvas.get_size()), (0,0))

    #get mouse pos
    mousePos = pygame.mouse.get_pos()

    #calculate delta time
    crntTime = time.time()
    deltaTime = crntTime - prevTime
    prevTime = crntTime

    #handle events
    for event in pygame.event.get():
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    #display the cursor on the canvas
    canvas.blit(cursorImage, (mousePos[0]//resolution, mousePos[1]//resolution))

    #draw a taskbar placeholder for now

    #display the canvas on the screen
    screen.blit(pygame.transform.scale(canvas, screenSize), (0, 0))

    pygame.display.flip()

pygame.quit()