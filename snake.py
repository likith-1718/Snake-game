import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480

# Set colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set game speed (higher value = faster speed)
game_speed = 15

# Create game window
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Set initial snake position
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set initial food position
food_position = [random.randrange(1, screen_width // 10) * 10,
                 random.randrange(1, screen_height // 10) * 10]
food_spawn = True

# Set initial direction (right)
direction = 'RIGHT'
change_to = direction

# Define function to display score
def show_score(score):
    font = pygame.font.SysFont('arial', 20)
    score_surface = font.render('Score: ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (screen_width / 2, 10)
    game_screen.blit(score_surface, score_rect)

# Main game loop
game_over = False
score = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'

    # Validate direction (avoid opposite direction)
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Update snake position
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    # Food spawn
    if not food_spawn:
        food_position = [random.randrange(1, screen_width // 10) * 10,
                         random.randrange(1, screen_height // 10) * 10]
    food_spawn = True

    # Draw game screen
    game_screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_screen, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > screen_width - 10:
        game_over = True
    if snake_position[1] < 0 or snake_position[1] > screen_height - 10:
        game_over = True
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True

    # Show score
    show_score(score)

    # Refresh game screen
    pygame.display.flip()

    # Set game speed
    clock.tick(game_speed)

# Quit the game
pygame.quit()
