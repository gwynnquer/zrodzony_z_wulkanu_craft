# own libraries
import entity

# public libraries
import pygame


class MainPlayer(entity.Entity):

    PLAYERS = {
        'kwiat': {
            'image': r'01.ASSETS\graphics\characters\kwiat.png',
            'stats': (12, 20, 16),
        },
        'dasher': {
            'image': r'01.ASSETS\graphics\characters\dasher.png',
            'stats': (12, 14, 18),
        },
    }

    def __init__(self, player_name):

        self.player = self.PLAYERS[player_name]

        print(self.player['stats'])
        self.stats = super().__init__(stats=self.player['stats'])

        print(self.stats)

        self.load = pygame.image.load(self.player['image']).convert_alpha()

        player_height, player_width = self.load.get_size()

        self.image = pygame.transform.smoothscale(
            self.load,
            (player_height/12, player_width/12)
        )

        self.rect = self.image.get_rect()

    def moving(self, event):

        if event.type == pygame.KEYDOWN:
            print(event)
            if event.key == ord('a'):
                self.rect.x -= self.stats.ms
                print(self.rect.x)
            if event.key == ord('d'):
                self.rect.x += self.stats.ms

        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                self.rect.x -= self.stats.ms
            if event.key == ord('b'):
                self.rect.x += self.stats.ms
