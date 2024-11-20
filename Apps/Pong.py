import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 102, 204)

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6

# Ball settings
BALL_SIZE = 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Initialize font for scoring
font = pygame.font.SysFont('Arial', 30)
button_font = pygame.font.SysFont('Arial', 24)

# Paddle positions
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball position
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Ball velocity
ball_velocity_x = BALL_SPEED_X
ball_velocity_y = BALL_SPEED_Y

# Scores
player_score = 0
ai_score = 0

# Game state
game_running = False
game_paused = False

# Clock object to control game speed
clock = pygame.time.Clock()

# Function to reset the ball to the center
def reset_ball():
    global ball_velocity_x, ball_velocity_y
    ball.x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2
    ball_velocity_x = -ball_velocity_x  # Change direction

# Function to update the game screen
def update_screen():
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, ai_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display scores
    score_text = font.render(f"{player_score} - {ai_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Display pause/play text if game is paused
    if game_paused:
        paused_text = font.render("Game Paused", True, WHITE)
        screen.blit(paused_text, (WIDTH // 2 - paused_text.get_width() // 2, HEIGHT // 2 - 50))

    # Draw pause and resume buttons at the top right
    draw_buttons()

    pygame.display.flip()

# Function to move the AI paddle
def move_ai():
    if ai_paddle.centery < ball.centery:
        ai_paddle.y += PADDLE_SPEED
    elif ai_paddle.centery > ball.centery:
        ai_paddle.y -= PADDLE_SPEED

    # Prevent AI paddle from going off-screen
    if ai_paddle.top < 0:
        ai_paddle.top = 0
    if ai_paddle.bottom > HEIGHT:
        ai_paddle.bottom = HEIGHT

# Function to handle player paddle movement
def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

# Function to draw buttons on the screen
def draw_buttons():
    pause_button = pygame.Rect(WIDTH - 110, 10, 100, 40)
    resume_button = pygame.Rect(WIDTH - 110, 60, 100, 40)

    # Button hover effect
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Pause button
    if pause_button.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, pause_button)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, pause_button)
    pause_text = button_font.render("Pause", True, WHITE)
    screen.blit(pause_text, (WIDTH - 60 - pause_text.get_width() // 2, 20))

    # Resume button
    if resume_button.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, resume_button)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, resume_button)
    resume_text = button_font.render("Resume", True, WHITE)
    screen.blit(resume_text, (WIDTH - 60 - resume_text.get_width() // 2, 70))

# Function to handle button clicks
def handle_buttons():
    global game_running, game_paused, player_score, ai_score, ball_velocity_x, ball_velocity_y

    mouse_x, mouse_y = pygame.mouse.get_pos()

    pause_button = pygame.Rect(WIDTH - 110, 10, 100, 40)
    resume_button = pygame.Rect(WIDTH - 110, 60, 100, 40)

    if pause_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
        game_paused = True

    if resume_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
        game_paused = False

# Function to display the start button
def draw_start_button():
    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)

    # Button hover effect
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if start_button.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, start_button)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, start_button)

    start_text = button_font.render("Start Game", True, WHITE)
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 10))

    return start_button

# Main game loop
def game_loop():
    global player_score, ai_score, ball_velocity_x, ball_velocity_y, game_running, game_paused

    while True:
        clock.tick(60)  # 60 frames per second

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # If the game isn't running, show the start button
        if not game_running:
            start_button = draw_start_button()
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Start game if start button is clicked
            if start_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                game_running = True
                reset_ball()
                player_score = 0
                ai_score = 0

        # If the game is running, handle gameplay
        if game_running and not game_paused:
            move_player()
            move_ai()

            # Move ball
            ball.x += ball_velocity_x
            ball.y += ball_velocity_y

            # Ball collision with top and bottom walls
            if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball_velocity_y = -ball_velocity_y

            # Ball collision with paddles
            if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
                ball_velocity_x = -ball_velocity_x

            # Ball passes the player paddle
            if ball.left <= 0:
                ai_score += 1
                reset_ball()

            # Ball passes the AI paddle
            if ball.right >= WIDTH:
                player_score += 1
                reset_ball()

        # Handle pause and resume buttons
        if game_running:
            handle_buttons()

        # Update screen
        update_screen()

# Run the game
if __name__ == "__main__":
    game_loop()
