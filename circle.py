from OpenGL.GL import *
from math import *

def circle(radius: int = 1, sides: int = 32, x_shift: int = 0, y_shift: int = 0):
    glBegin(GL_POLYGON)
    for i in range(100):
        _x = radius * cos(i*2*pi/sides) + x_shift
        _y = radius * sin(i*2*pi/sides) + y_shift
        glVertex2f(_x,_y)
    glEnd()