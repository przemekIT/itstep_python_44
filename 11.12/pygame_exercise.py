import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prosty przykład w Pygame")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

rect_width = 50
rect_height = 50
rect_x = screen_width // 2 - rect_width // 2
rect_y = screen_height // 2 - rect_height // 2

rect_speed = 10

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed    
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    if rect_x < 0:
        rext_x = 0
    if rect_x + rect_width >screen_width:
        rect_x = screen_width - rect_height

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()


