# own libraries
import display_manager

# external libraries
import pygame


class Menu():

    WINDOW_WIDTH = display_manager.GameWindowSettings.WINDOW_WIDTH
    WINDOW_HEIGHT = display_manager.GameWindowSettings.WINDOW_HEIGHT

    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

        # początkowy kursor na starcie
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.exitx, self.exity = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def main_display(self):
        self.run_display = True
        while self.run_display:
            self.game.get_events()
            self.check_input()
            self.game.display.fill((120, 120, 120))
            self.game.draw_text(
                'Main Menu', 20, self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 20)
            self.game.draw_text('Start Game', 200, self.startx, self.starty)
            self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
            self.game.draw_text('Exit', 20, self.exitx, self.exity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):

        # ruch kursora, jak jest na statusie A i nacisniesz DOWN to idzie do B
        if self.actions['down']:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset,
                                           self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset,
                                           self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset,
                                           self.starty)
                self.state = 'Start'

    def check_input(self):
        if self.game.actions['start']:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                pass
            elif self.state == 'Credits':
                pass
            elif self.state == 'Exit':
                self.game.playing = False
                self.game.running = False

            self.run_display = False
