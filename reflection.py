import numpy as np
from typing import Tuple

import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

Coordinate = Tuple[float, float]

def reflectX(point: Coordinate) -> Coordinate:
    x, y = point
    m = ([x], [y], [1])
    tx_m = ([1, 0, 0], [0, -1, 0], [0, 0, 1])
    xT, yT, _ = np.dot(tx_m, m)
    return (xT[0], yT[0])

def reflectY(point: Coordinate) -> Coordinate:
    x, y = point
    m = ([x], [y], [1])
    tx_m = ([-1, 0, 0], [0, 1, 0], [0, 0, 1])
    xT, yT, _ = np.dot(tx_m, m)
    return (xT[0], yT[0])

def displayPaint():
    st_point: Coordinate = (-4,-6)
    end_point: Coordinate = (7,3)
    stX_tps = reflectX(st_point)
    endX_tps = reflectX(end_point)
    stY_tps = reflectY(st_point)
    endY_tps = reflectY(end_point)
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(st_point[0], st_point[1])
    glVertex2f(end_point[0], end_point[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(stX_tps[0], stX_tps[1])
    glVertex2f(endX_tps[0], endX_tps[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0,0.0,1.0)
    glVertex2f(stY_tps[0], stY_tps[1])
    glVertex2f(endY_tps[0], endY_tps[1])
    glEnd()

def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("Translate - COMP343 Computer Graphics Lab")

    gluPerspective(150, 1, 1, 10)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        displayPaint()
        display.flip()

main()