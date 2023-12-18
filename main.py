import pygame
import sys
from os import path
import bard

# Constants
WIDTH, HEIGHT = 800, 800
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Colors
WHITE = (186, 202, 68)
BLACK = (0, 68, 116)

# Initialize Pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board")

# Load knight image
knight_image = pygame.image.load(path.join('src','knight.png'))
knight_image = pygame.transform.scale(knight_image, (SQUARE_SIZE, SQUARE_SIZE)).convert_alpha()

# Function to draw the chess board
def draw_chess_board(knight, move_number):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    x, y = knight
    screen.blit(knight_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))

    font = pygame.font.Font(None, 36)
    text = font.render(str(move_number), True, (255, 255, 255))
    screen.blit(text, (x * SQUARE_SIZE + SQUARE_SIZE // 3, y * SQUARE_SIZE + SQUARE_SIZE // 3))

    pygame.display.flip()

# Main loop
running = True
bard.max_generations=1000
tour = bard.knights_tour()
move_number = 0

while running and move_number < BOARD_SIZE ** 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the chess board with the knight's tour
    draw_chess_board(tour[move_number], move_number)

    # Add a delay to slow down the animation
    pygame.time.delay(500)

    move_number += 1

# Quit Pygame
pygame.quit()
sys.exit()
