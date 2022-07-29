from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2
import sys


def init(windowSize=(500, 500), *args):
    glutInit(args)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)

    glutInitWindowSize(*windowSize)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("My3DModeller")

    # glEnable(GL_CULL_FACE)


def draw(func=None):
    glutDisplayFunc(func)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


def reshape(w, h, windowSize=(500, 500)):
    glViewport(0, 0, w, h)
    glLoadIdentity()
    glOrtho(-w/windowSize[0], w/windowSize[0], -h /
            windowSize[1], h/windowSize[1], -1.0, 1.0)


def keyboard(key, x, y):
    key = key.decode('utf-8')
    if key == 'q':
        print('exit')
        sys.exit()


def cube():
    xrot = 45
    yrot = 45
    glClearColor(0.3, 0.3, 0.3, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glutWireCube(0.7)
    glFlush()


def showImage():
    img = cv2.imread('JellyfishIcon.png')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w = img.shape[:2]
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h,
                 0, GL_RGBA, GL_BYTE, img)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 1.0, 1.0))

    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glBegin(GL_QUADS)
    glTexCoord2d(0.0, 1.0)
    glVertex3d(-1.0, -1.0, 1.0)
    glTexCoord2d(1.0, 1.0)
    glVertex3d(1.0, -1.0, 0.0)
    glTexCoord2d(1.0, 0.0)
    glVertex3d(1.0, 1.0, 0.0)
    glTexCoord2d(0.0, 0.0)
    glVertex3d(-1.0, 1.0, 1.0)

    glEnd()
    glDisable(GL_TEXTURE_2D)

    glFlush()
    glutSwapBuffers()


def main(args):
    init(windowSize=(300, 300))
    draw(showImage)


if __name__ == "__main__":
    main(sys.argv)
    # img = cv2.imread('JellyfishIcon.png')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow("preview", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
