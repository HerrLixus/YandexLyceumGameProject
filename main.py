import pygame
import random

import render
import mobs_table
import global_variables

pygame.init()
pygame.font.init()
pygame.mixer.music.set_volume(0.75)


def restart():
    global_variables.inventory.clear()
    global_variables.atk = 1
    global_variables.karma = 0
    global_variables.is_dead = False
    spawn_new_mob()


def get_current_choice():
    for i, rect in enumerate(global_variables.option_hitboxes):
        if rect.collidepoint(pygame.mouse.get_pos()):
            return current_mob.choice_list[i]
    return None


def update_atk():
    weapons = {"МЕЧ": 5, "СУПЕР МЕЧ": 10, "ДЕМОНИЧЕСКИЙ МЕЧ": 100}
    global_variables.atk = sum([weapons[item] for item in global_variables.inventory
                                if item in weapons]) + 1


def process_click():
    global in_title_screen
    if in_title_screen:
        pygame.mixer.music.pause()
        pygame.mixer.music.load('data/music/Kevin MacLeod - 8bit Dungeon Level.mp3')
        pygame.mixer.music.play(-1)
        in_title_screen = False
    elif render.symbol_counter < len(render.central_text):
        render.symbol_counter = len(render.central_text)
    elif current_option is not None:
        if current_option.is_fighting:
            if global_variables.atk < current_mob.atk:
                die()
                return
        update_atk()
        result = current_option.perform_choice()
        if result is not None:
            close_mob(result)
    elif global_variables.is_dead:
        restart()
    elif current_mob == mobs_table.empty:
        spawn_new_mob()


def close_mob(result):
    global current_mob
    global previous_mob
    global current_option

    previous_mob = current_mob
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


def find_possible_mobs():
    possibilities = [mob for mob in mobs_table.mobs if mob.can_spawn()]
    if previous_mob in possibilities:
        possibilities.remove(previous_mob)
    return possibilities


def spawn_new_mob():
    summon_mob(random.choice(find_possible_mobs()))


if __name__ == '__main__':
    time = 0
    screen = pygame.display.set_mode(global_variables.size)
    clock = pygame.time.Clock()
    running = True
    in_title_screen = True
    previous_mob = None
    current_mob = None

    pygame.mixer.music.load('data/music/Joshua McLean - Mountain Trials.mp3')
    pygame.mixer.music.play(-1)

    spawn_new_mob()

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
