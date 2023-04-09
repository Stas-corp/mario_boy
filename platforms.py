import pygame as pg

PF_WIDTH = 32
PF_HEIGHT = 32
PF_COLOR = (200, 100, 255)

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('img/block.png'), (PF_WIDTH, PF_HEIGHT))
        self.rect = pg.Rect(x, y, PF_WIDTH, PF_HEIGHT)