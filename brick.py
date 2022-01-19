#Credits Andrei Tulpan, Irina Nita, Sebastian Severin 2022

from gameObject import GameObject
from constants import *

class Brick(GameObject):
    def __init__(self, game, position, dimensions, hits):
        super().__init__(game, position, [0, 0], dimensions)
        self.image = BRICK1
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.hits = hits
        self.type = hits

    def update(self):
        if (self.hits == 1):
            self.image = BRICK2
        elif (self.hits == 2):
            self.image = BRICK3
        elif (self.hits == 3):
            if (self.type) == 0:
                self.game.score += 50
            elif (self.type == 1):
                self.game.score += 30
            elif (self.type == 2):
                self.game.score += 10
            self.game.gameObjects.remove(self)
            self.game.bricks.remove(self)
            self.game.spawn_coin(self.rect.x, self.rect.y)

    def getType(self):
        return "brick"