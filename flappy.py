import pygame, sys

def draw_floor(): #use two floors to not show the end of the image
    screen.blit(floor_surface, (floor_x_pos, 630))
    screen.blit(floor_surface, (floor_x_pos + 400, 630))


pygame.init() # initialize pygame
screen = pygame.display.set_mode((400,711)) # screen to draw on
clock = pygame.time.Clock() # to set the frame rate of the game

bg_surface = pygame.image.load('assets/background-day.png').convert() # convert makes the game run faster
bg_surface = pygame.transform.scale(bg_surface, (400, 711)) # fit the screen

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (400,133))
floor_x_pos = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # X button
            pygame.quit() # quit the game
            sys.exit() # quit the while loop

    screen.blit(bg_surface,(0,0)) # draw the image starting at top left corner
    floor_x_pos -= 1

    draw_floor()
    if floor_x_pos <= -400: # reset position when the first floor is complete out of the picture
        floor_x_pos = 0

    pygame.display.update() # to update the frame
    clock.tick(60) # frame rate
