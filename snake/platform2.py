from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 500                               # window size
field_width, field_height = 50, 50                     # internal resolution

box = [25, 24]                                         # box list of (x, y) positions
platformx = list(range(22, 29))
platformy = [(24)]

velocityy = 0
velocityx = 0

interval = 40                                        # update interval in millisecond

def refresh2d_custom(width, height, internal_width, internal_height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, internal_width, 0.0, internal_height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def draw_box():
    glColor3f(0.5, 0.5, 1.0)    # set color to blue
    draw_rect(box[0], box[1], 1, 1)   # draw it at (x, y) with width=1 and height=1

def draw_platform():
    glColor3f(1.0, 1.0, 1.0)     # set color to white
    for x in platformx:        # go through each (x, y) entry
        draw_rect(x, 24, 1, -1)   # draw it at (x, y) with width=1 and height=1

def draw():                                            # draw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d_custom(width, height, field_width, field_height)

    draw_box()                                         # draw the box
    draw_platform()                                    # draw the platform

    glutSwapBuffers()                                  # important for double buffering

def update(value):

    gravity()
    movement()
    outofbounds()

    print
    print platformx
    print platformy
    print
    print box
    print "velocity y = ", velocityy
    print "velocity x = ", velocityx
    print "---------------------------------------"

    glutTimerFunc(interval, update, 0)                 # trigger next update

def gravity():
    global velocityy
    if box[1] != 24:
        velocityy -= 1

def movement():
    global box, velocityx, velocityy

    yrange = int(velocityy)
    negativey = list(range(-1, yrange + 1, -1))
    positivey = list(range(1, yrange + 1, 1))

    print
    print "positive y moement", positivey
    print "negative y movement", negativey

    box[0] += velocityx
    bx, by = box[0], box[1]

    #set y movement
    if velocityy < 0:
        for x in negativey:
            box[1] -= 1
            if (by == 24):
                velocityy = 0

    elif velocityy > 0:
        for x in positivey:
            box[1] += 1
            if (by == 24):
                velocityy = 0
    else:
        pass

    velocityy = 0

    #set x movement
    if velocityx > 0:
        velocityx -= 1
    elif velocityx < 0:
        velocityx += 1
    else:
        velocityx = 0

def outofbounds():
    (bx, by) = box[0], box[1]
    if (bx >= 50 or bx <= -1 or by >= 50 or by <= -1):
        restart()

def restart():
    global box, velocityy, velocityy
    del box[:]
    box = [25, 24]
    velocityy = 0
    velocityx = 0

def keyboard(*args):
    global velocityy, velocityx, platformx

    if args[0] == GLUT_KEY_UP:
        (bx, by) = box[0], box[1]
        for x in platformx:
            if (x == bx and 24 == by):
                velocityy += 3
            else:
                velocityy += 0

    #if args[0] == GLUT_KEY_DOWN:

    if args[0] == GLUT_KEY_LEFT:
        if velocityx > -3:
            velocityx -= 1

    if args[0] == GLUT_KEY_RIGHT:
        if velocityx < 3:
            velocityx += 1

glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("box")                       # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutSpecialFunc(keyboard)                              # tell opengl that we want to check keys
glutTimerFunc(interval, update, 0)                     # trigger next update
glutMainLoop()                                         # start everything
