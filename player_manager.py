import pygame


class MainPlayer():

    PLAYERS = {
        'kwiat': {
            'image': r'01.ASSETS\graphics\characters\kwiat.png',
        },
        'dasher': {
            'image': r'01.ASSETS\graphics\characters\dasher.png',
        },
    }

    def __init__(self, player_name):

        self.player = self.PLAYERS[player_name]
        self.image = pygame.image.load(self.player['image']).convert_alpha()
