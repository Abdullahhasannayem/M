import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Abdullah Hasan Nayem Animation")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 24)

# Texts
text_abdullah = font.render("Abdullah", True, GREEN)
text_hasan = font.render("Hasan", True, GREEN)
text_nayem = font.render("Nayem", True, GREEN)

# Positions
abdullah_x = -200  # Start off-screen left
abdullah_y = 150
hasan_x = SCREEN_WIDTH // 2 - text_hasan.get_width() // 2
hasan_y = -100  # Start off-screen top
nayem_x = SCREEN_WIDTH  # Start off-screen right
nayem_y = 350

# Background effect
def draw_hacking_background():
    for _ in range(150):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        char = chr(random.randint(33, 126))  # Random ASCII character
        label = small_font.render(char, True, GREEN)
        screen.blit(label, (x, y))

# Main loop
clock = pygame.time.Clock()
running = True
frame_count = 0

while running:
    screen.fill(BLACK)
    draw_hacking_background()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animate "Abdullah"
    if abdullah_x < SCREEN_WIDTH // 2 - text_abdullah.get_width() // 2:
        abdullah_x += 5  # Move right

    # Animate "Hasan"
    if hasan_y < SCREEN_HEIGHT // 2 - text_hasan.get_height() // 2:
        hasan_y += 5  # Move down

    # Animate "Nayem"
    if nayem_x > SCREEN_WIDTH // 2 - text_nayem.get_width() // 2:
        nayem_x -= 5  # Move left

    # Draw texts
    screen.blit(text_abdullah, (abdullah_x, abdullah_y))
    screen.blit(text_hasan, (hasan_x, hasan_y))
    screen.blit(text_nayem, (nayem_x, nayem_y))

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()