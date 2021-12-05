from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Ping Pong")

clock = time.Clock()

game = True
x1 = 100
y1 = 150

x2 =250
y2 = 30
while game:


    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_w] and y1 > 0:
        y1 -= 10

    if keys_pressed[K_s] and y1 < 395:
        y1 += 10

    if keys_pressed[K_a] and x1 > 0:
        x1 -= 10

    if keys_pressed[K_d] and x1 < 595:
        x1 += 10


    if keys_pressed[K_UP] and y2 > 0:
        y2 -= 10

    if keys_pressed[K_DOWN] and y2 < 395:
        y2 += 10

    if keys_pressed[K_LEFT] and x2 > 0:
        x2 -= 10

    if keys_pressed[K_RIGHT] and x2 < 595:
        x2 += 10

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()
