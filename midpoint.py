from typing import Tuple
import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

Coordinate = Tuple[int, int]

def midpoint(start_coordinate: Coordinate, end_coordinate: Coordinate):
    x1, y1 = start_coordinate
    x2, y2 = end_coordinate
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    coordinates: list[Coordinate] = []

    if dy <= dx:
        d = dy - dx/2
        x, y = x1, y1
        
        coordinates.append((x, y))

        while x < x2:
            x  = x + 1

            if d < 0:
                d = d + dy
            else:
                d = d + dy - dx
                y = y + 1
            coordinates.append((x, y))
    elif dx <= dy:
        d = dx - dy/2
        x, y = x1, y1

        coordinates.append((x, y))

        while y < y2:
            y  = y + 1

            if d < 0:
                d = d + dx
            else:
                d = d + dx - dy
                x = x + 1
            coordinates.append((x, y))

    return coordinates


def drawMidPoint():
    vertices = midpoint((-1,-1), (2,2))
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,1.0)
    for v in vertices:
        x,y = v
        glVertex2f(x, y)
    glEnd()

def main():
    pg.init()
    display.set_mode((400, 400), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("MidPoint - COMP343 Computer Graphics Lab")

    gluPerspective(40, 1, 1, 10)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        drawMidPoint()
        display.flip()

main()