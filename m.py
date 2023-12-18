import random
import pygame
import sys
from os import path

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
knight_image = pygame.transform.scale(knight_image, (SQUARE_SIZE, SQUARE_SIZE))

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

# Function to generate a valid knight's tour
def generate_knight_tour():
    tour = [(0, 0)]
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    for _ in range(1, BOARD_SIZE ** 2):
        current_x, current_y = tour[-1]

        # Filter valid moves
        valid_moves = [(current_x + dx, current_y + dy) for dx, dy in moves if 0 <= current_x + dx < BOARD_SIZE and 0 <= current_y + dy < BOARD_SIZE and (current_x + dx, current_y + dy) not in tour]

        # Check if there are no valid moves
        if not valid_moves:
            break

        # Randomly select a valid move
        next_move = random.choice(valid_moves)
        tour.append(next_move)

    return tour

# Main loop
running = True
tour = generate_knight_tour()
move_number = 1

while running and move_number <= BOARD_SIZE ** 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the chess board with the knight's tour
    draw_chess_board(tour[move_number - 1], move_number)

    # Add a delay to slow down the animation
    pygame.time.delay(500)

    move_number += 1

# Quit Pygame
pygame.quit()
sys.exit()
