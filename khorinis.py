# own libraries
import display_manager

# external libraries
import pygame


class Khorinis(pygame.sprite.Sprite):

    # mapa miasta
    KHORINIS_IMAGES = [
        r'graphics\lokacje\brama.png',
        r'graphics\lokacje\kurt.png',
        r'graphics\lokacje\targ.png',
        r'graphics\lokacje\gailen.png',
        r'graphics\lokacje\gildia.png',
        r'graphics\lokacje\kuznia.png',
        r'graphics\lokacje\straz.png',
        r'graphics\lokacje\mlyn.png'
    ]

    # parametry
    WINDOW_HEIGHT = display_manager.GameWindowSettings.WINDOW_HEIGHT
    WINDOW_WIDTH = display_manager.GameWindowSettings.WINDOW_WIDTH

    def __init__(self, index=4):

        super().__init__()
        self.set_img(index)

    def set_img(self, index):

        # ustawienie mapy bazując na numerze indeksu
        self.check_index = index
        self.image = pygame.image.load(
            self.KHORINIS_IMAGES[index]).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        self.rect = self.transform.get_rect(topleft=(0, 0))
