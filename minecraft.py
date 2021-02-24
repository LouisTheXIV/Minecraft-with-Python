from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
import random

screen = Ursina()
dirt = "textures/dirt.jpg"
stone = "textures/stone.jpg"
block_pick = 1
sky = "textures/sky.png"
arm_texture = load_texture('textures/arm_texture.png')
copper = "textures/copper.png"
tree = "textures/tree.jpg"
leaf = "textures/leaf.jpg"
#camera.orthographic = True
#camera.fov = 20
window.exit_button.visible = False      
window.fps_counter.enabled = False


def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['left mouse'] or ['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['f1']:
        window.fps_counter.enabled = True
    if held_keys['f2']:
        window.fps_counter.enabled = False
        

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = dirt):
        super().__init__(parent = scene,position = position, texture = texture, model = 'cube',
                         origin_y = 0.5, color = color.color(0,0,random.uniform(0.9,1)), scale=1,
                         highlight_color = color.lime)


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = dirt)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = copper)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = tree)
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = leaf)

                
            if key == 'right mouse down':
                destroy(self)
                

class Hand(Entity):
        def __init__(self):
                super().__init__(
                        parent = camera.ui,
                        model = 'arm',
                        texture = arm_texture,
                        scale = 0.2,rotation = Vec3(150,-10,0),position = Vec2(0.4,-0.6))

        def active(self):
                self.position = Vec2(0.3,-0.5)

        def passive(self):
                self.position = Vec2(0.4,-0.6)
            

Entity(parent = scene, model="sphere", texture="sky", scale=(150), position=(0,0,0), double_sided = True)

tree1 = random.randint(0,1)
tree2 = random.randint(0,1)

for z in range(14):
    for x in range(14):
        Voxel(position = (x,0,z))
        Voxel(position = (x,-1,z))
        Voxel(position = (x,-2,z))
        Voxel(position = (x,-2,z), texture=stone)
        Voxel(position = (x,-3,z), texture=stone)        
        Voxel(position = (x, -4, z,), texture = stone)
        Voxel(position = (x, -5, z,), texture = stone)
        Voxel(position = (x, -6, z,), texture = stone)
        Voxel(position = (x, -7, z,), texture = stone)
        Voxel(position = (x, -8, z,), texture = stone)

for z in range(7):
    for x in range(7):
        f = random.randint(4, 8)
        f = -f
        a = random.randint(0,10)
        s = random.randint(0,10)
        Voxel(position = (a, f, s), texture = copper)

for x in range(1):
    for z in range(1):
        a = random.randint(1,13)
        b = random.randint(1,13)
        c = random.randint(0,1)
        d = random.randint(0,1)

        Voxel(position = (a, 1, b), texture = tree)
        Voxel(position = (a, 2, b), texture = tree)
        Voxel(position = (a, 3, b), texture = tree)
        Voxel(position = (a, 4, b), texture = tree)
        Voxel(position = (a, 5, b), texture = leaf)
        Voxel(position = (a - 1, 5, b + 1), texture = leaf)
        Voxel(position = (a + 1, 5, b - 1), texture = leaf)
        Voxel(position = (a + 1, 5, b + 1), texture = leaf)
        Voxel(position = (a, 6, b), texture = leaf)
        Voxel(position = (a - 1, 6, b), texture = leaf)
        if c == 1:
            Voxel(position = (a, 6, b + 1), texture = leaf)
        else:
            pass
        Voxel(position = (a, 6, b - 1), texture = leaf)
        Voxel(position = (a + 1, 6, b), texture = leaf)
        Voxel(position = (a, 7, b), texture = leaf)
        Voxel(position = (a - 1, 7, b + 1), texture = leaf)
        Voxel(position = (a + 1, 7, b - 1), texture = leaf)
        if d == 1:
            Voxel(position = (a - 1, 7, b - 1), texture = leaf)
        else:
            pass
        Voxel(position = (a, 8, b), texture = leaf)

if tree1 == 1:
    for x in range(1):
        for z in range(1):
            a = random.randint(1,13)
            b = random.randint(1,13)
            c = random.randint(0,1)
            d = random.randint(0,1)

            Voxel(position = (a, 1, b), texture = tree)
            Voxel(position = (a, 2, b), texture = tree)
            Voxel(position = (a, 3, b), texture = tree)
            Voxel(position = (a, 4, b), texture = tree)
            Voxel(position = (a, 5, b), texture = leaf)
            Voxel(position = (a - 1, 5, b + 1), texture = leaf)
            Voxel(position = (a + 1, 5, b - 1), texture = leaf)
            Voxel(position = (a + 1, 5, b + 1), texture = leaf)
            Voxel(position = (a, 6, b), texture = leaf)
            Voxel(position = (a - 1, 6, b), texture = leaf)
            if c == 1:
                Voxel(position = (a, 6, b + 1), texture = leaf)
            else:
                pass
            Voxel(position = (a, 6, b - 1), texture = leaf)
            Voxel(position = (a + 1, 6, b), texture = leaf)
            Voxel(position = (a, 7, b), texture = leaf)
            Voxel(position = (a - 1, 7, b + 1), texture = leaf)
            Voxel(position = (a + 1, 7, b - 1), texture = leaf)
            if d == 1:
                Voxel(position = (a - 1, 7, b - 1), texture = leaf)
            else:
                pass
            Voxel(position = (a, 8, b), texture = leaf)
else:
    pass

if tree2 == 1:
    for x in range(1):
        for z in range(1):
            a = random.randint(1,13)
            b = random.randint(1,13)
            c = random.randint(0,1)
            d = random.randint(0,1)

            Voxel(position = (a, 1, b), texture = tree)
            Voxel(position = (a, 2, b), texture = tree)
            Voxel(position = (a, 3, b), texture = tree)
            Voxel(position = (a, 4, b), texture = tree)
            Voxel(position = (a, 5, b), texture = leaf)
            Voxel(position = (a - 1, 5, b + 1), texture = leaf)
            Voxel(position = (a + 1, 5, b - 1), texture = leaf)
            Voxel(position = (a + 1, 5, b + 1), texture = leaf)
            Voxel(position = (a, 6, b), texture = leaf)
            Voxel(position = (a - 1, 6, b), texture = leaf)
            if c == 1:
                Voxel(position = (a, 6, b + 1), texture = leaf)
            else:
                pass
            Voxel(position = (a, 6, b - 1), texture = leaf)
            Voxel(position = (a + 1, 6, b), texture = leaf)
            Voxel(position = (a, 7, b), texture = leaf)
            Voxel(position = (a - 1, 7, b + 1), texture = leaf)
            Voxel(position = (a + 1, 7, b - 1), texture = leaf)
            if d == 1:
                Voxel(position = (a - 1, 7, b - 1), texture = leaf)
            else:
                pass
            Voxel(position = (a, 8, b), texture = leaf)
else:
    pass


hand = Hand() 
player = FirstPersonController()
screen.run()

