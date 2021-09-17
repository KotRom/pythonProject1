# pip install pygame
# https://www.pygame.org/docs/

import pygame

pygame.init()
# Creating a window
WIN_WIDTH, WIN_HEIGHT = 900, 500
# Width and height are given as a Tuple
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# Setting program title
pygame.display.set_caption("Let's learn Pygame")

BG_IMG = pygame.image.load('assets/bg.png')
CAT_IMG = pygame.image.load('assets/cat.png')
SPRITE_WALK = [pygame.image.load('assets/adventurer-run-00.png'), pygame.image.load('assets/adventurer-run-01.png'),
               pygame.image.load('assets/adventurer-run-02.png'), pygame.image.load('assets/adventurer-run-03.png'),
               pygame.image.load('assets/adventurer-run-04.png'), pygame.image.load('assets/adventurer-run-05.png')]

CLOCK = pygame.time.Clock()
FPS = 30

# rect parameters
POS_X = 0
POS_Y = 436
WIDTH = 64
HEIGHT = 64
# # walk dimensions
# WIDTH = 50
# HEIGHT = 37

VEL = 5
JUMP_STATE = False
JUMP_COUNT = 10
WALK_STATE = False
WALK_COUNT = 0



def draw_window():
    global WALK_COUNT
    # Draw a rectangle
    WIN.blit(BG_IMG, (0, 0))
    WIN.blit(CAT_IMG, (POS_X, POS_Y))
    # if WALK_COUNT + 1 >= 30:
    #     WALK_COUNT = 0
    # WIN.blit(SPRITE_WALK[WALK_COUNT//5], (POS_X, POS_Y))
    # WALK_COUNT += 1

    # display must be update every while cycle
    pygame.display.update()


def main():
    global POS_X, POS_Y, WIDTH, HEIGHT, VEL, JUMP_STATE, JUMP_COUNT, WALK_STATE, WALK_COUNT
    # In order to redraw main window a while loop is used
    condition = True
    while condition:
        CLOCK.tick(FPS)
        pygame.time.delay(50)
        # for loop for pygame events is used to check if event occurred
        for event in pygame.event.get():
            # Check if user quit the window
            if event.type == pygame.QUIT:
                condition = False
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and POS_X > VEL:
            POS_X -= VEL
            WALK_STATE = True
        if pressed_keys[pygame.K_RIGHT] and POS_X < WIN_WIDTH - WIDTH - VEL:
            POS_X += VEL
            WALK_STATE = True
        else:
            WALK_COUNT = 0

        # Checks if is jumping
        # blocks up and down movement while jumping
        if not JUMP_STATE:
            if pressed_keys[pygame.K_SPACE]:
                JUMP_STATE = True
        else:

            if JUMP_COUNT >= -10:
                neg = 1
                if JUMP_COUNT < 0:
                    neg = -1
                POS_Y -= (JUMP_COUNT ** 2) * 0.5 * neg
                JUMP_COUNT -= 1
            # Ensure that jump stops change jump count back to 10
            else:
                JUMP_STATE = False
                JUMP_COUNT = 10
                WALK_STATE = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

