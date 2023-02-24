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
char_vel = [0, 0]
gravity = 0.1
dragging = False

# Set up font and text
font = pygame.font.SysFont("Arial", 30)
text = font.render("Use the mouse to drag", True, (0, 0, 0))
text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

# Set timer for text to disappear after 3 seconds
text_timer = 3 * 60  

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
                pre_x = event.pos[0] - char_pos[0]
                pre_y = event.pos[1] - char_pos[1]
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    # Update character's position and velocity
    char_vel[1] += gravity
    if dragging:
        # Update character position while dragging
        char_pos = [event.pos[0] - pre_x, event.pos[1] - pre_y]
    else:
        # Update character position with gravity
        char_pos[0] += char_vel[0]
        char_pos[1] += char_vel[1]
        
    # Check if character hits top of the screen
    if char_pos[1] < 0:
        char_vel[1] = 0
        char_pos[1] = 0

    # Check if character hits bottom of the screen
    if char_pos[1] + char_rect.height > screen.get_height():
        char_vel[1] = 0
        char_pos[1] = screen.get_height() - char_rect.height

    # Update character rect
    char_rect.x = char_pos[0]
    char_rect.y = char_pos[1]

    # Clear screen
    screen.fill((192, 192, 192))

    # Render character
    screen.blit(char_image, char_rect)

    # Render text if timer hasn't expired
    if text_timer > 0:
        screen.blit(text, text_rect)
        text_timer -= 1

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)

# Quit game
pygame.quit()
