import pygame
import random

import render
import mobs_table
import global_variables

pygame.init()


def restart():
    global_variables.inventory.clear()
    global_variables.atk = 1
    global_variables.karma = 0
    global_variables.is_dead = False
    summon_mob(random.choice(mobs_table.mobs))


def get_current_choice():
    for i, rect in enumerate(global_variables.option_hitboxes):
        if rect.collidepoint(pygame.mouse.get_pos()):
            return current_mob.choice_list[i]
    return None


def process_click():
    global in_title_screen
    if in_title_screen:
        in_title_screen = False
    elif render.symbol_counter < len(render.central_text):
        render.symbol_counter = len(render.central_text)
    elif current_option is not None:
        if current_option.is_fighting:
            if global_variables.atk < current_mob.atk:
                die()
                return
        result = current_option.perform_choice()
        if result is not None:
            close_mob(result)
    elif global_variables.is_dead:
        restart()
    elif current_mob == mobs_table.empty:
        summon_mob(random.choice(mobs_table.mobs))


def close_mob(result):
    global current_mob
    global current_option

    current_mob = mobs_table.empty
    render.current_mob = current_mob
    render.symbol_counter = 0
    render.central_text = result
    current_option = None


def summon_mob(mob):
    global current_mob
    global current_option

    current_mob = mob
    render.current_mob = current_mob
    render.symbol_counter = 0
    render.central_text = current_mob.text
    current_option = None


def die():
    global current_mob
    summon_mob(mobs_table.death_screen)
    global_variables.is_dead = True


if __name__ == '__main__':
    time = 0
    screen = pygame.display.set_mode(global_variables.size)
    clock = pygame.time.Clock()
    running = True
    in_title_screen = True
    current_mob = None

    summon_mob(random.choice(mobs_table.mobs))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    process_click()

        if current_mob != mobs_table.empty and render.symbol_counter > len(render.central_text):
            current_option = get_current_choice()

        screen.fill(pygame.Color('black'))
        if in_title_screen:
            render.render_title_screen(screen)
        else:
            render.update_screen(screen)

        delta_time = clock.tick(60) / 1000
        time += delta_time
    pygame.quit()
