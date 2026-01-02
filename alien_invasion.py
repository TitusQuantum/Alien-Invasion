import sys
import pygame as pg

class AlienInvasion:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1200,800))
        pg.display.set_caption("Alien Invasion")

    def run_game(self):

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()
            pg.display.flip() # Make the most recently drawn screen visible.


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()