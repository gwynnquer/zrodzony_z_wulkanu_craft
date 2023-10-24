# own libraries
import display_manager
import city
import player_manager

# external libraries
import pygame
import time


class Game():
    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        self.running, self.playing = True, True
        self.dt, self.prev_time = 0, 0

        self.state_stack = []

        # odwołanie sie do display_manager.py i inicjacja wszystkich ustawień okna
        self.screen = display_manager.GameWindowSettings().screen
        self.player = player_manager.MainPlayer('kwiat')
        self.khorinis = city.Khorinis()

        self.actions = {"left": False, "right": False, "up": False,
                        "down": False, "action1": False, "action2": False, "start": False}

        # zapewne tymczasowe wrzucenie khorinis do kolejki, potem bedzie tutja wiecej

        self.state_stack.append(self.khorinis)

    def game_loop(self):

        # głowna pętla gry
        while self.playing:
            # zmiana czasu, nie wiem jeszcze po co ale sie przyda
            self.get_dt()
            # zebranie wszystkich evenetów
            self.get_events()
            # update to co sie dzieje na screenie
            self.update()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def get_events(self):

        for event in pygame.event.get():
            # wyłączenie gry
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

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

    def update(self):

        # .image state_stacku, którym np. jest khorinis
        self.screen.blit(self.state_stack[-1].image, (0, 0))

        # rozpoznanie akcji i zmienienie pozycji
        self.player.get_actions(self.actions)

        # blit gracza
        self.screen.blit(self.player.image, self.player.rect)

        # update okna
        pygame.display.update()

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False


if __name__ == "__main__":

    game = Game()
    while game.running:
        game.game_loop()

    pygame.quit()
    exit()
