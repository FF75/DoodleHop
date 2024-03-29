import pygame as pg
import sys
import time
from player import *
from platforms import *
from settings import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.new_game()
        self.clock = pg.time.Clock()

    def new_game(self):
        self.player = Player(self)
        self.platforms = Platforms(self)

    def update(self):
        self.player.update()
        self.platforms.update()

    def draw(self):
        self.screen.fill("beige")
        self.player.draw()
        self.platforms.draw()
        pg.display.flip()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
           
    def run(self):
        while True:
            self.clock.tick(30)
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()