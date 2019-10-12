
import pygame as pg
from pygame.locals import *
from sys import exit
pg.init()
screen=pg.display.set_mode((500,500),0,32)
screen.fill((0,0,0))

BoardImage=pg.image.load("Board.png")
BoardRect=BoardImage.get_rect()
while 1:
    screen.blit(BackgroundImage,Boardrect,Boardrect)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit()
    pg.display.update()