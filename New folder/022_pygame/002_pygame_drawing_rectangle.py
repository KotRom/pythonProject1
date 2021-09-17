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

# rect parameters
POS_X = 50
POS_Y = 50
WIDTH = 40
HEIGHT = 60
VEL = 5



def draw_window():
    # Draw a rectangle
    WIN.fill((125, 125, 125))
    pygame.draw.rect(WIN, (255, 0, 0), (POS_X, POS_Y, WIDTH, HEIGHT))
    # display must be update every while cycle
    pygame.display.update()


def main():
    global POS_X, POS_Y, WIDTH, HEIGHT, VEL
    # In order to redraw main window a while loop is used
    condition = True
    while condition:
        pygame.time.delay(50)
        # for loop for pygame events is used to check if event occurred
        for event in pygame.event.get():
            # Check if user quit the window
            if event.type == pygame.QUIT:
                condition = False
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and POS_X > VEL:
            POS_X -= VEL
        if pressed_keys[pygame.K_RIGHT] and POS_X < WIN_WIDTH - WIDTH - VEL:
            POS_X += VEL
        if pressed_keys[pygame.K_UP] and POS_Y > VEL:
            POS_Y -= VEL
        if pressed_keys[pygame.K_DOWN] and POS_Y < WIN_HEIGHT - HEIGHT - VEL:
            POS_Y += VEL
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

