import numpy as np
from typing import Tuple

import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

Coordinate = Tuple[float, float]

def shear(point: Coordinate, shearX_by: int, shearY_by) -> Coordinate:
    x, y = point
    m = ([x], [y], [1])
    shearX_m = ([1, shearX_by, 0], [0, 1, 0], [0, 0, 1])
    shearY_m = ([1, 0, 0], [shearY_by, 1, 0], [0, 0, 1])
    
    composite_m = np.dot(shearX_m, shearY_m)
    
    sheared_m = np.dot(composite_m, m)

    xT, yT, _ = sheared_m
    
    return (xT[0], yT[0])

def displayPaint():
    st_point: Coordinate = (-4,-6)
    end_point: Coordinate = (7,3)
    shear_By = (2,1)
    st_tps = shear(st_point, shear_By[0], shear_By[1])
    end_tps = shear(end_point, shear_By[0], shear_By[1])
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(st_point[0], st_point[1])
    glVertex2f(end_point[0], end_point[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(st_tps[0], st_tps[1])
    glVertex2f(end_tps[0], end_tps[1])
    glEnd()

def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("Scaling - COMP343 Computer Graphics Lab")

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