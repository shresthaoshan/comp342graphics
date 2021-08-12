from typing import Tuple
import pygame as pg
from pygame import display, event
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Defining region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000
  
# Defining x_max, y_max and x_min, y_min for rectangle
# Since diagonal points are enough to define a rectangle
x_max = 300.0
y_max = 300.0
x_min = -300.0
y_min = -300.0


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

# Function to compute region code for a point(x, y)
def computeCode(point: Coordinate):
    x, y = point
    code = INSIDE
    if x < x_min:      # to the left of rectangle
        code |= LEFT
    elif x > x_max:    # to the right of rectangle
        code |= RIGHT
    if y < y_min:      # below the rectangle
        code |= BOTTOM
    elif y > y_max:    # above the rectangle
        code |= TOP
  
    return code
  
  
def cohenSutherlandClip(point1: Coordinate, point2: Coordinate):
    x1, y1 = point1
    x2, y2 = point2
    
    code1 = computeCode((x1, y1))
    code2 = computeCode((x2, y2))

    accept = False
  
    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
  
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
  
            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
  
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
  
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
            
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode((x1, y1))
            else:
                x2 = x
                y2 = y
                code2 = computeCode((x2, y2))
  
    if accept:
        drawLine((x1, y1), (x2, y2), (0.0, 1.0, 0.0))

def draw():
    cohenSutherlandClip((225, 115), (-78, 400))
    glFlush()

def main():
    pg.init()
    display.set_mode((500, 500), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("Lab 5 - Cohen Sutherland - COMP343 Computer Graphics Lab")

    glTranslatef(0.0, 0.0, 0.0)
    gluOrtho2D(-320,320,-320,320)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()        
        # draw clipping window
        drawLine((x_min,y_min), (x_max,y_min))
        drawLine((x_max,y_min), (x_max,y_max))
        drawLine((x_min,y_min), (x_min,y_max))
        drawLine((x_min,y_max), (x_max,y_max))
        # draw lines
        draw()

        display.flip()

main()