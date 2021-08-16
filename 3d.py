from typing import Tuple
import pygame as pg
from pygame import display, event
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

# Defining x_max, y_max and x_min, y_min for rectangle
# Since diagonal points are enough to define a rectangle
x_max = 300.0
y_max = 300.0
x_min = -300.0
y_min = -300.0

Coordinate = Tuple[float, float, float]
ColorRGB = Tuple[float, float, float]

def drawLine(point1: Coordinate, point2: Coordinate, color: ColorRGB = (1.0, 1.0, 1.0)):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    r, g, b = color
    glBegin(GL_LINE_STRIP)
    glColor3f(r,g,b)
    glVertex3d(x1,y1,z1)
    glVertex3d(x2,y2,z2)
    glEnd()

def translate(point: Coordinate, translateX_by: int, translateY_by: int, translateZ_by: int) -> Coordinate:
    x, y, z = point
    m = ([x], [y], [z], [1])
    tx_m = ([1, 0, 0, translateX_by], [0, 1, 0, translateY_by], [0, 0, 1, translateZ_by], [0, 0, 0, 1])
    xT, yT, zT, _ = np.dot(tx_m, m)
    return (xT[0], yT[0], zT[0])

def scale(point: Coordinate, scaleX_by: int, scaleY_by: int, scaleZ_by: int) -> Coordinate:
    x, y, z = point
    m = ([x], [y], [z], [1])
    tx_m = ([scaleX_by, 0, 0, 0], [0, scaleY_by, 0, 0], [0, 0, scaleZ_by, 0], [0, 0, 0, 1])
    xT, yT, zT, _ = np.dot(tx_m, m)
    return (xT[0], yT[0], zT)

def rotate(point: Coordinate, rotateBy: float) -> Coordinate:
    x, y, z = point
    m = ([x], [y], [z], [1]) # rotating matrix
    a = np.deg2rad(rotateBy) # rotation angle
    rx_m = ([1, 0,          0,          0],
            [0, np.cos(a), -np.sin(a),  0],
            [0, np.sin(a), np.cos(a),   0],
            [0, 0,          0,          1]) # rotate by matrix
    xT, yT, zT, _ = np.dot(rx_m, m)
    return (xT[0], yT[0], zT[0])

def main():
    pg.init()
    display.set_mode((500, 500), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("Lab 6 - 3D - COMP343 Computer Graphics Lab")

    gluPerspective(120, 1, 0, 200)
    glTranslatef(-20,-20,-100)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()
        # draw clipping window
        p1 = (1, 4, 40)
        p2 = (25, 4, 10)
        yellow  = (1, 1, 0)
        teal    = (0, 1, 1)
        white   = (1,1,1)
        _w   = (0.5,1,0.5)
        drawLine((0, 0, 0), (200, 0, 0), (1, 0, 0)) # x
        drawLine((0, 0, 0), (0, 200, 0), (0, 1, 0)) # y
        drawLine((0, 0, 0), (0, 0, 200), (0, 0, 1)) # z
        drawLine(p1, p2, yellow)
        pT1 = translate(p1, 30, 60, 10)
        pT2 = translate(p2, 30, 60, 10)
        drawLine(pT1, pT2, teal)
        pS1 = scale(p1, 4, 5, 1)
        pS2 = scale(p2, 4, 5, 1)
        drawLine(pS1, pS2, white)
        pR1 = rotate(p1, 45)
        pR2 = rotate(p2, 45)
        drawLine(pR1, pR2, _w)
        # drawLine((x_min,y_min, 1), (x_max,y_min, 1), (1, 0, 0))
        # drawLine((x_max,y_min, 1), (x_max,y_max, -1), (1, 1, 0))

        display.flip()

main()