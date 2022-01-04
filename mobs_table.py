import player_stats


class Choice:
    def __init__(self, text, affect_on_karma, items_required=None):
        self.text = text
        self.karma = affect_on_karma
        self.items_required = items_required

    def perform_choice(self):
        for item in self.items_required:
            player_stats.inventory.remove(item)
        player_stats.karma += self.karma


class Mob:
    def __init__(self, texture, choice_list, atk):
        self.texture = texture
        self.choice_list = choice_list
        self.atk = atk

    def add_choice(self, choice):
        self.choice_list.append(choice)
