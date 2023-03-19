import pygame as pg
import sys
from random import randrange as rnd

import levl1

DISPLAY = Win_Width, Win_Height = 800, 600
BG_Color = ((rnd(0,255)),(rnd(0,255)),(rnd(0,255)))

fps = 60

def main():
    pg.init()
    mw = pg.display.set_mode(DISPLAY)
    mw.fill(BG_Color)
    pg.display.set_caption('Mario')
    timer = pg.time.Clock() 

    g = True
    while g:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                g = False

        mw.fill(BG_Color)

        x=y=0

        for row in levl1.Level:
            for item in row:
                if item == '-':
                    pf = pg.Surface(levl1.Pl_Size)
                    pf.fill(levl1.Pl_Color)
                    mw.blit(pf,(x,y))
                x += levl1.Pl_Width
            y += levl1.Pl_Height
            x = 0

        pg.display.update()
        timer.tick(fps)

if __name__ == '__main__':
    main()















