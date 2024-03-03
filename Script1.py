import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_WIDTH = 4
CELL_SIZE = WIDTH // 3

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Game variables
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

    # Handle user input
    mouse_x, mouse_y = pygame.mouse.get_pos()
    row = mouse_y // CELL_SIZE
    col = mouse_x // CELL_SIZE
    if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
        if board[row][col] == ' ':
            board[row][col] = current_player
            current_player = 'O' if current_player == 'X' else 'X'

    # Draw X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (col * CELL_SIZE, row * CELL_SIZE),
                                 ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, LINE_COLOR, ((col + 1) * CELL_SIZE, row * CELL_SIZE),
                                 (col * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, LINE_COLOR,
                                   (int(col * CELL_SIZE + CELL_SIZE / 2), int(row * CELL_SIZE + CELL_SIZE / 2)),
                                   int(CELL_SIZE / 2 - LINE_WIDTH), LINE_WIDTH)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()