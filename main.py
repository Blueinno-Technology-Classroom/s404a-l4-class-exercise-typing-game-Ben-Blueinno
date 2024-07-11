import pgzrun

from pgzhelper import *

WIDTH = 1000
HEIGHT = 800

zombie_run_img = [
    'zombie/run/tile002',
    'zombie/run/tile003',
    'zombie/run/tile004',
    'zombie/run/tile005'
]

player_idle_img = [
    'player/idle/tile000',
    'player/idle/tile001',
    'player/idle/tile002',
    'player/idle/tile003',
    'player/idle/tile004',
    'player/idle/tile005',
    'player/idle/tile006',
    'player/idle/tile007',
    'player/idle/tile008',
    'player/idle/tile009'
]

player_die_img = [
    'player/die/tile000',
    'player/die/tile001',
    'player/die/tile002',
    'player/die/tile003',
    'player/die/tile004',
    'player/die/tile005',
    'player/die/tile006',
]

zombie = Actor(zombie_run_img[0])
zombie.images = zombie_run_img
zombie.scale = 5
zombie.fps = 10
zombie.right = WIDTH + 100
zombie.bottom = HEIGHT

player = Actor(player_idle_img[0])
player.images = player_idle_img
player.fps = 20
player.scale = 5
player.bottom = HEIGHT + 300

question = 'hello world'
response = ''


def update():
    global response
    zombie.animate()
    player.animate()
    if not(player.image in player_die_img):
        zombie.x -= 1
    if player.image == player_die_img[-1]:
        player.images = player_idle_img
        player.fps = 20
    if zombie.left <= 0:
        zombie.right = WIDTH + 100
        response = ''
    if zombie.collide_pixel(player):
        zombie.right = WIDTH + 100
        response = ''
        player.images = player_die_img
        player.fps = 5


def on_key_down(key):
    global response
    # print(key)

    if key in range(97, 123):
        print(chr(key))
        response += chr(key)
    elif key == keys.SPACE:  # spacebar
        response += ' '
    elif key == keys.BACKSPACE:  # backspace
        response = response[0:-1]


def draw():
    screen.clear()
    screen.draw.text(question, (50, 100), fontsize=120)
    screen.draw.text(response, (50, 100), fontsize=120, color='green')
    zombie.draw()
    player.draw()


pgzrun.go()
