import pygame
import global_variables


class Choice:
    def __init__(self, text, end_text, affect_on_karma, items_required=()):
        self.text = text
        self.end_text = end_text
        self.karma = affect_on_karma
        self.items_required = items_required

    def perform_choice(self):
        try:
            for item in self.items_required:
                global_variables.inventory.remove(item)
            global_variables.karma += self.karma
        except:
            return None
        return self.end_text


class Mob:
    def __init__(self, text, texture, choice_list, atk=0):
        self.text = text
        self.texture = pygame.transform.scale(texture, (texture.get_width() * 3, texture.get_height() * 3))
        self.choice_list = choice_list
        self.atk = atk

    def add_choice(self, choice):
        self.choice_list.append(choice)


empty = Mob("", pygame.Surface((1, 1)), [])
empty.texture.set_alpha(0)

spider_choices = [
    Choice('Дать ЖУКА (необходим ЖУК)',
           "ПАУК не умеет говорить, но Вы видите, что он благодарен",
           -30,
           ("ЖУК",)),
    Choice("Не давать ЖУКА",
           "Судя по всему, ПАУК недоволен",
           10),
    Choice('Съесть ЖУКА на его глазах (необходим ЖУК)',
           "Какой ужас...",
           -45,
           ('ЖУК',))
                  ]
spider = Mob('Пред Вами предстал ПАУК. Он просит у Вас ЖУКА. Что будете делать?',
             pygame.image.load('data/textures/spider.png'), spider_choices)

'''
print(spider.text)
for choice in enumerate(spider.choice_list):
    print(choice[0] + 1, choice[1].text)
choice = int(input())
print(spider.choice_list[choice - 1].end_text)'''
