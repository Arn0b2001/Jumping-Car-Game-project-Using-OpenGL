from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

dx = 0
dy = 30
color = (random.random(), random.random(), random.random())
W_Width = 500
W_Height = 600


####################################################################################################################################
def midp_line(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    increE = 2 * dy
    increNE = 2 * (dy - dx)
    x = x1
    y = y1
    cx, cy = convert_to_org(x, y, zone)
    glVertex2f(cx, cy)
    while (x < x2):

        if (d <= 0):
            d = d + increE
            x = x + 1
        else:
            d = d + increNE
            x += 1
            y += 1
        cx, cy = convert_to_org(x, y, zone)
        glVertex2f(cx, cy)


def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx >= 0 and dy < 0:
            zone = 7
        elif dx < 0 and dy >= 0:
            zone = 3
        else:
            zone = 4
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx >= 0 and dy < 0:
            zone = 6
        elif dx < 0 and dy >= 0:
            zone = 2
        else:
            zone = 5
    return zone


def convert_to_z0(x, y, zone):
    if (zone == 1):
        x, y = y, x
    elif (zone == 2):
        x, y = y, -x
    elif (zone == 3):
        x, y = -x, y
    elif (zone == 4):
        x, y = -x, -y
    elif (zone == 5):
        x, y = -y, -x
    elif (zone == 6):
        x, y = -y, x
    elif (zone == 7):
        x, y = x, -y
    return x, y


def convert_to_org(x, y, zone):
    if (zone == 1):
        x, y = y, x
    elif (zone == 2):
        x, y = -y, x
    elif (zone == 3):
        x, y = -x, y
    elif (zone == 4):
        x, y = -x, -y
    elif (zone == 5):
        x, y = -y, -x
    elif (zone == 6):
        x, y = y, -x
    elif (zone == 7):
        x, y = x, -y
    return x, y


def circle_points(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)
    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)
    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)
    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)


def heart_c(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)
    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)


def mid_circle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius
    glPointSize(1)
    glBegin(GL_POINTS)
    while x <= y:

        circle_points(x, y, cx, cy)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    glEnd()


