
from typing import Tuple
import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

Coordinate = Tuple[int, int]

def midptellipse(center: Coordinate = (0,0), rx: int = 1, ry: int = 1):
    xc, yc = center
    
    x = 0
    y = ry
    coordinates: list[Coordinate] = []
    
 
    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) +
                      (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
 
    # For region 1
    while (dx < dy):
        coordinates.append((x+xc, y+yc))
 
        # Checking and updating value of
        # decision parameter based on algorithm
        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)
 
    # Decision parameter of region 2
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
           (rx * rx * ry * ry))
 
    # Plotting points of region 2
    while (y >= 0):
        coordinates.append((x+xc, y+yc))
 
        # Checking and updating parameter
        # value based on algorithm
        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)

    return coordinates

def drawEllipse():
    xc, yc = (50, 70)
    region = midptellipse((xc, yc), 30, 50)
    region_xy : list[Coordinate] = [(x[0] - xc, x[1] - yc) for x in region] 
    region_nxy : list[Coordinate] = [(-x[0] + xc, x[1] - yc) for x in region]
    region_xny : list[Coordinate] = [(x[0] - xc, -x[1] + yc) for x in region]
    region_nxny : list[Coordinate] = [(-x[0] + xc, -x[1] + yc) for x in region]

    for region in [region_xy, region_nxy, region_xny, region_nxny]:
        glBegin(GL_LINE_STRIP)
        glColor3f(0.0,0.0,1.0)
        for v in region:
            x,y = v
            glVertex2f(x, y)
        glEnd()

def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("Ellipse - Mid Point - COMP343 Computer Graphics Lab")

    gluPerspective(200, 1, 1, 10)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        drawEllipse()
        display.flip()

main()