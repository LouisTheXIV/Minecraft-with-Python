from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
import random
import asyncio

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

player = FirstPersonController()

def update():
    playerX = round(player.x)
    playerY = round(player.y)
    playerZ = round(player.z)
    if playerZ == 5 and held_keys['z']:
        createChunk(5)
    if playerZ == 10 and held_keys['z']:
        createChunk(10)
    if playerZ == 15 and held_keys['z']:
        createChunk(15)
    if playerZ == 20 and held_keys['z']:
        createChunk(20)
        
##    if held_keys['f2']:
##        Text(f"X: {playerX}", scale = 1.5, color = color.black, y=.5, x=-.40)
##        Text(f"Y: {playerY}", scale = 1.5, color = color.black)
##        Text(f"Z: {playerZ}", scale = 1.5, color = color.black)
    if held_keys['f2']:
        print(f"X: {playerX} Y:{playerY} Z:{playerZ}")
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

def saveChunk(chunkName):
    file = open(f"chunk{chunkName}.chunk", "w")
    file.write("5")
    file.close()
    

def createChunk(num):
    tree1 = random.randint(0,1)
    tree2 = random.randint(0,1)

    for z in range(6):
        for x in range(6):
            Voxel(position = (x,0,z+num))
            Voxel(position = (x,-1,z+num))
            Voxel(position = (x,-2,z+num))
            Voxel(position = (x,-2,z+num), texture=stone)
            Voxel(position = (x,-3,z+num), texture=stone)        
            Voxel(position = (x, -4, z+num,), texture = stone)
            Voxel(position = (x, -5, z+num,), texture = stone)
            Voxel(position = (x, -6, z+num,), texture = stone)
            Voxel(position = (x, -7, z+num,), texture = stone)
            Voxel(position = (x, -8, z+num,), texture = stone)

    for z in range(3):
        for x in range(3):
            f = random.randint(4, 8)
            f = -f
            a = random.randint(0,5)
            s = random.randint(0,5)
            Voxel(position = (a, f, s+num), texture = copper)
    
    if tree1 == 1:
        for x in range(1):
            for z in range(1):
                a = random.randint(1,5)
                b1 = random.randint(1,5)
                b = b1 +num
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

    if tree2 == 1:
        for x in range(1):
            for z in range(1):
                a = random.randint(1,5)
                b1 = random.randint(1,5)
                b = b1 +num
                c1 = random.randint(0,1)
                d1 = random.randint(0,1)

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
                if c1 == 1:
                    Voxel(position = (a, 6, b + 1), texture = leaf)
                else:
                    pass
                Voxel(position = (a, 6, b - 1), texture = leaf)
                Voxel(position = (a + 1, 6, b), texture = leaf)
                Voxel(position = (a, 7, b), texture = leaf)
                Voxel(position = (a - 1, 7, b + 1), texture = leaf)
                Voxel(position = (a + 1, 7, b - 1), texture = leaf)
                if d1 == 1:
                    Voxel(position = (a - 1, 7, b - 1), texture = leaf)
                else:
                    pass
                Voxel(position = (a, 8, b), texture = leaf)
    else:
        pass


createChunk(0)
hand = Hand() 

screen.run()

