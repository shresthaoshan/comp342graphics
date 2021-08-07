from typing import Tuple
import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

Coordinate = Tuple[int, int]

def bresenham(startCoordinate: Coordinate,endCoordinate: Coordinate):
    x1, y1 = startCoordinate
    x2, y2 = endCoordinate

    m  = abs((y2 - y1)/(x2 - x1))
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    coordinates : list[Coordinate] = []
    
    if m < 1:
        for i in range(0, dx):
            p = 2 * dy - dx
            x = x + 1
            if p < 0:
                coordinates.append((x, y))
                p = p + 2 * dy
            else:
                y = y + 1
                coordinates.append((x, y))
                p = p + 2 * (dy - dx)
    else:
        for i in range(0, dy):
            p = 2 *dx - dy
            y = y + 1
            if p < 0:
                coordinates.append((x, y))
                p = p + 2 * dx
            else:
                x = x + 1
                coordinates.append((x, y))
                p = p + 2 * (dx - dy)
    return coordinates


def drawBSA():
    coordinates = bresenham((-1,0),(3,2))
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,1.0)
    for v in coordinates:
        x,y = v
        glVertex2f(x, y)
    glEnd()

def main():
    pg.init()
    display.set_mode((400, 400), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("BSA - COMP343 Computer Graphics Lab")

    gluPerspective(40, 1, 1, 10)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        drawBSA()
        display.flip()

main()