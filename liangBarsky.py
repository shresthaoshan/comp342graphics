from typing import Tuple
import pygame as pg
from pygame import display, event
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# window
x_min, y_min = (-300, -300)
x_max, y_max = (300, 300)

Coordinate = Tuple[float, float]
ColorRGB = Tuple[float, float, float]

def drawLine(point1: Coordinate, point2: Coordinate, color: ColorRGB = (1.0, 1.0, 1.0)):
    x1, y1 = point1
    x2, y2 = point2
    r, g, b = color
    glBegin(GL_LINE_STRIP)
    glColor3f(r,g,b)
    glVertex2d(x1,y1)
    glVertex2d(x2,y2)
    glEnd()

def liangBarsky(first_point: Coordinate, second_point: Coordinate, wMin: Coordinate = (x_min, y_min), wMax: Coordinate = (x_max, y_max)):
    x1,     x2      = first_point
    y1,     y2      = second_point
    xw_min, yw_min  = wMin
    xw_max, yw_max  = wMax

    dx = x2 - x1
    dy = y2 - y1
    
    p = [-dx, dx,  -dy, dy]
    q = [x1 - xw_min, xw_max - x1, y1 - yw_min, yw_max - y1]

    for i in range(4):
        pk = p[i]
        qk = q[i]
        if pk == 0:
            if qk >= 0:
                if(i <2):
                    if (y1 < yw_min):
                        y1 = yw_min
                    if(y2 > yw_max):
                        y2 = yw_max
                    print((x1,y1), (x2,y2))
                    drawLine((x1,y1), (x2,y2), (1, 0, 0))
                else:
                    if (x1 < xw_min):
                        x1 = xw_min
                    if (x2 > xw_max):
                        x2 = xw_max
                    print((x1,y1), (x2,y2))
                    drawLine((x1,y1), (x2,y2), (0,0,1))

    u1, u2 = 0, 1
    for i in range(4):
        if not p[i] == 0:
            t = q[i]/p[i]
            if p[i] < 0:
                if u1 <= t:
                    u1 = t
            else:
                if u2 > t:
                    u2 = t

    if u1 < u2:
        x1, x2 = x1 + u1 * dx, x1 + u2 * dx
        y1, y2 = y1 + u1 * dy, y1 + u2 * dy
        drawLine((x1, y1), (x2, y2), (0, 1, 0))


def main():
    pg.init()
    display.set_mode((500, 500), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("Lab 5 - Liang Barsky - COMP343 Computer Graphics Lab")

    glTranslatef(0.0, 0.0, 0.0)
    gluOrtho2D(-320,320,-320,320)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()        
        # draw clipping window
        drawLine((x_min,y_min), (x_max,y_min), (1.0, 1.0, 0.0))
        drawLine((x_max,y_min), (x_max,y_max), (1.0, 1.0, 0.0))
        drawLine((x_min,y_min), (x_min,y_max), (1.0, 1.0, 0.0))
        drawLine((x_min,y_max), (x_max,y_max), (1.0, 1.0, 0.0))
        # draw lines
        liangBarsky((400, 160), (10, 110))
        liangBarsky((20, 230), (-80, 190))

        display.flip()

main()