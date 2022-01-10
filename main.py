import pygame
import random

import render
import mobs_table
import global_variables

pygame.init()


def get_current_choice():
    for i, rect in enumerate(global_variables.option_hitboxes):
        if rect.collidepoint(pygame.mouse.get_pos()):
            return current_mob.choice_list[i]
    return None


def process_click():
    if render.symbol_counter < len(render.central_text):
        render.symbol_counter = len(render.central_text)
    elif current_option is not None:
        result = current_option.perform_choice()
        if result is not None:
            close_mob(result)
    elif current_mob == mobs_table.empty:
        summon_new_mob()


def close_mob(result):
    global current_mob
    global current_option

    current_mob = mobs_table.empty
    render.current_mob = current_mob
    render.symbol_counter = 0
    render.central_text = result
    current_option = None


def summon_new_mob():
    global current_mob
    global current_option

    current_mob = random.choice(mobs_table.mobs)
    render.current_mob = current_mob
    render.symbol_counter = 0
    render.central_text = current_mob.text
    current_option = None


if __name__ == '__main__':
    time = 0
    screen = pygame.display.set_mode(global_variables.size)
    clock = pygame.time.Clock()
    running = True
    current_mob = None

    summon_new_mob()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    process_click()

        if current_mob != mobs_table.empty:
            current_option = get_current_choice()
        render.update_screen(screen)

        delta_time = clock.tick(60) / 1000
        time += delta_time
    pygame.quit()