def mid_h(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius
    glBegin(GL_POINTS)
    while x <= y:

        heart_c(x, y, cx, cy)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    glEnd()


def draw_line(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x1, y1 = convert_to_z0(x1, y1, zone)
    x2, y2 = convert_to_z0(x2, y2, zone)
    glPointSize(1)
    glBegin(GL_POINTS)  # Change to GL_LINES for line drawing
    midp_line(x1, y1, x2, y2, zone)
    glEnd()


######################################################################################################################################
# v = random.choice([0, 1])
def gov():
    glColor3f(1.0, 1.0, 1.0)
    # G
    draw_thicker_line(150, 350, 165, 350, 2)
    draw_thicker_line(150, 350, 150, 325, 2)
    draw_thicker_line(150, 325, 165, 325, 2)
    draw_thicker_line(165, 325, 165, 335, 2)

    # A
    draw_thicker_line(175, 325, 175, 350, 2)
    draw_thicker_line(175, 350, 190, 350, 2)
    draw_thicker_line(190, 350, 190, 325, 2)
    draw_thicker_line(175, 335, 190, 335, 2)

    # M
    draw_thicker_line(200, 325, 200, 350, 2)
    draw_thicker_line(200, 350, 215, 335, 2)
    draw_thicker_line(215, 335, 230, 350, 2)
    draw_thicker_line(230, 350, 230, 325, 2)

    # E
    draw_thicker_line(240, 325, 240, 350, 2)
    draw_thicker_line(240, 325, 255, 325, 2)
    draw_thicker_line(240, 335, 255, 335, 2)
    draw_thicker_line(240, 350, 255, 350, 2)

    # O
    draw_thicker_line(275, 325, 275, 350, 2)
    draw_thicker_line(275, 325, 290, 325, 2)
    draw_thicker_line(290, 325, 290, 350, 2)
    draw_thicker_line(275, 350, 290, 350, 2)

    # V
    draw_thicker_line(300, 350, 315, 325, 2)
    draw_thicker_line(315, 325, 330, 350, 2)

    # E
    draw_thicker_line(335, 325, 335, 350, 2)
    draw_thicker_line(335, 325, 350, 325, 2)
    draw_thicker_line(335, 335, 350, 335, 2)
    draw_thicker_line(335, 350, 350, 350, 2)

    # R
    draw_thicker_line(360, 325, 360, 350, 2)
    draw_thicker_line(360, 350, 375, 350, 2)
    draw_thicker_line(375, 350, 375, 335, 2)
    draw_thicker_line(360, 335, 375, 335, 2)
    draw_thicker_line(360, 335, 375, 325, 2)


v = random.choice([True, False])


def vehicle():
    global dx, dy
    thickness = 3
    draw_thicker_line(20 + dx, 90 + dy, 75 + dx, 90 + dy, thickness)  # lower straight line
    draw_thicker_line(20 + dx, 90 + dy, 20 + dx, 100 + dy, thickness)  # left attached line
    draw_thicker_line(75 + dx, 90 + dy, 75 + dx, 100 + dy, thickness)  # right attached line
    draw_thicker_line(20 + dx, 100 + dy, 30 + dx, 100 + dy, thickness)  # left attached line to the right
    draw_thicker_line(30 + dx, 100 + dy, 30 + dx, 110 + dy, thickness)  # to the right
    draw_thicker_line(75 + dx, 100 + dy, 65 + dx, 100 + dy, thickness)  # right attached line to the left
    draw_thicker_line(65 + dx, 100 + dy, 65 + dx, 110 + dy, thickness)  # to the left
    draw_thicker_line(30 + dx, 110 + dy, 65 + dx, 110 + dy, thickness)  # head
    for i in range(8):
        mid_circle(35 + dx, 86 + dy, i)  # left wheels
        mid_circle(60 + dx, 86 + dy, i)  # right wheels


def draw_thicker_line(x1, y1, x2, y2, thickness):
    for i in range(thickness):
        draw_line(x1, y1 + i, x2, y2 + i)


def bike():
    draw_thicker_line(20 + dx, 90 + dy, 60 + dx, 90 + dy, 4)
    draw_thicker_line(20 + dx, 90 + dy, 35 + dx, 100 + dy, 4)
    draw_thicker_line(35 + dx, 100 + dy, 50 + dx, 90 + dy, 4)

    draw_thicker_line(60 + dx, 90 + dy, 70 + dx, 100 + dy, 4)

    draw_thicker_line(58 + dx, 110 + dy, 80 + dx, 90 + dy, 4)
    draw_thicker_line(58 + dx, 110 + dy, 53 + dx, 110 + dy, 4)
    for i in range(8):
        mid_circle(20 + dx, 82 + dy, i)
        mid_circle(80 + dx, 83 + dy, i)


def heart():
    global live
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(3)
    for i in range(8):
        if live == 3:
            mid_h(445, 580, i)
            draw_line(437 + i, 580, 445, 565)
            draw_line(453 - i, 580, 445, 565)
        if live == 3 or live == 2:
            mid_h(463, 580, i)
            draw_line(455 + i, 580, 463, 565)
            draw_line(471 - i, 580, 463, 565)
        if live == 1 or live == 2 or live == 3:
            mid_h(481, 580, i)
            draw_line(473 + i, 580, 481, 565)
            draw_line(489 - i, 580, 481, 565)


def newh():
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(3)
    global live, bcol, ball_c1, ball_c2, ball_animation_started
    if bcol == True:
        if live < 3:
            if live == 2:
                mid_h(445, 580, i)
                draw_line(437 + i, 580, 445, 565)
                draw_line(453 - i, 580, 445, 565)
                live += 1
                print('You got Extra life')
            if live == 1:
                mid_h(463, 580, i)
                draw_line(455 + i, 580, 463, 565)
                draw_line(471 - i, 580, 463, 565)
                live += 1
                print('You got Extra life')
        bcol = False
        ball_c1 = 730
        ball_c2 = 110
        ball_animation_started = False


g = []
for i in range(800):
    g.append((i, random.randint(92, 99)))


def ground():
    glColor3f(1.0, 1.0, 1.0)
    draw_line(0, 105, 800, 105)
    glPointSize(1)
    for i in g:
        glBegin(GL_POINTS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(i[0], i[1])
        glEnd()


def draw_star():
    global count
    glPointSize(2)  # Set point size for stars
    glBegin(GL_POINTS)
    for _ in range(100):
        x_pos = random.uniform(0.0, 800.0)
        y_pos = random.uniform(0.0, 600.0)
        color = (1.0, 1.0, 1.0)  # Random color
        glColor3f(*color)
        glVertex2f(x_pos, y_pos)
    glEnd()
    if count == 3000:
        count = 0


score = 0


# car
def clouds():
    glPointSize(20)
    glColor3f(0.53, 0.81, 0.92)
    glBegin(GL_POINTS)
    # fc1
    glVertex2f(50, 450)
    glVertex2f(70, 450)
    glVertex2f(90, 450)
    glVertex2f(60, 460)
    glVertex2f(80, 460)
    # fc2
    glVertex2f(180, 430)
    glVertex2f(200, 430)
    glVertex2f(220, 430)
    glVertex2f(190, 440)
    glVertex2f(210, 440)
    # fc3
    glVertex2f(300, 390)
    glVertex2f(320, 390)
    glVertex2f(340, 390)
    glVertex2f(310, 400)
    glVertex2f(330, 400)
    # fc4
    glVertex2f(400, 450)
    glVertex2f(420, 450)
    glVertex2f(440, 450)
    glVertex2f(410, 460)
    glVertex2f(430, 460)
    glEnd()


def scoreD(p):
    glColor(1, 1, 1)
    if len(p) == 1:
        p = '0' + p
    for i in range(len(p)):
        if i == 0:
            s1, s2, p1, p2, p3 = 260, 240, 590, 560, 575
        else:
            s1, s2, p1, p2, p3 = 290, 270, 590, 560, 575

        if p[i] == '0':
            draw_line(s2, p1, s1, p1)
            draw_line(s2, p1, s2, p2)
            draw_line(s2, p2, s1, p2)
            draw_line(s1, p1, s1, p2)

        elif p[i] == '1':
            draw_line(s1, p1, s1, p2)

        elif p[i] == '2':
            draw_line(s2, p1, s1, p1)
            draw_line(s1, p1, s1, p3)
            draw_line(s1, p3, s2, p3)
            draw_line(s2, p2, s1, p2)
            draw_line(s2, p3, s2, p2)

        elif p[i] == '3':
            draw_line(s2, p1, s1, p1)
            draw_line(s1, p1, s1, p2)
            draw_line(s1, p3, s2, p3)
            draw_line(s2, p2, s1, p2)

        elif p[i] == '4':
            draw_line(s1, p1, s1, p2)
            draw_line(s2, p1, s2, p3)
            draw_line(s2, p3, s1, p3)

        elif p[i] == '5':
            draw_line(s2, p1, s1, p1)
            draw_line(s2, p1, s2, p3)
            draw_line(s2, p2, s1, p2)
            draw_line(s1, p3, s1, p2)
            draw_line(s2, p3, s1, p3)

        elif p[i] == '6':
            draw_line(s2, p1, s1, p1)
            draw_line(s2, p1, s2, p2)
            draw_line(s2, p2, s1, p2)
            draw_line(s1, p3, s1, p2)
            draw_line(s2, p3, s1, p3)

        elif p[i] == '7':
            draw_line(s2, p1, s1, p1)
            draw_line(s1, p1, s2, p2)
        elif p[i] == '8':
            draw_line(s1, p1, s2, p1)
            draw_line(s2, p1, s2, p2)
            draw_line(s2, p2, s1, p2)
            draw_line(s1, p1, s1, p3)
            draw_line(s2, p2, s2, p3)
            draw_line(s1, p3, s2, p3)
            draw_line(s1, p3, s1, p2)

        elif p[i] == '9':
            draw_line(s2, p1, s1, p1)
            draw_line(s1, p1, s1, p2)
            draw_line(s2, p1, s2, p3)
            draw_line(s2, p2, s1, p2)
            draw_line(s1, p2, s1, p3)
            draw_line(s1, p3, s2, p3)


initial_jump_velocity = 10
gravity_effect = 2.5  # Adjust the gravity effect as needed
jump_limit = 20  # Adjust the jump limit as needed

jumping = False
jump_count = 0


def jump():
    global jumping, jump_count, dy
    if not jumping:
        jumping = True
        jump_count = 0
        # dy += initial_jump_velocity  # Apply initial jump velocity


move = 0
obstacle = 1


def obstacles():
    global move, obstacle
    if obstacle == 1:
        # tree
        for i in range(45):
            draw_thicker_line(470 - move, 150 - i, 480 - move, 150 - i, 1)

        for i in range(10):
            mid_circle(460 - move, 150, 10 - i)  # left leaf
            mid_circle(490 - move, 150, 10 - i)  # right leaf
            mid_circle(475 - move, 160, 10 - i)  # middle leaf

    elif obstacle == 2:
        # diamond
        draw_line(470 - move, 130, 480 - move, 155)
        draw_line(480 - move, 105, 470 - move, 130)
        draw_line(480 - move, 155, 490 - move, 130)
        draw_line(490 - move, 130, 480 - move, 105)



def ball(c1, c2):
    glColor3f(0.0, 0.0, 0.5)
    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex2f(c1, c2)
    glEnd()


freeze = False
blst = False
live = 3
shot = False
score = 0
bcol = False
temp_dy = 0

def collision():
    global move, dy, v, obstacle, freeze, move, move2, bullets, blst, live, shot, score, ball_c1, ball_c2, ball_animation_started, bcol

    if not freeze:
        if v == False and bcol == False and ball_c1 <= 90 + dx and dy < 40:  # for bike and tree
            print('collied with the ball')
            bcol = True
        if v == True and bcol == False and ball_c1 <= 90 + dx and dy < 40:  # for bike and tree
            print('collied with the ball')
            bcol = True
        if live == 0:
            freeze = True
            print(f'Game Over! score: {score}')
        if v == False and obstacle == 1 and (360 - dx <= move <= 440 - dx) and dy < 40:  # for bike and tree
            blst = True
            move = 0
            live -= 1
            print(f'You have {live} lives remaining')

        if v == True and obstacle == 1 and (375 - dx <= move <= 450 - dx) and dy < 40:  # for car and tree
            blst = True
            move = 0
            live -= 1
            print(f'You have {live} lives remaining')

        if v == False and obstacle == 2 and (380 - dx <= move <= 460 - dx) and dy < 40:  # for bike and dim
            blst = True
            move = 0
            live -= 1
            print(f'You have {live} lives remaining')

        if v == True and obstacle == 2 and (395 - dx <= move <= 465 - dx) and dy < 40:  # for car and dim
            blst = True
            move = 0
            live -= 1
            print(f'You have {live} lives remaining')

        # for bullets

        if v == True and obstacle == 2 and (70 + move2 < 470 - move - dx <= 81 + move2) and temp_dy < 40 and shot:  # for car and diamond
            bullets = []
            move = 0
            v = False
            print("Vehicle Changed")

        if v == False and obstacle == 2 and (85 + move2 < 470 - move - dx <= 96 + move2) and temp_dy < 40 and shot:  # for bike and diamond
            bullets = []
            move = 0
            v = True
            print("Vehicle Changed")

        if v == False and obstacle == 1 and (85 + move2 < 450 - move - dx <= 96 + move2) and dy < 40:  # for bike and tree
            bullets = []
            print("Aim for diamonds")

        if v == True and obstacle == 1 and (70 + move2 < 450 - move - dx <= 81 + move2) and dy < 40:  # for car and tree

            bullets = []
            print("Aim for diamonds")



move2 = 0  # bullets x-axis movement parameter
bullets = []


def shoot():
    global v, move2, dy, bullets, shot
    if freeze == False:
        if v:
            bullets.append([78 + dx, 100 + dy, 3])  # 100 since dy = 30

        else:
            bullets.append([93 + dx, 100 + dy, 3])


count = 0


def time_func():
    if 0 <= count <= 1499:
        clouds()
    if 1500 <= count <= 3000:
        draw_star()


import time

past_time = time.time()
speed = 1
brad = 0


def blast():
    global brad
    if blst == True:
        glColor3f(1, 0, 0)
        mid_circle(100 + dx, 100, brad)


ball_c1 = 730  # Initial x-coordinate of the ball
ball_c2 = 110  # Initial y-coordinate of the ball
ball_animation_started = False


def animate():
    global move, obstacle, freeze, move2, bullets, past_time, speed, shot, score
    global ball_c1, ball_c2, ball_animation_started

    present_time = time.time()
    passed_time = present_time - past_time

    if passed_time >= 5 and not freeze:
        speed *= 1.2
        print("speed increased")
        past_time = present_time

    if move < 470 and not freeze:
        move += speed
    else:
        if not freeze:
            score += 1
            move = 0
            obstacle = random.randint(1, 2)
            print(f"score: {score}")

    if move2 < 450 and len(bullets) != 0:
        if not freeze:
            move2 += 1
    else:
        bullets = []
        move2 = 0
        shot = False

    # Ball animation logic
    if score % 10 == 0 and score > 0 and not ball_animation_started and live > 0:
        ball_animation_started = True

    if ball_animation_started:
        if freeze == False:
            ball_c1 -= 0.90

    glutPostRedisplay()


on_g = False


def buttons():
    global click, color

    draw_line(10, 570, 30, 590)
    draw_line(10, 570, 30, 550)
    draw_line(10, 570, 60, 570)



def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b


def mouseListener(button, state, x, y):
    global score, freeze, bullets, move, speed, v, obstacle, freeze, live, blst, brad, ball_c1, ball_c2, ball_animation_started, dx,present_time,past_time
    c_x, c_y = convert_coordinate(x, y)

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if -220 < c_x < -150 and 260 < c_y < 300:
            score = 0
            move = 0
            speed = 1
            freeze = False
            obstacle = random.randint(1, 2)
            live = 3
            blst = False
            brad = 0
            ball_c1 = 730
            ball_c2 = 110
            ball_animation_started = False
            dx = 0
            present_time=time.time()
            past_time=time.time()
            print("Starting Over!")


def display():
    global dy, jumping, jump_count, count, on_g, brad, blst, score, bcol
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(*color)  # Set color for the vehicle
    if freeze == False and live > 0:
        if jumping:
            if jump_count < jump_limit:
                dy += initial_jump_velocity  # Apply initial jump velocity
                jump_count += 1
            else:
                jumping = False
        else:
            if dy > 30:  # Adjust jump depent speed as needed
                dy -= gravity_effect
            if dy == 30:
                on_g = True

    if v:
        vehicle()
    else:
        bike()

    if len(bullets) != 0:
        for i in bullets:
            mid_circle(i[0] + move2, i[1], i[2])
    ground()
    heart()
    scoreD(str(score))
    obstacles()
    if bcol == False:
        ball(ball_c1, ball_c2)
    newh()

    if live != 0:
        time_func()
    if freeze == False:
        count += 1
    # clouds()
    collision()
    buttons()
    # pause()
    if blst == True:
        for i in range(5):
            blast()
            brad += 1
    lv()
    if live == 0:
        gov()

    # print(move, dy)
    glutSwapBuffers()


def lv():
    global blst, live, freeze
    if blst == True and live > 0:
        freeze = False
        blst = False


def handle_key(key, x, y):
    global v, shot, move2, bullets, on_g, freeze, dx, temp_dy
    if key == b'j' and on_g == True:
        jump()
        on_g = False
    if key == b' ':
        if freeze == False:
            freeze = True
            print("Paused")


        else:
            freeze = False
            print("Resumed")

    if key == b's':
        if len(bullets) == 0:  # shoots only once at a time
            temp_dy = dy
            shoot()
            shot = True

    if key == b'd':
        if dx < 420 and dy == 30 and not freeze:
            dx += 10
    if key == b'a':
        if dx > 0 and dy == 30 and not freeze:
            dx -= 10


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 500, 0, 600)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 500)
glutCreateWindow(b"Assignment 2")
init()

glutDisplayFunc(display)
glutIdleFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(handle_key)
glutMouseFunc(mouseListener)
# glEnable(GL_DEPTH_TEST)  # Register keyboard callback
glutMainLoop()
