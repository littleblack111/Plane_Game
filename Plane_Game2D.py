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

#创建Player
player = Actor('player_plane')
player.x = 250
player.y = 650

weapons = []
#创建3个enemy角色
enemy = []
for i in range(3):
    e = Actor('bubu')
    e.x = random.randint(0, 500)
    enemy.append(e)

def draw():
    global counter
    global cooldown
    global Kills
    global time
    screen.blit('星球', [0, 0])
    player.draw()
    #游戏失败之前绘制角色
    if player.image != '失败':
        for w in weapons:
            w.draw()
        for e in enemy:
            e.draw()
#空格键发射子弹   
def on_key_down(key):
    global counter
    global cooldown
    global Kills
    global time
    #鼠标左键发射
    control = mouse.Controller()
    if keyboard.space:
        weapon = Actor('子弹')
        weapon.x = player.x
        weapon.y = player.y - 50
        weapons.append(weapon)
def on_mouse_down():
    global counter
    global cooldown
    global Kills
    global time
    weapon = Actor('子弹')
    weapon.x = player.x
    weapon.y = player.y - 50        
    weapons.append(weapon)


def update():
    global counter
    global cooldown
    global Kills
    global time
    counter += 1
    #Player移动
    if keyboard.left or keyboard.a:
        player.x -= 5
    if keyboard.right or keyboard.d:
        player.x += 5
    if keyboard.up or keyboard.w:
        player.y -= 5
    if keyboard.down or keyboard.s:
        player.y += 5 
    if player.image == '失败':
        print('You Have Killed',Kills)
        print('You Got in',time,'secounds')
        exit()
    #计时
    for e in enemy:
        if counter == 60:
            counter = 0
            time += 1
    #让enemy随机走动
    if e.y >= 150:
        random_num = random.randint(1, 5)
        if random == 1:
            e.x += 2
        else:
            e.x -= 2

    
    #子弹从下向上移动, 到窗口上边缘消失    
    for w in weapons:
        w.y -= 30
    for w in weapons:
        if w.y <= 0:
            weapons.remove(w)
    
    # enemy从上向下移动, 到窗口下边后初始化到窗口上方
    for e in enemy:
        e.y += 5
        if e.y > 700:
            e.x = random.randint(0, 500)
            e.y = 0
    
    #enemy和子弹碰撞后, 回到初始位置
    for e in enemy:
        for w in weapons:
            if e.colliderect(w):
                e.x = random.randint(0, 500)
                e.y = 0
                Kills += 1
                weapons.remove(w)

        
        #enemy碰到Player游戏失败
        if e.colliderect(player) or player.y <= -15 or player.y >= 715 or player.x >= 515 or player.x <= -15:
            player.image = '失败'
            #播放失败音乐
            music.play('faild')

#播放背景音乐
music.play('music1')

os.environ['SDL_VIDEO_CENTERED'] = '1'

pgzrun.go()