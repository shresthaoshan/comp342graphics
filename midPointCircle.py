
from typing import Tuple
import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

Coordinate = Tuple[int, int]

def midptcircle(center: Coordinate = (0,0), r: int = 1):
    x_centre, y_centre = center
    
    coordinates: list[Coordinate] = []

    x = r
    y = 0
      
    # Printing the initial point the 
    # axes after translation 
    coordinates.append((x + x_centre, y + y_centre))

    # When radius is zero only a single 
    # point be printed 
    if (r > 0) :
        coordinates.append((x + x_centre, -y + y_centre))
        coordinates.append((y + x_centre, x + y_centre))
        coordinates.append((-y + x_centre, x + y_centre))

    # Initialising the value of P 
    P = 1 - r 
  
    while x > y:
      
        y += 1
          
        # Mid-point inside or on the perimeter
        if P <= 0: 
            P = P + 2 * y + 1
              
        # Mid-point outside the perimeter 
        else:         
            x -= 1
            P = P + 2 * y - 2 * x + 1
          
        # All the perimeter points have 
        # already been printed 
        if (x < y):
            break
          
        # Printing the generated point its reflection 
        # in the other octants after translation
        
        coordinates.append((x + x_centre, y + y_centre))
        coordinates.append((-x + x_centre, y + y_centre))
        coordinates.append((x + x_centre, -y + y_centre))
        coordinates.append((-x + x_centre, -y + y_centre))
 
        # If the generated point on the line x = y then 
        # the perimeter points have already been printed 
        if x != y:
            
            coordinates.append((y + x_centre, x + y_centre))
            coordinates.append((-y + x_centre, x + y_centre))
            coordinates.append((y + x_centre, -x + y_centre))
            coordinates.append((-y + x_centre, -x + y_centre))

    return coordinates

def drawEllipse():
    xc, yc = (0, 0)
    region = midptcircle((xc, yc), 15)
    region_xy : list[Coordinate] = [(x[0] - xc, x[1] - yc) for x in region] 
    region_nxy : list[Coordinate] = [(-x[0] + xc, x[1] - yc) for x in region]
    region_xny : list[Coordinate] = [(x[0] - xc, -x[1] + yc) for x in region]
    region_nxny : list[Coordinate] = [(-x[0] + xc, -x[1] + yc) for x in region]

    for region in [region_xy, region_nxy, region_xny, region_nxny]:
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0,0.0,1.0)
        for v in region:
            x,y = v
            glVertex2f(x, y)
        glEnd()

def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("Circle - Mid Point - COMP343 Computer Graphics Lab")

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