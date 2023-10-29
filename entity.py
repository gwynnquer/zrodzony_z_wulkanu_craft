# external libraries
import pygame


class Entity(pygame.sprite.Sprite):
    DEFAULT_IMAGE_HEIGHT = 141
    DEFAULT_IMAGE_WIDTH = 100
    GRAVITY = 0.1

    def __init__(self, image, stats, gravity=False):

        self.str, self.dex, self.con = stats
        self.str_mod, self.str_dex, self.str_con = self.get_bonus(
            self.str), self.get_bonus(self.dex), self.get_bonus(self.con)

        self.gravity = gravity

        self.jump = self.str_mod + 1
        if self.jump <= 0:
            self.jump = 1.5

        self.ms = (30 + self.str_dex) / 30

        self.image = pygame.transform.smoothscale(
            pygame.image.load(image).convert_alpha(), (self.DEFAULT_IMAGE_WIDTH, self.DEFAULT_IMAGE_HEIGHT))
        self.rect = self.image.get_rect()

        super().__init__()

    def get_bonus(self, stat):
        return int((stat-10)/2)
