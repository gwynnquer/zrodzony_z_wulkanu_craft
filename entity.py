import pygame


class Entity():

    def __init__(self, stats):

        self.str, self.dex, self.con = stats

        self.ms = 30 + self.get_bonus(self.dex)

    def get_bonus(self, stat):
        return int((stat-10)/2)
