import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 30)

# Snake settings
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'

# Food settings
food_x = random.randrange(0, WIDTH, CELL_SIZE)
food_y = random.randrange(0, HEIGHT, CELL_SIZE)

# Score
score = 0


def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))


def draw_food():
    pygame.draw.rect(screen, RED, (food_x, food_y, CELL_SIZE, CELL_SIZE))


def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def move_snake():
    global food_x, food_y, score

    head_x, head_y = snake[0]

    if direction == 'UP':
        head_y -= CELL_SIZE
    elif direction == 'DOWN':
        head_y += CELL_SIZE
    elif direction == 'LEFT':
        head_x -= CELL_SIZE
    elif direction == 'RIGHT':
        head_x += CELL_SIZE

    new_head = (head_x, head_y)

    # Game over conditions
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake
    ):
        game_over()

    snake.insert(0, new_head)

    # Eating food
    if head_x == food_x and head_y == food_y:
        score += 1
        food_x = random.randrange(0, WIDTH, CELL_SIZE)
        food_y = random.randrange(0, HEIGHT, CELL_SIZE)
    else:
        snake.pop()


def game_over():
    over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)

    screen.fill(BLACK)
    screen.blit(over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - 120, HEIGHT // 2))
    pygame.display.update()

    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    move_snake()

    screen.fill(BLACK)

    draw_snake()
    draw_food()
    show_score()

    pygame.display.update()

    clock.tick(10)
