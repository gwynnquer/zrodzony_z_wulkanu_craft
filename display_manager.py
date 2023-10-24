import pygame


class GameWindowSettings():

    WINDOW_HEIGHT = 720
    WINDOW_WIDTH = 1280
    GAME_NAME = 'ZRODZONY Z WULKANU (Craft)'
    ICON = r'01.ASSETS\graphics\icon.png'
    FONT = r'01.ASSETS\font\Tickerbit-mono.otf'

    def __init__(self):

        self.set_screen(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.set_game_name(self.GAME_NAME)
        self.set_icon(self.ICON)
        self.set_font(self.FONT)

    def set_screen(self, height, width):
        self.screen = pygame.display.set_mode((height, width))

    def set_game_name(self, game_name):
        pygame.display.set_caption(game_name)

    def set_icon(self, icon):
        icon = pygame.image.load(icon).convert()
        icon = pygame.transform.smoothscale(icon, (32, 32))
        pygame.display.set_icon(icon)

    def set_font(self, font):
        pygame.font.Font(font, 20)
