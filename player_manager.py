# own libraries
import display_manager
import entity

# external libraries
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

        super().__init__(
            image=self.PLAYERS[player_name]['image'],
            stats=self.PLAYERS[player_name]['stats'],
            gravity=True,
        )

        self.left_pressed, self.right_pressed, self.jumping = False, False, False

    # przypisanie akcji gracza do działania
    def get_actions(self, actions):
        # akcje ruchu

        self.left_pressed = actions['left']
        self.right_pressed = actions['right']
        self.jumping = actions['up']

        self.update_movement()

    # ruch gracza
    def update_movement(self, ):
        self.vel_x = 0
        self.vel_y = 0

        if self.left_pressed and not self.right_pressed:
            self.vel_x = -self.ms
        if self.right_pressed and not self.left_pressed:
            self.vel_x = self.ms
        if self.jumping and self.rect.bottom == display_manager.GameWindowSettings.WINDOW_HEIGHT:
            self.vel_y = -self.jump
            self.jumping = False

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
