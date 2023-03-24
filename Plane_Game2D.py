import pgzrun
import pgzero
import random
import pygame
import time
import os
from pynput import mouse

counter = 0
time = 0
Kills = 0

WIDTH = 500
HEIGHT = 700

# create Player
player = Actor('player_plane')
player.x = 250
player.y = 650

weapons = []
# create three enemy entity
enemy = []
for i in range(3):
    e = Actor('en')
    e.x = random.randint(0, 500)
    enemy.append(e)

def draw():
    global counter
    global cooldown
    global Kills
    global time
    screen.blit('bg', [0, 0])
    player.draw()
    # fucked char
    if player.image != 'fail':
        for w in weapons:
            w.draw()
        for e in enemy:
            e.draw()
# shoot
def on_key_down(key):
    global counter
    global cooldown
    global Kills
    global time
    # left click for shoot
    control = mouse.Controller()
    if keyboard.space:
        weapon = Actor('aml')
        weapon.x = player.x
        weapon.y = player.y - 50
        weapons.append(weapon)
def on_mouse_down():
    global counter
    global cooldown
    global Kills
    global time
    weapon = Actor('aml')
    weapon.x = player.x
    weapon.y = player.y - 50        
    weapons.append(weapon)


def update():
    global counter
    global cooldown
    global Kills
    global time
    counter += 1
    #Player move
    if keyboard.left or keyboard.a:
        player.x -= 5
    if keyboard.right or keyboard.d:
        player.x += 5
    if keyboard.up or keyboard.w:
        player.y -= 5
    if keyboard.down or keyboard.s:
        player.y += 5 
    if player.image == 'fail':
        print('You Have Killed',Kills)
        print('You Got in',time,'secounds')
        exit()
    # timer
    for e in enemy:
        if counter == 60:
            counter = 0
            time += 1
    # make entity movwe
    if e.y >= 150:
        random_num = random.randint(1, 5)
        if random == 1:
            e.x += 2
        else:
            e.x -= 2

    
    # aim
    for w in weapons:
        w.y -= 30
    for w in weapons:
        if w.y <= 0:
            weapons.remove(w)
    
    # enemy fix
    for e in enemy:
        e.y += 5
        if e.y > 700:
            e.x = random.randint(0, 500)
            e.y = 0
    
    #enemy init
    for e in enemy:
        for w in weapons:
            if e.colliderect(w):
                e.x = random.randint(0, 500)
                e.y = 0
                Kills += 1
                weapons.remove(w)

        
        # faild
        if e.colliderect(player) or player.y <= -15 or player.y >= 715 or player.x >= 515 or player.x <= -15:
            player.image = 'fail'
            #播放失败音乐
            music.play('faild')

# background music
music.play('music1')

os.environ['SDL_VIDEO_CENTERED'] = '1'

pgzrun.go()
