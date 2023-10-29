# own libraries
import game

# external libraries
import pygame


if __name__ == "__main__":

    game = game.Game()
    while game.running:
        game.game_loop()

    pygame.quit()
    exit()
