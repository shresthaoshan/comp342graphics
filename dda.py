from typing import Tuple
import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def DDA(start_coordinate: Tuple[int, int], end_coordinate: Tuple[int, int]):
    x1, y1 = start_coordinate
    x2, y2 = end_coordinate

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    steps = max(dx, dy)

    Xinc = dx / steps
    Yinc = dy / steps

    X = x1
    Y = y1
    vertices : list[tuple[float, float]] = []
    for i in range(steps):
        vertices.append((X, Y))
        X = X + Xinc
        Y = Y + Yinc
    return vertices

def drawDDA():
    vertices = DDA((1,1), (20,40))
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0,0.0,1.0)
    for v in vertices:
        x,y = v
        glVertex2f(x, y)
    glEnd()

def main():
    pg.init()
    display.set_mode((400, 400), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("DDA - COMP343 Computer Graphics Lab")

    gluPerspective(200, 1, 1, 10)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        drawDDA()
        display.flip()

main()