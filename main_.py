import pygame as pg
from random import randrange as rnd

import level
import player
import platforms

DISPLAY = WIN_WIDTH, WIN_HEIGHT = 800, 600
BG_COLOR = ((rnd(0,255)),(rnd(0,255)),(rnd(0,255)))

fps = 60

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
        entities.draw(mw)

        pg.display.update()
        timer.tick(fps)

if __name__ == '__main__':
    main()















