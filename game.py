# own libraries
import display_manager
import player_manager

# external libraries
import pygame


class Game():
    def __init__(self):

        pygame.init()
        self.playing = True
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        # odwołanie sie do display_manager.py i inicjacja wszystkich ustawień okna
        self.screen = display_manager.GameWindowSettings().screen
        self.player = player_manager.MainPlayer('kwiat')

        self.screen.blit(self.player.image, self.player.rect)

    def loop(self):

        # głowna pętla gry
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                exit()

            # ruch gracza
            self.player.moving(event)

        # update
        pygame.display.update()


if __name__ == "__main__":

    game = Game()
    while game.playing:
        game.loop()
