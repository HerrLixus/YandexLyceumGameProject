import pygame
import render
import mobs_table
import global_variables

pygame.init()


def get_current_choice():
    for i, rect in enumerate(global_variables.option_hitboxes):
        if rect.collidepoint(pygame.mouse.get_pos()):
            return current_mob.choice_list[i]
    return None


if __name__ == '__main__':
    time = 0
    screen = pygame.display.set_mode(global_variables.size)
    clock = pygame.time.Clock()
    running = True

    current_mob = mobs_table.spider
    render.current_mob = current_mob
    render.central_text = current_mob.text
    current_option = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and current_option is not None:
                    result = current_option.perform_choice()
                    if result is not None:
                        current_mob = mobs_table.empty
                        render.current_mob = current_mob
                        render.symbol_counter = 0
                        render.central_text = result

        if current_mob != mobs_table.empty:
            current_option = get_current_choice()
        render.update_screen(screen)

        delta_time = clock.tick(60) / 1000
        time += delta_time
    pygame.quit()
