import pygame as pg
import random
from settings import *

class Platforms:
    def __init__(self, game):
        self.game = game
        self.platforms = []
        self.counterUntilNew = HEIGHT

        for _ in range(20):
            platformX = random.randint(0, WIDTH-PLATFORM_WIDTH)
            platformY = random.randint(0, HEIGHT-PLATFORM_HEIGHT)
            platform = pg.Rect(platformX, platformY, PLATFORM_WIDTH, PLATFORM_HEIGHT)

            self.platforms.append(platform)
        for _ in range(20):
            platformX = random.randint(0, WIDTH-PLATFORM_WIDTH)
            platformY = random.randint(-HEIGHT, 0)
            platform = pg.Rect(platformX, platformY, PLATFORM_WIDTH, PLATFORM_HEIGHT)

            self.platforms.append(platform)


    def generate_new(self):
        for _ in range(20):
            platformX = random.randint(0, WIDTH-PLATFORM_WIDTH)
            platformY = random.randint(-HEIGHT, 0)
            platform = pg.Rect(platformX, platformY, PLATFORM_WIDTH, PLATFORM_HEIGHT)

            self.platforms.append(platform)
        self.platforms = self.platforms[20:]

    def lower(self, y_vel):
        self.counterUntilNew += y_vel
        for platform in self.platforms:
            platform.y -= y_vel

        if self.counterUntilNew <= 0:
            self.generate_new()
            self.counterUntilNew = HEIGHT

    def movement(self):
        return

    def draw(self):
        for platform in self.platforms:
            pg.draw.rect(self.game.screen, "white", platform)

    def update(self):
        self.movement()