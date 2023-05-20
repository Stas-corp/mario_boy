import pygame as pg
from random import randrange as rnd

import level
import player
import platforms

DISPLAY = WIN_WIDTH, WIN_HEIGHT = 800, 600
BG_COLOR = ((rnd(0,255)),(rnd(0,255)),(rnd(0,255)))
FPS = 60

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pg.Rect(0,0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_config(camera, target_rect):
    x, y, _, _ = target_rect
    _, _, w, h = camera
    x = -x + WIN_WIDTH / 2
    y = -y + WIN_HEIGHT / 2

    x = min(0, x)
    x = max(-(camera.width - WIN_WIDTH), x)
    y = max(-(camera.height - WIN_HEIGHT), y)
    y = min(0, y)

    return pg.Rect(x, y, w, h)

def main():
    pg.init()
    mw = pg.display.set_mode(DISPLAY)
    mw.fill(BG_COLOR)
    pg.display.set_caption('Mario')
    timer = pg.time.Clock() 

    pl = player.Player(50, 50)

    left = right = up = False
    entities = pg.sprite.Group()
    platforms_list = []
    entities.add(pl)

    x=y=0
    for row in level.level:
        for item in row:
            if item == '-':
                pf = platforms.Platform(x, y)
                entities.add(pf)
                platforms_list.append(pf)
            x += level.PF_WIDTH
        y += level.PF_HEIGHT
        x = 0

    level_width = len(level.level[0]) * level.PF_WIDTH
    level_height = len(level.level) * level.PF_HEIGHT
    camera = Camera(camera_config, level_width, level_height)

    game = True
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a: left = True
                if event.key == pg.K_d: right = True
                if event.key == pg.K_SPACE: up = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_a: left = False
                if event.key == pg.K_d: right = False
                if event.key == pg.K_SPACE: up = False

        mw.fill(BG_COLOR)

        pl.update(left, right, up, platforms_list)
        camera.update(pl)
        
        for e in entities:
            mw.blit(e.image, camera.apply(e))

        pg.display.update()
        timer.tick(FPS)

if __name__ == '__main__':
    main()