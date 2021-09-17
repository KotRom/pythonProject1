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

def draw_window():
    # fill screen with one color passed as an RGB Tuple (255, 255, 255)
    # if fill will be applied after image, image will disappear
    WIN.fill((125, 125, 125))
    # display must be update every while cycle
    pygame.display.update()


def main():
    # In order to redraw main window a while loop is used
    condition = True
    while condition:
        # for loop for pygame events is used to check if event occurred
        for event in pygame.event.get():
            # Check if user quit the window
            if event.type == pygame.QUIT:
                condition = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

