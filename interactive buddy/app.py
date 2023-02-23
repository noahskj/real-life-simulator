import pygame

# Initialize the game window
pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

# Load the character sprite
char_image = pygame.image.load("mario.png")
char_rect = char_image.get_rect()

# Create a character object with initial position, velocity, and acceleration
char_pos = [100, 100]
dragging = False

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Start dragging if mouse is over the character
            if char_rect.collidepoint(event.pos):
                dragging = True
                pre_x = event.pos[0] - char_rect.x
                pre_y = event.pos[1] - char_rect.y
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    # Update character's position and velocity
    if dragging:
        x, y = pygame.mouse.get_pos()
        char_pos = [x - pre_x, y - pre_y]

    # Update character rect
    char_rect.x = char_pos[0]
    char_rect.y = char_pos[1]

    # Clear screen
    screen.fill((255, 255, 255))

    # Render character
    screen.blit(char_image, char_rect)

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)

# Quit game
pygame.quit()
