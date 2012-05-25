from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5,-0.5)
    glVertex2f(-0.5,0.5)
    glVertex2f(0.5,0.5)
    glVertex2f(0.5,-0.5)
    glEnd()
    glFlush()
    
def mymain():
    print "Game Over!"
    
    glutInit(len(sys.argv), sys.argv)
    glutCreateWindow("Game Over!")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    mymain()

if __name__ == '__main__':
    pass