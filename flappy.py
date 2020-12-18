import pygame, sys

def draw_floor(): #use two floors to not show the end of the image
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 672, 900))

def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (700, 512)) # placed the pipe rect in the middle of the screen
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        if pipe.centerx < -700: # remove the pipes the out of screen
            pipes.remove(pipe)
        pipe.centerx -= 5

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

pygame.init() # initialize pygame
screen = pygame.display.set_mode((576,1024)) # screen to draw on
clock = pygame.time.Clock() # to set the frame rate of the game

# Game Varibales
gravity = 0.25
bird_movement = 0

# Load the background
bg_surface = pygame.image.load('assets/background-day.png').convert() # convert makes the game run faster
bg_surface = pygame.transform.scale2x(bg_surface) # fit the screen

# Load the floor
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# Load the bird
bird_surface = pygame.image.load(('assets/bluebird-midflap.png')).convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512)) # put the bird in a rectangle at a specific location

# Load the pipes
pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
# Spawn new pipe every 1.2 sec
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # X button
            pygame.quit() # quit the game
            sys.exit() # quit the while loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -12
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

    # Draw the background
    screen.blit(bg_surface,(0,0)) # draw the image starting at top left corner

    # Draw the bird
    screen.blit(bird_surface, bird_rect)
    bird_movement += gravity # movement will compound by gravity
    bird_rect.centery += bird_movement # move the rect

    # Draw the pipes
    move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Draw the floor
    draw_floor()
    floor_x_pos -= 5
    if floor_x_pos < -672: # reset position when the first floor is complete out of the picture
        floor_x_pos = 0

    pygame.display.update() # to update the frame
    clock.tick(120) # frame rate
