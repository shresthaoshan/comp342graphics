import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

def circle(x: GLfloat, y: GLfloat, radius: GLfloat):
    glBegin(GL_POLYGON)
    for i in range(100):
        angle = i*2*(pi/100)
        glVertex2f(x+(cos(angle)*radius),y+(sin(angle)*radius))
    glEnd()


def flag():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(0.1, 0.1, 0.0)
    glVertex3f(0.1, 0.96, 0.0)
    glVertex3f(0.12, 0.96, 0.0)
    glVertex3f(0.12, 0.1, 0.0)

    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)

    glVertex3f(0.12, 0.9, 0.0)
    glVertex3f(0.3, 0.5, 0.0)
    glVertex3f(0.12, 0.5, 0.0)

    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.12, 0.6, 0.0)
    glVertex3f(0.35, 0.2, 0.0)
    glVertex3f(0.12, 0.2, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)

    glVertex3f(0.12, 0.9, 0.0)
    glVertex3f(0.3, 0.5, 0.0)
    glVertex3f(0.33, 0.5, 0.0)
    glVertex3f(0.12, 0.96, 0.0)

    glVertex3f(0.33, 0.5, 0.0)
    glVertex3f(0.18, 0.5, 0.0)
    glVertex3f(0.20, 0.46, 0.0)
    glVertex3f(0.33, 0.46, 0.0)

    glVertex3f(0.19, 0.48, 0.0)
    glVertex3f(0.35, 0.18, 0.0)
    glVertex3f(0.3688, 0.2, 0.0)
    glVertex3f(0.215, 0.49, 0.0)

    glVertex3f(0.12, 0.2, 0.0)
    glVertex3f(0.3680, 0.2, 0.0)
    glVertex3f(0.3680, 0.16, 0.0)
    glVertex3f(0.12, 0.16, 0.0)

    glEnd()

    # moon
    glColor3f(1.0,1.0,1.0)
    circle(0.180,0.610,0.036)
    glColor3f(1.0,0.0,0.0)
    circle(0.180,0.630,0.036)
    glColor3f(1.0,1.0,1.0)
    circle(0.180,0.61,0.019)


    # sun
    
    glColor3f(1.0,1.0,1.0)
    glBegin (GL_POLYGON)
    glVertex3f(0.20-0.02,0.60-0.28,0.0)
    glVertex3f(0.22-0.02,0.63-0.28,0.0)
    glVertex3f(0.24-0.02,0.6-0.28,0.0)
    glVertex3f(0.26-0.02,0.61-0.28,0.0)
    glVertex3f(0.25-0.02,0.58-0.28,0.0)
    glVertex3f(0.27-0.02,0.56-0.28,0.0)
    glVertex3f(0.24-0.02,0.56-0.28,0.0)
    glVertex3f(0.22-0.02,0.53-0.28,0.0)
    glVertex3f(0.2-0.02,0.56-0.28,0.0)
    glVertex3f(0.16-0.02,0.555-0.28,0.0)
    glVertex3f(0.18-0.02,0.58-0.28,0.0)
    glVertex3f(0.16-0.02,0.605-0.28,0.0)
    glEnd()

def main():
    pg.init()
    display.set_mode((400, 400), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("Flag of Nepal - COMP343 Computer Graphics Lab")

    gluPerspective(55, 1, 1, 10)
    glTranslatef(0.0, 0, -2)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        # square(2)
        # circle()
        flag()
        display.flip()

main()