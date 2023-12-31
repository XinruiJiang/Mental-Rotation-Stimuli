from vpython import *
#GlowScript 3.0 VPython

# Prep canvas
scene = canvas(width=1200, height=1200,center=vector(0,0,0))

# Lighting
scene.lights = []
distant_light(direction=vector(.22,.44,.88),color=color.gray(.4))
distant_light(direction=vector(-.88,-.22,-.44),color=color.white)

# Positions of child cubes of each molecule
# Copy the output from 01_converShapes.py here
pss=[[(2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (0, 8, 6), (-2, 8, 6)] ,
    [(2, -2, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (0, 8, 6), (-2, 8, 6)] ,
    [(2, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (0, 8, 6), (-2, 8, 6), (-4, 8, 6)] ,
    [(2, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (0, 8, 6), (-2, 8, 0), (-4, 8, 0)] ,
    [(2, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (-6, 8, 0), (-2, 8, 0), (-4, 8, 0)],
    [(4, 2, 0), (2, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (-2, 8, 0), (-4, 8, 0)] ,
    [(4, 2, 0), (2, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 2, 2), (0, 2, 4), (0, 2, 6), (-2, 8, 0)] ,
    [(4, 2, 0), (2, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 2, 2), (0, 2, 4), (0, 2, 6), (-2, 8, 0), (-4, 8, 0)] ,
    [(4, 2, 0), (2, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (4, 2, 2), (4, 2, 4), (4, 2, 6), (-2, 8, 0), (-4, 8, 0)] ,
    [(4, 2, 6), (2, 2, 6), (0, 2, 6), (0, 4, 6), (0, 6, 6), (0, 8, 6), (4, 2, 2), (4, 2, 4), (4, 2, 6), (-2, 8, 6), (-4, 8, 6)] ,
    [(4, 2, 4), (2, 2, 4), (0, 2, 4), (0, 4, 4), (0, 6, 4), (0, 8, 4), (4, 2, 0), (4, 2, 2), (4, 2, 4), (0, 8, 6), (0, 8, 8)] ,
    [(4, 2, 4), (2, 2, 4), (0, 2, 4), (0, 4, 4), (0, 6, 4), (0, 8, 4), (4, 2, 0), (4, 2, 2), (4, 2, 4), (2, 2, 0), (0, 2, 0)] ,
    [(4, 2, 4), (2, 2, 4), (0, 2, 4), (4, 4, 4), (4, 6, 4), (4, 8, 4), (4, 2, 0), (4, 2, 2), (4, 2, 4), (2, 2, 0), (0, 2, 0)] ,
    [(4, 2, 4), (2, 2, 4), (0, 2, 4), (0, 0, 4), (0, -2, 4), (0, -4, 4), (4, 2, 0), (4, 2, 2), (4, 2, 4), (2, 2, 0), (0, 2, 0)] ,
    [(2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (0, 8, 6), (0, 6, 6)] ,
    [(4, 2, -2), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (0, 8, 6), (0, 6, 6)] ,
    [(4, 2, 2), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (0, 8, 6), (0, 6, 6)] ,
    [(4, 2, -4), (4, 2, -2), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (2, 8, 4)] ,
    [(6, 2, 0), (6, 2, -2), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (2, 8, 4)] ,
    [(6, 2, 0), (6, 2, -2), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4), (-2, 8, 4)] ,
    [(6, 2, 0), (6, 2, -2), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 6, 2), (0, 6, 4), (-2, 6, 4)] ,
    [(6, 2, 0), (6, 2, -2), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 6, 2), (0, 6, 4), (-2, 6, 4), (-4, 6, 4)] ,
    [(6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 6, 2), (0, 6, 4), (-2, 6, 4), (-4, 6, 4)] ,
    [(6, 0, 0), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (0, 8, 4)] ,
    [(6, -2, 0), (6, 0, 0), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2)] ,
    [(6, -2, 0), (6, 0, 0), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (6, -2, 2)] ,
    [(6, -2, 0), (6, 0, 0), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (6, -2, -2)] ,
    [(6, -2, 0), (6, 0, 0), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 6, -2), (0, 6, -4)] ,
    [(6, 4, 0), (6, 6, 0), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 6, -2), (0, 6, -4)] ,
    [(6, 2, 4), (6, 2, 2), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 6, -2), (0, 6, -4)] ,
    [(6, 2, 4), (6, 2, 2), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 0, 0), (0, -2, 0), (0, -2, -2), (0, -2, -4)] ,
    [(6, 0, 2), (6, 0, 0), (6, 2, 0), (2, 2, 0), (4, 2, 0), (0, 2, 0), (0, 0, 0), (0, -2, 0), (0, -2, -2), (0, -2, -4)] ,
    [(2, 2, 0), (4, 2, 0), (4, 0, 0), (4, -2, 0), (0, 2, 0), (0, 4, 6), (0, 6, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, 0, 0), (4, -2, 0), (0, 2, 0), (-2, 2, 6), (-4, 2, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, 0, 0), (4, -2, 0), (0, 2, 0), (-2, 2, 8), (-4, 2, 8), (0, 2, 2), (0, 2, 4), (0, 2, 6), (0, 2, 8)] ,
    [(2, 2, 0), (4, 2, 0), (4, 0, 0), (4, -2, 0), (0, 2, 0), (0, 4, 8), (0, 6, 8), (0, 2, 2), (0, 2, 4), (0, 2, 6), (0, 2, 8)] ,
    [(2, 2, 0), (4, 2, 0), (4, 2, -4), (4, 2, -2), (0, 2, 0), (0, 4, 6), (0, 6, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -4, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (0, 4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -4, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (-2, 2, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -4, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (0, 0, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -4, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (2, 2, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -4, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (2, 2, 6), (4, 2, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (0, 6, 6), (0, 4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (0, 6, 6), (0, 8, 6), (0, 4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (-2, 2, 6), (-4, 2, 6), (-6, 2, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (0, 0, 6), (0, -2, 6), (0, -4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, -2, 0), (4, 0, 0), (0, 2, 0), (2, 2, 6), (4, 2, 6), (6, 2, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, 0, 0), (0, 2, 0), (2, 2, 6), (4, 2, 6), (6, 2, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, 0, 0), (0, 2, 0), (0, 0, 6), (0, -2, 6), (0, -4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, 0, 0), (0, 2, 0), (-2, 2, 6), (-4, 2, 6), (-6, 2, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (4, 0, 0), (0, 2, 0), (0, 6, 6), (0, 8, 6), (0, 4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (0, 0, 0), (0, 2, 0), (0, 6, 6), (0, 8, 6), (0, 4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (-2, 2, 0), (0, 2, 0), (0, 6, 6), (0, 8, 6), (0, 4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (0, 4, 0), (0, 2, 0), (0, 6, 6), (0, 8, 6), (0, 4, 6), (0, 2, 2), (0, 2, 4), (0, 2, 6)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (0, 6, 4), (0, 4, 4), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (0, 6, 4), (0, 4, 4), (0, 2, 2), (0, 2, 4), (6, 2, -2), (6, 2, -4)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (0, 6, 4), (0, 4, 4), (0, 2, 2), (0, 2, 4), (6, 4, 0), (6, 6, 0)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (2, 2, 4), (4, 2, 4), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (-2, 2, 4), (-4, 2, 4), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (0, 0, 4), (0, -2, 4), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (0, 0, 4), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (4, -4, 0)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (0, 0, 4), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (6, -4, -2)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (0, 0, 4), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (8, -4, 0)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (0, 0, 4), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (6, -4, 2)] ,
    [(2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (-2, 2, 4), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (4, -4, 0)] ,
    [(0, 4, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (4, -4, 0)] ,
    [(2, 2, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (4, -4, 0)] ,
    [(-2, 2, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (6, -4, -2)] ,
    [(0, 4, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (6, -4, -2)] ,
    [(2, 2, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (6, -4, -2)] ,
    [(-2, 2, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (8, -4, 0)] ,
    [(0, 4, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (8, -4, 0)] ,
    [(2, 2, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (8, -4, 0)] ,
    [(-2, 2, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (6, -4, 2)] ,
    [(0, 4, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (6, -4, 2)] ,
    [(2, 2, 4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (0, 2, 0), (6, -4, 0), (0, 2, 2), (0, 2, 4), (6, 0, 0), (6, -2, 0), (6, -4, 2)] ,
    [(6, -2, -4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (2, 8, 0), (6, 0, -4), (2, 4, 0), (2, 6, 0), (6, 2, -2), (6, 2, -4)] ,
    [(4, 2, -4), (2, 2, -4), (2, 2, 0), (4, 2, 0), (6, 2, 0), (2, 8, 0), (2, 4, 0), (2, 6, 0), (6, 2, -2), (6, 2, -4)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, -2, 8), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, 0, -2)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 8), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, 0, -2)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 8), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, -2, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 8), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, 2, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, -2, 8), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, 2, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, -2, 8), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, -2, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 4), (0, 4, 4), (0, 6, 4), (-2, 6, 4), (-4, 6, 4), (-4, 6, 2)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 4), (0, 4, 4), (0, 6, 4), (-2, 6, 4), (-4, 6, 4), (-4, 6, 6)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 4), (0, 4, 4), (0, 6, 4), (-2, 6, 4), (-4, 6, 4), (-4, 4, 4)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 4), (0, 4, 4), (0, 6, 4), (-2, 6, 4), (-4, 6, 4), (-4, 8, 4)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, -2), (0, 2, 4), (0, 4, 4), (0, 6, 4), (-2, 6, 4), (-4, 6, 4), (-4, 8, 4)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, -2), (0, 2, 4), (0, 4, 4), (0, 6, 4), (-2, 6, 4), (-4, 6, 4), (-4, 4, 4)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, -2), (0, 2, 4), (0, 4, 4), (0, 6, 4), (-2, 6, 4), (-4, 6, 4), (-4, 6, 6)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, -2), (0, 2, 4), (0, 4, 4), (0, 6, 4), (-2, 6, 4), (-4, 6, 4), (-4, 6, 2)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, -2, 0), (0, -4, 0), (0, -6, 0), (2, -6, 0), (4, -6, 0), (6, -6, 0), (6, -6, -2)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, -2, 0), (0, -4, 0), (0, -6, 0), (2, -6, 0), (4, -6, 0), (6, -6, 0), (6, -6, 2)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, -2, 0), (0, -4, 0), (0, -6, 0), (2, -6, 0), (4, -6, 0), (6, -6, 0), (6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, -2, 0), (0, -4, 0), (0, -6, 0), (2, -6, 0), (4, -6, 0), (6, -6, 0), (6, -8, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, -2, 0), (0, -4, 0), (0, -6, 0), (2, -6, 0), (4, -6, 0), (6, -6, 0), (6, -8, 0), (6, -10, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, -2, 0), (0, -4, 0), (0, -6, 0), (2, -6, 0), (4, -6, 0), (6, -6, 0), (6, -4, 0), (6, -2, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, -2, 0), (0, -4, 0), (0, -6, 0), (2, -6, 0), (4, -6, 0), (6, -6, 0), (6, -6, -4), (6, -6, -2)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (2, 2, 4), (4, 2, 4), (6, 2, 4), (0, 2, 0), (0, 4, 0), (0, 4, -2), (0, 4, -4)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (2, 2, 4), (4, 2, 4), (6, 2, 4), (0, 2, 0), (0, 4, 0), (-2, 4, 0), (-4, 4, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (2, 2, 4), (4, 2, 4), (6, 2, 4), (0, 2, 0), (0, 4, 0), (2, 4, 0), (4, 4, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (2, 2, 4), (4, 2, 4), (6, 2, 4), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (-2, 2, 4), (-4, 2, 4), (-6, 2, 4), (0, 2, 0), (0, 4, 0), (0, 4, -2), (0, 4, -4)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (-2, 2, 4), (-4, 2, 4), (-6, 2, 4), (0, 2, 0), (0, 4, 0), (-2, 4, 0), (-4, 4, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (-2, 2, 4), (-4, 2, 4), (-6, 2, 4), (0, 2, 0), (0, 4, 0), (2, 4, 0), (4, 4, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (-2, 2, 4), (-4, 2, 4), (-6, 2, 4), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (0, 2, 6), (2, 2, 6), (4, 2, 6), (6, 2, 6), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (0, 2, 6), (2, 2, 6), (4, 2, 6), (6, 2, 6), (0, 2, 0), (0, 4, 0), (-2, 4, 0), (-4, 4, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (0, 2, 6), (2, 2, 6), (4, 2, 6), (6, 2, 6), (0, 2, 0), (0, 4, 0), (2, 4, 0), (4, 4, 0)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (0, 2, 6), (2, 2, 6), (4, 2, 6), (6, 2, 6), (0, 2, 0), (0, 4, 0), (0, 4, -2), (0, 4, -4)] ,
    [(0, 0, 0), (0, 2, 2), (0, 2, 4), (0, 2, 6), (-2, 2, 6), (-4, 2, 6), (-6, 2, 6), (0, 2, 0), (0, 4, 0), (0, 4, -2), (0, 4, -4)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (2, 0, 2), (2, 0, 4), (2, 0, 6), (6, 0, -2), (6, -2, -2), (6, -4, -2)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (2, 0, 2), (2, 0, 4), (2, 0, 6), (6, 0, -2), (6, 2, -2), (6, 4, -2)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, 0, 2), (6, 0, 4), (6, 0, 6), (6, 0, -2), (6, 2, -2), (6, 4, -2)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, 0, 2), (6, 0, 4), (6, 0, 6), (6, 0, -2), (6, -2, -2), (6, -4, -2)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, 0, 2), (6, 0, 4), (6, 0, 6), (6, -2, 2), (6, -4, 2), (6, -6, 2), (6, -8, 2)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (6, 0, 2), (6, 0, 4), (6, 0, 6), (6, 2, 2), (6, 4, 2), (6, 6, 2), (6, 8, 2)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (-2, 0, 0), (-4, 0, 0), (2, 8, 0), (4, 8, 0), (6, 8, 0), (6, 8, 2)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (-2, 0, 0), (-4, 0, 0), (2, 8, 0), (4, 8, 0), (6, 8, 0), (6, 8, -2)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, 2), (-2, 0, 0), (-4, 0, 0), (2, 8, 0), (4, 8, 0), (6, 8, 0)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (0, 8, -2), (-2, 0, 0), (-4, 0, 0), (2, 8, 0), (4, 8, 0), (6, 8, 0)] ,
    [(0, 0, 2), (0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (-2, 0, 0), (-4, 0, 0), (2, 8, 0), (4, 8, 0), (6, 8, 0)] ,
    [(0, 0, -2), (0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (-2, 0, 0), (-4, 0, 0), (2, 8, 0), (4, 8, 0), (6, 8, 0)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (-2, 0, 0), (-4, 0, 0), (-4, 0, 2), (2, 8, 0), (4, 8, 0), (6, 8, 0)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (0, 8, 0), (-2, 0, 0), (-4, 0, 0), (-4, 0, -2), (2, 8, 0), (4, 8, 0), (6, 8, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, -2, 8), (0, -4, 8), (-2, 0, 0), (-4, 0, 0), (-4, 2, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, -2, 8), (0, -4, 8), (-2, 0, 0), (-4, 0, 0), (-4, -2, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, -2, 8), (-2, 0, 0), (-4, 0, 0), (-4, -2, 0), (-4, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, -2, 8), (-2, 0, 0), (-4, 0, 0), (-4, 2, 0), (-4, 4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, -2, 8), (0, -4, 8), (-2, 0, 0), (-4, 0, 0), (-4, 2, 0), (-4, 4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 8), (0, 4, 8), (-2, 0, 0), (-4, 0, 0), (-4, 2, 0), (-4, 4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 0, 8), (0, 2, 8), (0, 4, 8), (-2, 0, 0), (-4, 0, 0), (-4, -2, 0), (-4, -4, 0)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, 2, 0), (0, 4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (6, -2, -6)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, 2, 0), (0, 4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (6, 2, -6)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, -2, 0), (0, -4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (6, 2, -6)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, -2, 0), (0, -4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (6, -2, -6)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, -2, 0), (0, -4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (8, 0, -6)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, -2, 0), (0, -4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (4, 0, -6)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, 2, 0), (0, 4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (4, 0, -6)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, 2, 0), (0, 4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (8, 0, -6)] ,
    [(0, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0), (0, 2, 0), (0, 4, 0), (6, 0, -2), (6, 0, -4), (6, 0, -6), (6, -2, -6)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (2, 0, 4), (2, 0, 6), (0, -2, 0), (0, -4, 0), (2, -4, 0), (4, -4, 0), (6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (2, 0, 4), (2, 0, 6), (0, -2, 0), (0, -4, 0), (-2, -4, 0), (-4, -4, 0), (-6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (2, 0, 4), (0, 0, 6), (0, -2, 0), (0, -4, 0), (-2, -4, 0), (-4, -4, 0), (-6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (2, 0, 4), (0, 0, 6), (0, -2, 0), (0, -4, 0), (2, -4, 0), (4, -4, 0), (6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (2, 0, 4), (0, 2, 4), (0, -2, 0), (0, -4, 0), (2, -4, 0), (4, -4, 0), (6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (2, 0, 4), (0, 2, 4), (0, -2, 0), (0, -4, 0), (-2, -4, 0), (-4, -4, 0), (-6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (-2, 0, 4), (0, 2, 4), (0, -2, 0), (0, -4, 0), (-2, -4, 0), (-4, -4, 0), (-6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (-2, 0, 4), (0, 2, 4), (0, -2, 0), (0, -4, 0), (2, -4, 0), (4, -4, 0), (6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (-2, 0, 4), (0, -2, 4), (0, -2, 0), (0, -4, 0), (2, -4, 0), (4, -4, 0), (6, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (-2, 0, 4), (0, -2, 4), (0, -2, 0), (0, -4, 0), (-2, -4, 0), (-4, -4, 0), (-6, -4, 0)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (-2, 0, 0), (-4, 0, 0), (-4, 0, 2), (-4, 0, 4), (-4, 0, 6), (0, 6, -2), (0, 6, -4)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (-2, 0, 0), (-4, 0, 0), (-4, 0, -2), (-4, 0, -4), (-4, 0, -6), (0, 6, 2), (0, 6, 4)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (-2, 0, 0), (-4, 0, 0), (-4, 0, -2), (-4, 0, -4), (-4, 0, -6), (0, 0, 2), (0, 0, 4)] ,
    [(0, 0, 0), (0, 2, 0), (0, 4, 0), (0, 6, 0), (-2, 0, 0), (-4, 0, 0), (-4, 0, 2), (-4, 0, 4), (-4, 0, 6), (0, 0, -2), (0, 0, -4)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (2, 0, 6), (4, 0, 6), (4, 0, 8), (4, 0, 10), (0, -2, 0), (0, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (2, 0, 6), (4, 0, 6), (4, 0, 8), (4, 0, 10), (0, 2, 0), (0, 4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (2, 0, 6), (4, 0, 6), (4, 0, 8), (4, 0, 10), (4, 0, 12), (0, 2, 0), (0, 4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (2, 0, 6), (4, 0, 6), (4, 0, 8), (4, 0, 10), (4, 0, 12), (0, -2, 0), (0, -4, 0)] ,
    [(0, 0, 0), (0, 0, 2), (0, 0, 4), (0, 0, 6), (0, 2, 6), (2, 0, 0), (4, 0, 0), (6, 0, 0), (8, 0, 0), (8, 2, 0)] ,
    [(2, 0, 2), (2, 0, 4), (2, 0, 6), (2, 2, 6), (2, 0, 0), (4, 0, 0), (6, 0, 0), (8, 0, 0), (8, -2, 0), (8, -4, 0)]]

# Rotate by
rotateBy=5
refreshRate=5
    
# Draw cubes and rotate around Z axis
n=0
for ps in pss:
    n=n+1
    if n<=1:
        # Draw cubes
        cubes=[]
        x=[]
        y=[]
        for p in ps:
            x1=p[0]
            y1=p[1]
            z1=p[2]
            # Align axis with cube
            x2=x1*cos(pi/(180/45))-y1*sin(pi/(180/45))
            y2=x1*sin(pi/(180/45))+y1*cos(pi/(180/45))
            z2=z1
            x3=x2
            y3=-y2*cos(pi/(180/90))+z2*sin(pi/(180/90))
            z3=-y2*sin(pi/(180/90))-z2*cos(pi/(180/90))
            x.append(x3)
            y.append(y3)
            # Draw cubes
            my_cube=box(pos=vector(x3,y3,z3),axis=vector(1,0,1),size=vector(2,2,2))
            cubes.append(my_cube)
        cubes=compound(cubes,texture="https://i.imgur.com/FcYoC8w.jpg")
        scene.autoscale=False
        scene.camera.pos=vector((min(x)+max(x))/2,(min(y)+max(y))/2+23.2885-7,23.2885)# Check scene.camera.pos to determine the number
        scene.camera.axis=vector(0,-(23.2885-8),-23.2885)
        scene.capture(n+'_X_0_a.png')
        scene.capture(n+'_Z_0_a.png')
     
        # Rotate
        for r in range(1,int(360/rotateBy)):
            rate(refreshRate)
            # Rotate around x axis
            cubes.rotate(angle=pi/(180/rotateBy),axis=vector(1,0,0))
            scene.capture(n+'_X_'+str(r*rotateBy)+'_a.png')
        # Return to original position
        cubes.rotate(angle=pi/(180/rotateBy),axis=vector(1,0,0))
        scene.capture(n+'_X_360_a.png')
        
        for r in range(1,int(360/rotateBy)):
            rate(refreshRate)
            # Rotate around Z axis
            cubes.rotate(angle=-pi/(180/rotateBy),axis=vector(0,1,0))
            scene.capture(n+'_Z_'+str(r*rotateBy)+'_a.png')
        # Return to original position
        cubes.rotate(angle=-pi/(180/rotateBy),axis=vector(0,1,0))
        scene.capture(n+'_Z_360_a.png')
        
        # Clear canvas
        cubes.visible=False
        del cubes 
