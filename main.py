import pygame
import render


if __name__ == '__main__':
    size = WIDTH, HEIGHT = 500, 500
    time = 0
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render.update_screen(screen)

        delta_time = clock.tick(60) / 1000
        time += delta_time
    pygame.quit()
