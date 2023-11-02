# own libraries
import display_manager
import city
import menu
import player_manager

# external libraries
import pygame
import time


class Game():

    BLACK, WHITE = (0, 0, 0), (255, 255, 255)

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        self.running, self.playing = True, True
        self.dt, self.prev_time = 0, 0

        self.state_stack = []

        # odwołanie sie do display_manager.py i inicjacja wszystkich ustawień okna
        self.display_manager = display_manager.GameWindowSettings()
        self.screen = self.display_manager.screen
        self.display = self.display_manager.display

        # wywołanie gracza
        # self.player = player_manager.MainPlayer('kwiat')

        self.actions = {"left": False, "right": False, "up": False,
                        "down": False, "action1": False, "action2": False, "start": False}

        # wrzucenie menu na początek stacka

        self.main_menu = menu.MainMenu(self)

        self.state_stack.append(self.main_menu)

    def game_loop(self):

        # głowna pętla gry
        while self.playing:

            # zmiana strategii, każdys state ma swój main_display
            self.state_stack[-1].main_display()

            print(2)

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def get_events(self):

        for event in pygame.event.get():
            # wyłączenie gry
            if event.type == pygame.QUIT:
                self.playing, self.running = False, False
                self.main_menu.run_display = False

            # klawiatura 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_w:
                    self.actions['up'] = True
                if event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_p:
                    self.actions['action1'] = True
                if event.key == pygame.K_o:
                    self.actions['action2'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True

            # klawiatura 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_w:
                    self.actions['up'] = False
                if event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_p:
                    self.actions['action1'] = False
                if event.key == pygame.K_o:
                    self.actions['action2'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False

            # ruch gracza

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def draw_text(self, text, size, x, y):
        # funckja do rysowania tekstu
        font = pygame.font.Font(self.display_manager.FONT, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
