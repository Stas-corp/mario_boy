import pygame as pg 
import platforms as pf
SPEED = 7

PL_HEIGHT = 30
PL_WIDTH = 22
PL_COLOR = (200, 100, 100)
GRAVITY = 0.35
JUMP_POWER = 10

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.onGround = False
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = pg.Surface((PL_WIDTH, PL_HEIGHT))
        self.image.fill(PL_COLOR)
        self.rect = pg.Rect(x, y, PL_WIDTH, PL_HEIGHT)

    def update(self, left: bool, right: bool, up: bool, platforms):
        if up: 
            if self.onGround: self.yvel = -JUMP_POWER

        if left: self.xvel = -SPEED
        if right: self.xvel = SPEED

        if not(left or right): self.xvel = 0

        if not self.onGround: self.yvel += GRAVITY

        self.onGround = False

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms: list):
        for p in platforms:
            if pg.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0: 
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
