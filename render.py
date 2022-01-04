import pygame


def draw_light_beam(screen):
    pygame.draw.polygon(screen, pygame.Color(100, 128, 100), [(250, 0), (125, 375), (375, 375)])
    pygame.draw.ellipse(screen, pygame.Color(0, 128, 0), pygame.Rect((125, 350), (250, 50)))


def update_screen(screen):
    screen.fill(pygame.Color('black'))
    draw_light_beam(screen)
    pygame.display.flip()
