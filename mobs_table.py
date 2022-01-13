import pygame
import global_variables


class Choice:
    def __init__(self, text, end_text, affect_on_karma, items_required=(), items_acquired=(), is_fighting=False):
        self.text = text
        self.end_text = end_text
        self.karma = affect_on_karma
        self.items_required = items_required
        self.items_acquired = items_acquired
        self.is_fighting = is_fighting

    def perform_choice(self):
        try:
            for item in self.items_required:
                global_variables.inventory.remove(item)
            for item in self.items_acquired:
                global_variables.inventory.append(item)
            global_variables.karma += self.karma
        except:
            return None
        return self.end_text


class Mob:
    def __init__(self, text, texture, choice_list, atk=0, karma_required=0):
        self.text = text
        self.texture = pygame.transform.scale(texture, (texture.get_width() * 3, texture.get_height() * 3))
        self.choice_list = choice_list
        self.atk = atk
        self.karma = karma_required

    def add_choice(self, choice):
        self.choice_list.append(choice)

    def can_spawn(self):
        if self.karma > 0:
            return global_variables.karma >= self.karma
        elif self.karma < 0:
            return global_variables.karma <= self.karma
        return True


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

beetle_choices = [
    Choice('Дать ЖУКУ ФРУКТ (необходим ФРУКТ)',
           "ЖУК благодарит Вас и присоединяется к Вам.",
           20,
           ("ФРУКТ",),
           ("ЖУК",)),
    Choice("Не давать ФРУКТ",
           "ЖУК выглядит печально.",
           -10)
]
beetle = Mob('Вы повстречали ЖУКА. Кажется, он хочет ФРУКТ.',
             pygame.image.load('data/textures/beetle.png'), beetle_choices)

well_choices = [
    Choice('Взять ведро ВОДЫ',
           "Вы получили ведро воды",
           0,
           items_acquired=("ВОДА",)),
    Choice("Не брать ведро ВОДЫ",
           "Вы молча уходите",
           0)
]
well = Mob("Вы наткунлись на колодец. Что сделаете?",
           pygame.image.load('data/textures/well.png'), well_choices)

tree_choices = [
    Choice("Полить дерево (необходима ВОДА)",
           "Внезапно дерево начало цвести и плодоносить.\n Вы забираете его ФРУКТ.",
           10,
           ('ВОДА',),
           ("ФРУКТ",)),
    Choice("Ничего не делать",
           "Вы молча уходите.",
           0)
]
tree = Mob('Вы увидели ДЕРЕВО. Что будуте делать?',
           pygame.image.load('data/textures/tree.png'), tree_choices)

thirsty_man_choices = [
    Choice('Дать ВОДЫ (необходима ВОДА)',
           "Он благодарит Вас и даёт Вам ЗОЛОТО",
           30,
           ("ВОДА",),
           ("ЗОЛОТО",)),
    Choice("Не давать ВОДЫ",
           "Человек проклинает Вас",
           -10)
]
thirsty_man = Mob('Вы повстречали человека, что невероятно желает ВОДЫ.\n'
                  'Что будете делать?',
                  pygame.image.load('data/textures/human.png'), thirsty_man_choices, karma_required=10)

trader_choices = [
    Choice("Купить МЕЧ (необходимо ЗОЛОТО)",
           "Вы приобрели МЕЧ", 0,
           ("ЗОЛОТО",), ("МЕЧ",)),
    Choice("Купить ВОДУ (2 шт) (необходимо ЗОЛОТО)",
           "Вы приобрели ВОДУ", 0,
           ("ЗОЛОТО",), ("ВОДА", "ВОДА")),
    Choice("Купить ФРУКТ (2 шт) (необходимо ЗОЛОТО)",
           "Вы приобрели ФРУКТ", 0,
           ("ЗОЛОТО",), ("ФРУКТ", "ФРУКТ")),
    Choice("Купить ЖУКА (необходимо ЗОЛОТО)",
           "Вы приобрели ЖУКА", 0,
           ("ЗОЛОТО",), ("ЖУК",)),
]
trader = Mob('Вы замечаете торговца', pygame.image.load('data/textures/trader.png'),
             trader_choices, karma_required=30)

dead_choices = [
    Choice('Начать заново',
           "Вы отказываетесь идти у смерти на поводу\nи просыпаетесь в начале своего пути.", 0)
]
death_screen = Mob("Вы умерли", empty.texture, dead_choices)

'''
print(spider.text)
for choice in enumerate(spider.choice_list):
    print(choice[0] + 1, choice[1].text)
choice = int(input())
print(spider.choice_list[choice - 1].end_text)'''
mobs = [spider, beetle, well, tree, thirsty_man, trader]
