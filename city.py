# own libraries
import display_manager

# external libraries
import os
import pygame


class Khorinis(pygame.sprite.Sprite):

    # mapa miasta

    IMAGE_PATH = r'01.ASSETS\graphics\lokacje'
    KHORINIS_IMAGES = [
        r'brama.png',
        r'kurt.png',
        r'targ.png',
        r'gailen.png',
        r'gildia.png',
        r'kuznia.png',
        r'straz.png',
        r'mlyn.png'
    ]

    # parametry
    WINDOW_HEIGHT = display_manager.GameWindowSettings.WINDOW_HEIGHT
    WINDOW_WIDTH = display_manager.GameWindowSettings.WINDOW_WIDTH

    def __init__(self, index=4):

        super().__init__()
        self.set_img(index)

    def set_img(self, image_index):

        # ustawienie mapy bazując na numerze indeksu
        self.image_path = os.path.join(
            self.IMAGE_PATH, self.KHORINIS_IMAGES[image_index])
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        self.rect = self.image.get_rect(topleft=(0, 0))
