import pygame as pg 
import pyganim
import platforms as pf

SPEED = 7
PL_HEIGHT = 30
PL_WIDTH = 22
PL_COLOR = (200, 100, 100)
GRAVITY = 0.35
JUMP_POWER = 10

ANIMATION_RIGHT = [
    'mario/r1.png',
    'mario/r2.png',
    'mario/r3.png',
    'mario/r4.png',
    'mario/r5.png']
ANIMATION_LEFT = [
    'mario/l1.png',
    'mario/l2.png',
    'mario/l3.png',
    'mario/l4.png',
    'mario/l5.png']
ANIMATION_JUMP_RIGHT = [('mario/jr.png', 4)]
ANIMATION_JUMP_LEFT = [('mario/jl.png', 4)]
ANIMATION_JUMP = [('mario/j.png', 4)]
ANIMATION_STAY = [('mario/0.png', 4)]
ANIMATION_DELAY = 4


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.onGround = False
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = pg.transform.scale(pg.image.load('img/mario.png'), (PL_WIDTH, PL_HEIGHT))
        self.rect = pg.Rect(x, y, PL_WIDTH, PL_HEIGHT)

        self.image.set_colorkey((0,0,0,0))

        anim = []
        for a in ANIMATION_RIGHT:
            anim.append((a, ANIMATION_DELAY))
        self.AnimRight = pyganim.PygAnimation(anim)
        self.AnimRight.play()

        anim = []
        for a in ANIMATION_LEFT:
            anim.append((a, ANIMATION_DELAY))
        self.AnimLeft = pyganim.PygAnimation(anim)
        self.AnimLeft.play()

        self.AnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.AnimStay.play()
        self.AnimStay.blit(self.image, (0,0))

        self.AnimJumpL = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.AnimJumpL.play()

        self.AnimJumpR = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.AnimJumpR.play()

        self.AnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.AnimJump.play()

    def update(self, left: bool, right: bool, up: bool, platforms):
        
        if up: 
            if self.onGround: 
                self.yvel = -JUMP_POWER
            # self.image.fill((0,0,0,0))
            # self.AnimJump.blit(self.image, (0,0)) 

        if left: 
            self.xvel = -SPEED
            self.image.fill((0,0,0,0))
            # if up or not self.onGround:
            #     self.AnimJumpL.blit(self.image, (0,0))
            # else:
            self.AnimLeft.blit(self.image, (0,0))

        if right: 
            self.xvel = SPEED
            self.image.fill((0,0,0,0))
            # if up or not self.onGround:
            #     self.AnimJumpR.blit(self.image, (0,0))
            # else:
            self.AnimRight.blit(self.image, (0,0))

        if not(left or right): 
            self.xvel = 0
            if not up:
                pass
                # self.image.fill((0,0,0,0))
                # self.AnimStay.blit(self.image, (0,0))

        if not self.onGround: 
            self.yvel += GRAVITY

        if self.yvel < 0:
            self.image.fill((0,0,0,0))
            self.AnimJump.blit(self.image, (0,0))
        if self.yvel < 0 and self.xvel < 0:
            self.image.fill((0,0,0,0))
            self.AnimJumpL.blit(self.image, (0,0))
        if self.yvel < 0 and self.xvel > 0:
            self.image.fill((0,0,0,0))
            self.AnimJumpR.blit(self.image, (0,0))

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