from constants import *

class GameObject(pygame.sprite.Sprite):
    def __init__(self, game, position, velocity, dimensions):
        super().__init__()
        self.position = position
        self.game = game
        self.velocity = velocity
        self.dimensions = dimensions

    def draw(self):
        pass

    def update(self):
        pass

    def delete(self):
        self.game.gameObjects.remove(self)

    def getType(self):
        pass

    def collidesWith(self, other):
        return pygame.sprite.collide_mask(self, other)