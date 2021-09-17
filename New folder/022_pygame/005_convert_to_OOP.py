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


class Cat(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jump_state = False
        self.jump_count = 10
        self.walk_state = False
        self.walk_count = 0
        self.auto = False


CAT = Cat(0, 436, 64, 64)

def draw_window():
    # Draw a rectangle
    WIN.blit(BG_IMG, (0, 0))
    WIN.blit(CAT_IMG, (CAT.x, CAT.y))


    # display must be update every while cycle
    pygame.display.update()


def main():
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

        if pressed_keys[pygame.K_LEFT] and CAT.x > CAT.vel:
            CAT.x -= CAT.vel
        if pressed_keys[pygame.K_RIGHT] and CAT.x < WIN_WIDTH - CAT.width - CAT.vel:
            CAT.x += CAT.vel
        else:
            CAT.walk_count = 0

        # Checks if is jumping
        # blocks up and down movement while jumping
        if not CAT.jump_state:
            if pressed_keys[pygame.K_SPACE]:
                CAT.jump_state = True
        else:

            if CAT.jump_count >= -10:
                neg = 1
                if CAT.jump_count < 0:
                    neg = -1
                CAT.y -= (CAT.jump_count ** 2) * 0.5 * neg
                CAT.jump_count -= 1
            # Ensure that jump stops change jump count back to 10
            else:
                CAT.jump_state = False
                CAT.jump_count = 10

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

