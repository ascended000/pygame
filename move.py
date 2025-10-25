from pygame import *
init()

size = 1000,800
window = display.set_mode(size)
display.set_caption("move the square with arrow keys")
clock = time.Clock()
player = Rect(200, 200, 50, 50)
p_speed = 5

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    window.fill((0,0,0))
    draw.rect(window,(0,200,0),player)
    keys = key.get_pressed()
    if keys[K_w]:
        player.y -= p_speed
    if keys[K_s]:
        player.y += p_speed
    if keys[K_a]:
        player.x -= p_speed
    if keys[K_d]:
        player.x += p_speed
    display.update()
    clock.tick(60)