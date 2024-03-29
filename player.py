import pygame as pg
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.y_vel = 5
        self.player = pg.Rect(250-(PLAYER_WIDTH/2), 350-(PLAYER_HEIGHT/2), PLAYER_WIDTH, PLAYER_HEIGHT)

    def xMovement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.player.x - PLAYER_XVEL >= 0:
            self.player.x -= PLAYER_XVEL
        if keys[pg.K_RIGHT] and self.player.x + PLAYER_XVEL + self.player.width <= WIDTH:
            self.player.x += PLAYER_XVEL

    def yMovement(self):
        if self.y_vel >= 0:
            for platform in self.game.platforms.platforms:
                if platform.y + platform.height >= self.player.y and platform.colliderect(self.player):
                    self.y_vel = -40
                    #self.game.platforms.generate_new(self.y_vel)
        if self.y_vel < 0 and self.player.y < HEIGHT/2:
            self.game.platforms.lower(self.y_vel)
        else:
            self.player.y += self.y_vel
        self.y_vel += 3

    def movement(self):
        #self.y += 5
        #self.player.y = self.y
        self.yMovement()

        self.xMovement()

    def draw(self):
        pg.draw.rect(self.game.screen, "green", self.player)

    def update(self):
        self.movement()