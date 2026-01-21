from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Camera
cam_angle_x=20
cam_angle_y=30
cam_distance=8

#Mouse
last_x=0
last_y=0
mouse_pressed=False

def init ():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)
#lIGHTING
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

#Tipe shading
    glShadeModel(GL_SMOOTH)

#Posisi Cahaya
    light_position=[5.0,5.0,5.0,1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)


#Warna cahaya
    glLightfv(GL_LIGHT0, GL_AMBIENT,[0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE,[0.8, 0.8, 0.8, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR,[1.0, 1.0, 1.0, 1.0])

#Faungsi bikin 3D
def draw_cube():
    glBegin(GL_QUADS)

#Depan
    glNormal3f(0,0,1)
    glColor3f(1,0,0)
    glVertex3f(-1,-1,1)
    glVertex3f(1,-1,1)
    glVertex3f(1,1,1)
    glVertex3f(-1,1,1)

#Belakang
    glNormal3f(0,0,-1)
    glColor3f(0,1,0)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,1,-1)
    glVertex3f(1,1,-1)
    glVertex3f(1,-1,-1)

#Atas
    glNormal3f(0,1,0)
    glColor3f(0,0,1)
    glVertex3f(-1,1,-1)
    glVertex3f(-1,1,1)
    glVertex3f(1,1,1)
    glVertex3f(1,1,-1)

#Bawah
    glNormal3f(0,-1,0)
    glColor3f(1,1,0)
    glVertex3f(-1,-1,-1)
    glVertex3f(1,-1,-1)
    glVertex3f(1,-1,1)
    glVertex3f(-1,-1,1)

#Kanan
    glNormal3f(1,0,0)
    glColor3f(1,0,1)
    glVertex3f(1,-1,-1)
    glVertex3f(1,1,-1)
    glVertex3f(1,1,1)
    glVertex3f(1,-1,1)

#Kiri
    glNormal3f(-1, 0, 0)
    glColor3f(0,1,1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1,1)
    glVertex3f(-1,1,1)
    glVertex3f(-1,1,-1)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

#Kamera
    glTranslatef(0,0,-cam_distance)
    glRotatef(cam_angle_x, 1, 0, 0)
    glRotatef(cam_angle_y, 0, 1, 0)

    draw_cube()
    glutSwapBuffers()

def mouse(button, state, x, y):
    global mouse_pressed, last_x, last_y, cam_distance
    if button == GLUT_LEFT_BUTTON:
        mouse_pressed=(state==GLUT_DOWN)
        last_x=x
        last_y=y
#Scrol Zoom
    if button==3:
        cam_distance-=0.5
    elif button==4:
        cam_distance+=0.5

    glutPostRedisplay()
def motion(x,y):
    global last_x, last_y, cam_angle_x, cam_angle_y
    if mouse_pressed:
        dx=x-last_x
        dy = y- last_y
        cam_angle_y+=dx*0.5
        cam_angle_x+=dy*0.5
        last_x=x
        last_y=y
    glutPostRedisplay()

def reshape(w, h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800,600)
    glutCreateWindow(b'Grafika Komputer 3D -Lighting and Shading')

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()
main()