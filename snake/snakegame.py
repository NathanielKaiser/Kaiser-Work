from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint

window = 0                                             # glut window number
width, height = 500, 500                               # window size
field_width, field_height = 50, 50                     # internal resolution

snake = [(25, 25), (24, 25), (23, 25)]       # snake list of (x, y) positions
snake_dir = (0, 0)                           # snake movement direction

interval = 50                                # update interval in millisecond

food = []                                    # food list of type (x, y)

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

def draw_snake():
    glColor3f(1.0, 1.0, 1.0)    # set color to white
    for x, y in snake:          # go through each (x, y) entry
        draw_rect(x, y, .9, .9) # draw it at (x, y) with width=1 and height=1

def draw_food():
    glColor3f(0.5, 0.5, 1.0)  # set color to blue
    for x, y in food:         # go through each (x, y) entry
        draw_rect(x, y, 1, 1) # draw it at (x, y) with width=1 and height=1

def draw():                                            # draw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d_custom(width, height, field_width, field_height)

    draw_food()                                        # draw the food
    draw_snake()                                       # draw the snake

    glutSwapBuffers()                                  # important for double buffering

def update(value):
    # move snake
    snake.insert(0, vec_add(snake[0], snake_dir))      # insert new position in the beginning of the snake list
    snake.pop()                                        # remove the last element

    (hx, hy) = snake[0]                                # get the snake's head x and y position

    for x, y in snake[1:]:
        if hx == x and hy == y:
            killsnake()

    if hx >= 50 or hx <= -1 or hy >= 50 or hy <= -1:
        killsnake()

    for x, y in food:            # go through the food list
        if hx == x and hy == y:  # is the head where the food is?
            snake.append((x, y)) # make the snake longer
            food.remove((x, y))  # remove the food
            spawnfood()

    glutTimerFunc(interval, update, 0)            # trigger next update

def vec_add((x1, y1), (x2, y2)):
        return (x1 + x2, y1 + y2)

def keyboard(*args):
    global snake_dir                                   # important if we want to set it to a new value
                                                       # changes the variable defined at the top - not a local
    if args[0] == GLUT_KEY_UP:
        if snake_dir == (0, -1):
            snake_dir = (0, -1)
        else:
            snake_dir = (0, 1)
    if args[0] == GLUT_KEY_DOWN:
        if snake_dir == (0, 1):
            snake_dir = (0, 1)
        else:
            snake_dir = (0, -1)
    if args[0] == GLUT_KEY_LEFT:
        if snake_dir == (1, 0):
            snake_dir = (1, 0)
        else:
            snake_dir = (-1, 0)
    if args[0] == GLUT_KEY_RIGHT:
        if snake_dir == (-1, 0):
            snake_dir = (-1, 0)
        else:
            snake_dir = (1, 0)

def killsnake():
    global snake, snake_dir
    del snake[:]
    snake = [(25, 25), (24, 25), (23, 25)]
    snake_dir = (0, 0)
    del food[:]
    spawnfood()

def spawnfood():
    x, y = randint(0, 49), randint(0, 49)                  # random spawn position
    food.append((x, y))                                    # create food

spawnfood()
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("snake")                     # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutSpecialFunc(keyboard)                              # tell opengl that we want to check keys
glutTimerFunc(interval, update, 0)                     # trigger next update
glutMainLoop()                                         # start everything
