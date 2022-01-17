import global_variables
import pygame
import math

current_mob = None
w, h = global_variables.size
frame_counter = 0
symbol_counter = 0
central_text = ''
text = ''


def draw_light_beam(screen):
    points = [(w // 2, 0), (w // 4, h // 2), (w * 0.75, w // 2)]
    pygame.draw.polygon(screen, pygame.Color(100, 128, 100), points)
    pygame.draw.ellipse(screen, pygame.Color(0, 128, 0), pygame.Rect((w // 4, h // 2 - h // 20), (w // 2, h // 10)))


def render_mob(screen, mob):
    position = (global_variables.WIDTH - 64 * 3) // 2,\
               (global_variables.HEIGHT - 64 * 3) // 2 - 50
    screen.blit(mob.texture, position)


def display_central_text(screen, text):
    pygame.draw.rect(screen, pygame.Color(100, 255, 100),
                     pygame.Rect((5, h // 2 + h // 20 + 10), (w - 10, h // 10)), 2)
    font = pygame.font.Font(None, 30)
    for i, line in enumerate(text.split('\n')):
        text = font.render(line, True, pygame.Color(100, 128, 100))
        screen.blit(text, (10, h // 2 + h // 20 + 20 + i * font.get_height() + 5))


def render_options_list(screen, options):
    global_variables.option_hitboxes.clear()
    for i, choice in enumerate(options):
        if all([item in global_variables.inventory
                for item in choice.items_required]):
            text_color = pygame.Color(100, 128, 100)
            frame_color = pygame.Color(100, 255, 100)
        else:
            text_color = pygame.Color(50, 64, 50)
            frame_color = pygame.Color(50, 128, 50)

        position = (5, h // 20 * 13 + (h // 20 + 10) * i + 30)
        pygame.draw.rect(screen, frame_color,
                         pygame.Rect(position,
                                     (w - 10, h // 20)), 2)
        global_variables.option_hitboxes.append(pygame.Rect(position, (w - 10, h // 20)))
        font = pygame.font.Font(None, 30)
        text = font.render(choice.text, True, text_color)
        screen.blit(text, (position[0] + 10, position[1] + 10))


def update_screen(screen):
    global frame_counter
    global symbol_counter
    global text
    frame_counter += 1
    if frame_counter == 5:
        symbol_counter += 1
        text = central_text[:symbol_counter]
        frame_counter = 0

    draw_light_beam(screen)
    render_mob(screen, current_mob)
    display_central_text(screen, text)
    if symbol_counter > len(central_text):
        render_options_list(screen, current_mob.choice_list)
    pygame.display.flip()


"""Title screen stuff"""
title_frame_counter = 0
text_alpha = 1
text_pos = -100


def render_title_screen(screen):
    global title_frame_counter
    global text_alpha
    global text_pos
    title_frame_counter += 1
    color = pygame.Color(100, 255, 100)
    font = pygame.font.Font(None, 70)
    text_img = font.render('IN THE DUNGEON', True, color)
    text_img = pygame.transform.scale(text_img, (w, text_img.get_height() * w // text_img.get_width()))

    if title_frame_counter == 5:
        text_alpha += 1
        text_pos += 10 if text_pos <= h // 2 - text_img.get_height() // 2 else 0
        title_frame_counter = 0

    text_img.set_alpha(text_alpha)
    screen.blit(text_img, (w // 2 - text_img.get_width() // 2, text_pos))
    pygame.display.flip()
