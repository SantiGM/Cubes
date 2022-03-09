import pygame
import math
import time
import solver

class Colors:
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    blue = (0,0,255)
    green = (0,255,0)
    yellow = (255,255,0)
    orange = (255,102,0)
    grey = (220,220,220)

class Moves:
    U = 0
    Up = 1
    D = 2
    Dp = 3
    F = 4
    Fp = 5
    B = 6
    Bp = 7
    L = 8
    Lp = 9
    R = 10
    Rp = 11
    M_RL = 12 # hacia abajo
    M_RLp = 13 # hacia arriba
    M_FB = 14 # hacia derecha
    M_FBp = 15 #hacia izquierda
    M_UD = 16 # hacia derecha
    M_UDp = 17 # hacia izquierda

class Mouse:

    def __init__(self):
        self.prev_X = 0
        self.prev_Y = 0
        self.new_X = 0
        self.new_Y = 0

WIDTH = 1000
HEIGHT = 600

DEG_TO_RAD_30 = 30*math.pi/180

change = 0

class Cube:

    def __init__(self,x,y,len,color_L,color_F,color_U,color_R,color_B,color_D):
        self.x = x
        self.y = y
        self.len = len
        self.color_L = color_L
        self.color_F = color_F
        self.color_U = color_U
        self.color_R = color_R
        self.color_B = color_B
        self.color_D = color_D

        self.point1 = 0
        self.point2 = 0
        self.point3 = 0
        self.point4 = 0
        self.point5 = 0
        self.point6 = 0
        self.point7 = 0

    def update_points(self):
        self.point1 = (self.x - self.len*math.cos(DEG_TO_RAD_30), self.y - self.len*math.sin(DEG_TO_RAD_30))
        self.point2 = (self.x - self.len*math.cos(DEG_TO_RAD_30), self.y - self.len - self.len*math.sin(DEG_TO_RAD_30))
        self.point3 = (self.x, self.y)
        self.point4 = (self.x, self.y - self.len)
        self.point5 = (self.x, self.y - self.len - 2*self.len*math.sin(DEG_TO_RAD_30))
        self.point6 = (self.x + self.len*math.cos(DEG_TO_RAD_30), self.y - self.len*math.sin(DEG_TO_RAD_30))
        self.point7 = (self.x + self.len*math.cos(DEG_TO_RAD_30), self.y - self.len - self.len*math.sin(DEG_TO_RAD_30))

    def draw(self, screen):

        self.update_points()

        #Left Face
        pygame.draw.polygon(screen, self.color_L, [self.point1,self.point2,self.point4,self.point3])

        #Front Face
        pygame.draw.polygon(screen, self.color_F, [self.point3,self.point4,self.point7,self.point6])

        #Top Face
        pygame.draw.polygon(screen,self.color_U, [self.point2,self.point5,self.point7,self.point4])


        #center vertical
        pygame.draw.line(screen, Colors.grey, self.point3, self.point4,3)

        #center to right top
        pygame.draw.line(screen, Colors.grey, self.point4,self.point7,3)

        #right vertical
        pygame.draw.line(screen, Colors.grey, self.point7, self.point6,3)

        #center to right bottom
        pygame.draw.line(screen, Colors.grey, self.point3,self.point6,3)

        #center to left bottom
        pygame.draw.line(screen, Colors.grey, self.point3,self.point1,3)

        #center to left top
        pygame.draw.line(screen, Colors.grey, self.point4,self.point2,3)

        #left vertical
        pygame.draw.line(screen, Colors.grey, self.point1, self.point2,3)

        #left to center
        pygame.draw.line(screen, Colors.grey, self.point2, self.point5,3)

        #right to center
        pygame.draw.line(screen, Colors.grey, self.point5,self.point7,3)

        pygame.display.flip()

def Create_Cube_grid(x, y, length, grid_length, grid_width, grid_height, color_L, color_F, color_U,color_R,color_B,color_D):

    cube_array = []

    for h in range(grid_height):
        cube_array.append([])
        for w in range(grid_width):
            cube_array[h].append([])
            for l in range(grid_length):
                cube_array[h][w].append(Cube(x + (length*math.cos(DEG_TO_RAD_30))*l + (length*math.cos(DEG_TO_RAD_30))*w, y + (length*math.sin(DEG_TO_RAD_30))*l - (length*math.sin(DEG_TO_RAD_30))*w - length*h, length, color_L, color_F, color_U, color_R, color_B, color_D))
                cube_array[h][w][l].update_points()

    return cube_array

def Print_Cube_Array(cube_array, height, width, length):

    for h in range(height):
        for w in range(width):
            for l in range(length):
                cube_array[h][width-1-w][l].draw(gameDisplay)

    pass

def Move_Cubes(cube_array, move):

    if(move == Moves.U):

        cube_array[-1][0][1].color_L, cube_array[-1][1][-1].color_F, cube_array[-1][-1][1].color_R, cube_array[-1][1][0].color_B, cube_array[-1][0][0].color_L, cube_array[-1][0][0].color_B, \
        cube_array[-1][0][-1].color_L, cube_array[-1][0][-1].color_F, cube_array[-1][-1][-1].color_F, cube_array[-1][-1][-1].color_R, cube_array[-1][-1][0].color_R, cube_array[-1][-1][0].color_B, \
        cube_array[-1][0][0].color_U, cube_array[-1][0][-1].color_U, cube_array[-1][-1][-1].color_U, cube_array[-1][-1][0].color_U, cube_array[-1][0][1].color_U, cube_array[-1][1][-1].color_U, \
        cube_array[-1][-1][1].color_U, cube_array[-1][1][0].color_U = \
        cube_array[-1][1][-1].color_F, cube_array[-1][-1][1].color_R, cube_array[-1][1][0].color_B, cube_array[-1][0][1].color_L, cube_array[-1][0][-1].color_F, cube_array[-1][0][-1].color_L, \
        cube_array[-1][-1][-1].color_F, cube_array[-1][-1][-1].color_R, cube_array[-1][-1][0].color_R, cube_array[-1][-1][0].color_B, cube_array[-1][0][0].color_B, cube_array[-1][0][0].color_L, \
        cube_array[-1][0][-1].color_U, cube_array[-1][-1][-1].color_U, cube_array[-1][-1][0].color_U, cube_array[-1][0][0].color_U, cube_array[-1][1][-1].color_U, cube_array[-1][-1][1].color_U, \
        cube_array[-1][1][0].color_U, cube_array[-1][0][1].color_U

    elif(move == Moves.Up):

        cube_array[-1][1][-1].color_F, cube_array[-1][-1][1].color_R, cube_array[-1][1][0].color_B, cube_array[-1][0][1].color_L, cube_array[-1][0][-1].color_F, cube_array[-1][0][-1].color_L, \
        cube_array[-1][-1][-1].color_F, cube_array[-1][-1][-1].color_R, cube_array[-1][-1][0].color_R, cube_array[-1][-1][0].color_B, cube_array[-1][0][0].color_B, cube_array[-1][0][0].color_L, \
        cube_array[-1][0][-1].color_U, cube_array[-1][-1][-1].color_U, cube_array[-1][-1][0].color_U, cube_array[-1][0][0].color_U, cube_array[-1][1][-1].color_U, cube_array[-1][-1][1].color_U, \
        cube_array[-1][1][0].color_U, cube_array[-1][0][1].color_U = \
        cube_array[-1][0][1].color_L, cube_array[-1][1][-1].color_F, cube_array[-1][-1][1].color_R, cube_array[-1][1][0].color_B, cube_array[-1][0][0].color_L, cube_array[-1][0][0].color_B, \
        cube_array[-1][0][-1].color_L, cube_array[-1][0][-1].color_F, cube_array[-1][-1][-1].color_F, cube_array[-1][-1][-1].color_R, cube_array[-1][-1][0].color_R, cube_array[-1][-1][0].color_B, \
        cube_array[-1][0][0].color_U, cube_array[-1][0][-1].color_U, cube_array[-1][-1][-1].color_U, cube_array[-1][-1][0].color_U, cube_array[-1][0][1].color_U, cube_array[-1][1][-1].color_U, \
        cube_array[-1][-1][1].color_U, cube_array[-1][1][0].color_U

    elif(move == Moves.D):
        
        cube_array[0][1][-1].color_F, cube_array[0][-1][1].color_R, cube_array[0][1][0].color_B, cube_array[0][0][1].color_L, cube_array[0][0][-1].color_F, cube_array[0][0][-1].color_L, \
        cube_array[0][-1][-1].color_F, cube_array[0][-1][-1].color_R, cube_array[0][-1][0].color_R, cube_array[0][-1][0].color_B, cube_array[0][0][0].color_B, cube_array[0][0][0].color_L, \
        cube_array[0][0][-1].color_D, cube_array[0][-1][-1].color_D, cube_array[0][-1][0].color_D, cube_array[0][0][0].color_D, cube_array[0][1][-1].color_D, cube_array[0][-1][1].color_D, \
        cube_array[0][1][0].color_D, cube_array[0][0][1].color_D = \
        cube_array[0][0][1].color_L, cube_array[0][1][-1].color_F, cube_array[0][-1][1].color_R, cube_array[0][1][0].color_B, cube_array[0][0][0].color_L, cube_array[0][0][0].color_B, \
        cube_array[0][0][-1].color_L, cube_array[0][0][-1].color_F, cube_array[0][-1][-1].color_F, cube_array[0][-1][-1].color_R, cube_array[0][-1][0].color_R, cube_array[0][-1][0].color_B, \
        cube_array[0][0][0].color_D, cube_array[0][0][-1].color_D, cube_array[0][-1][-1].color_D, cube_array[0][-1][0].color_D, cube_array[0][0][1].color_D, cube_array[0][1][-1].color_D, \
        cube_array[0][-1][1].color_D, cube_array[0][1][0].color_D

    elif(move == Moves.Dp):

        cube_array[0][0][1].color_L, cube_array[0][1][-1].color_F, cube_array[0][-1][1].color_R, cube_array[0][1][0].color_B, cube_array[0][0][0].color_L, cube_array[0][0][0].color_B, \
        cube_array[0][0][-1].color_L, cube_array[0][0][-1].color_F, cube_array[0][-1][-1].color_F, cube_array[0][-1][-1].color_R, cube_array[0][-1][0].color_R, cube_array[0][-1][0].color_B, \
        cube_array[0][0][0].color_D, cube_array[0][0][-1].color_D, cube_array[0][-1][-1].color_D, cube_array[0][-1][0].color_D, cube_array[0][0][1].color_D, cube_array[0][1][-1].color_D, \
        cube_array[0][-1][1].color_D, cube_array[0][1][0].color_D = \
        cube_array[0][1][-1].color_F, cube_array[0][-1][1].color_R, cube_array[0][1][0].color_B, cube_array[0][0][1].color_L, cube_array[0][0][-1].color_F, cube_array[0][0][-1].color_L, \
        cube_array[0][-1][-1].color_F, cube_array[0][-1][-1].color_R, cube_array[0][-1][0].color_R, cube_array[0][-1][0].color_B, cube_array[0][0][0].color_B, cube_array[0][0][0].color_L, \
        cube_array[0][0][-1].color_D, cube_array[0][-1][-1].color_D, cube_array[0][-1][0].color_D, cube_array[0][0][0].color_D, cube_array[0][1][-1].color_D, cube_array[0][-1][1].color_D, \
        cube_array[0][1][0].color_D, cube_array[0][0][1].color_D
        
    elif(move == Moves.F):
        
        cube_array[-1][1][-1].color_U, cube_array[1][-1][-1].color_R, cube_array[0][1][-1].color_D, cube_array[1][0][-1].color_L, cube_array[-1][1][-1].color_F, cube_array[1][-1][-1].color_F, \
        cube_array[0][1][-1].color_F, cube_array[1][0][-1].color_F, cube_array[-1][0][-1].color_U, cube_array[-1][-1][-1].color_R, cube_array[0][-1][-1].color_D, cube_array[0][0][-1].color_L, \
        cube_array[-1][0][-1].color_L, cube_array[-1][-1][-1].color_U, cube_array[0][-1][-1].color_R, cube_array[0][0][-1].color_D, cube_array[-1][0][-1].color_F, cube_array[-1][-1][-1].color_F, \
        cube_array[0][-1][-1].color_F, cube_array[0][0][-1].color_F = \
        cube_array[1][0][-1].color_L, cube_array[-1][1][-1].color_U, cube_array[1][-1][-1].color_R, cube_array[0][1][-1].color_D, cube_array[1][0][-1].color_F, cube_array[-1][1][-1].color_F, \
        cube_array[1][-1][-1].color_F, cube_array[0][1][-1].color_F, cube_array[0][0][-1].color_L, cube_array[-1][0][-1].color_U, cube_array[-1][-1][-1].color_R, cube_array[0][-1][-1].color_D, \
        cube_array[0][0][-1].color_D, cube_array[-1][0][-1].color_L, cube_array[-1][-1][-1].color_U, cube_array[0][-1][-1].color_R, cube_array[0][0][-1].color_F, cube_array[-1][0][-1].color_F, \
        cube_array[-1][-1][-1].color_F, cube_array[0][-1][-1].color_F

    elif(move == Moves.Fp):

        cube_array[1][0][-1].color_L, cube_array[-1][1][-1].color_U, cube_array[1][-1][-1].color_R, cube_array[0][1][-1].color_D, cube_array[1][0][-1].color_F, cube_array[-1][1][-1].color_F, \
        cube_array[1][-1][-1].color_F, cube_array[0][1][-1].color_F, cube_array[0][0][-1].color_L, cube_array[-1][0][-1].color_U, cube_array[-1][-1][-1].color_R, cube_array[0][-1][-1].color_D, \
        cube_array[0][0][-1].color_D, cube_array[-1][0][-1].color_L, cube_array[-1][-1][-1].color_U, cube_array[0][-1][-1].color_R, cube_array[0][0][-1].color_F, cube_array[-1][0][-1].color_F, \
        cube_array[-1][-1][-1].color_F, cube_array[0][-1][-1].color_F = \
        cube_array[-1][1][-1].color_U, cube_array[1][-1][-1].color_R, cube_array[0][1][-1].color_D, cube_array[1][0][-1].color_L, cube_array[-1][1][-1].color_F, cube_array[1][-1][-1].color_F, \
        cube_array[0][1][-1].color_F, cube_array[1][0][-1].color_F, cube_array[-1][0][-1].color_U, cube_array[-1][-1][-1].color_R, cube_array[0][-1][-1].color_D, cube_array[0][0][-1].color_L, \
        cube_array[-1][0][-1].color_L, cube_array[-1][-1][-1].color_U, cube_array[0][-1][-1].color_R, cube_array[0][0][-1].color_D, cube_array[-1][0][-1].color_F, cube_array[-1][-1][-1].color_F, \
        cube_array[0][-1][-1].color_F, cube_array[0][0][-1].color_F

    elif(move == Moves.B):
        
        cube_array[1][0][0].color_L, cube_array[-1][1][0].color_U, cube_array[1][-1][0].color_R, cube_array[0][1][0].color_D, cube_array[1][0][0].color_B, cube_array[-1][1][0].color_B, \
        cube_array[1][-1][0].color_B, cube_array[0][1][0].color_B, cube_array[0][0][0].color_L, cube_array[-1][0][0].color_U, cube_array[-1][-1][0].color_R, cube_array[0][-1][0].color_D, \
        cube_array[0][0][0].color_D, cube_array[-1][0][0].color_L, cube_array[-1][-1][0].color_U, cube_array[0][-1][0].color_R, cube_array[0][0][0].color_B, cube_array[-1][0][0].color_B, \
        cube_array[-1][-1][0].color_B, cube_array[0][-1][0].color_B = \
        cube_array[-1][1][0].color_U, cube_array[1][-1][0].color_R, cube_array[0][1][0].color_D, cube_array[1][0][0].color_L, cube_array[-1][1][0].color_B, cube_array[1][-1][0].color_B, \
        cube_array[0][1][0].color_B, cube_array[1][0][0].color_B, cube_array[-1][0][0].color_U, cube_array[-1][-1][0].color_R, cube_array[0][-1][0].color_D, cube_array[0][0][0].color_L, \
        cube_array[-1][0][0].color_L, cube_array[-1][-1][0].color_U, cube_array[0][-1][0].color_R, cube_array[0][0][0].color_D, cube_array[-1][0][0].color_B, cube_array[-1][-1][0].color_B, \
        cube_array[0][-1][0].color_B, cube_array[0][0][0].color_B

    elif(move == Moves.Bp):
        
        cube_array[-1][1][0].color_U, cube_array[1][-1][0].color_R, cube_array[0][1][0].color_D, cube_array[1][0][0].color_L, cube_array[-1][1][0].color_B, cube_array[1][-1][0].color_B, \
        cube_array[0][1][0].color_B, cube_array[1][0][0].color_B, cube_array[-1][0][0].color_U, cube_array[-1][-1][0].color_R, cube_array[0][-1][0].color_D, cube_array[0][0][0].color_L, \
        cube_array[-1][0][0].color_L, cube_array[-1][-1][0].color_U, cube_array[0][-1][0].color_R, cube_array[0][0][0].color_D, cube_array[-1][0][0].color_B, cube_array[-1][-1][0].color_B, \
        cube_array[0][-1][0].color_B, cube_array[0][0][0].color_B = \
        cube_array[1][0][0].color_L, cube_array[-1][1][0].color_U, cube_array[1][-1][0].color_R, cube_array[0][1][0].color_D, cube_array[1][0][0].color_B, cube_array[-1][1][0].color_B, \
        cube_array[1][-1][0].color_B, cube_array[0][1][0].color_B, cube_array[0][0][0].color_L, cube_array[-1][0][0].color_U, cube_array[-1][-1][0].color_R, cube_array[0][-1][0].color_D, \
        cube_array[0][0][0].color_D, cube_array[-1][0][0].color_L, cube_array[-1][-1][0].color_U, cube_array[0][-1][0].color_R, cube_array[0][0][0].color_B, cube_array[-1][0][0].color_B, \
        cube_array[-1][-1][0].color_B, cube_array[0][-1][0].color_B

    elif(move == Moves.L):
        
        cube_array[-1][0][1].color_U, cube_array[1][0][-1].color_F, cube_array[0][0][1].color_D, cube_array[1][0][0].color_B, cube_array[-1][0][-1].color_U, cube_array[0][0][-1].color_F, \
        cube_array[0][0][0].color_D, cube_array[-1][0][0].color_B, cube_array[-1][0][-1].color_F, cube_array[0][0][-1].color_D, cube_array[0][0][0].color_B, cube_array[-1][0][0].color_U, \
        cube_array[-1][0][-1].color_L, cube_array[0][0][-1].color_L, cube_array[0][0][0].color_L, cube_array[-1][0][0].color_L, cube_array[-1][0][1].color_L, cube_array[1][0][-1].color_L, \
        cube_array[0][0][1].color_L, cube_array[1][0][0].color_L = \
        cube_array[1][0][0].color_B, cube_array[-1][0][1].color_U, cube_array[1][0][-1].color_F, cube_array[0][0][1].color_D, cube_array[-1][0][0].color_B, cube_array[-1][0][-1].color_U, \
        cube_array[0][0][-1].color_F, cube_array[0][0][0].color_D, cube_array[-1][0][0].color_U, cube_array[-1][0][-1].color_F, cube_array[0][0][-1].color_D, cube_array[0][0][0].color_B, \
        cube_array[-1][0][0].color_L, cube_array[-1][0][-1].color_L, cube_array[0][0][-1].color_L, cube_array[0][0][0].color_L, cube_array[1][0][0].color_L, cube_array[-1][0][1].color_L, \
        cube_array[1][0][-1].color_L, cube_array[0][0][1].color_L

    elif(move == Moves.Lp):

        cube_array[1][0][0].color_B, cube_array[-1][0][1].color_U, cube_array[1][0][-1].color_F, cube_array[0][0][1].color_D, cube_array[-1][0][0].color_B, cube_array[-1][0][-1].color_U, \
        cube_array[0][0][-1].color_F, cube_array[0][0][0].color_D, cube_array[-1][0][0].color_U, cube_array[-1][0][-1].color_F, cube_array[0][0][-1].color_D, cube_array[0][0][0].color_B, \
        cube_array[-1][0][0].color_L, cube_array[-1][0][-1].color_L, cube_array[0][0][-1].color_L, cube_array[0][0][0].color_L, cube_array[1][0][0].color_L, cube_array[-1][0][1].color_L, \
        cube_array[1][0][-1].color_L, cube_array[0][0][1].color_L = \
        cube_array[-1][0][1].color_U, cube_array[1][0][-1].color_F, cube_array[0][0][1].color_D, cube_array[1][0][0].color_B, cube_array[-1][0][-1].color_U, cube_array[0][0][-1].color_F, \
        cube_array[0][0][0].color_D, cube_array[-1][0][0].color_B, cube_array[-1][0][-1].color_F, cube_array[0][0][-1].color_D, cube_array[0][0][0].color_B, cube_array[-1][0][0].color_U, \
        cube_array[-1][0][-1].color_L, cube_array[0][0][-1].color_L, cube_array[0][0][0].color_L, cube_array[-1][0][0].color_L, cube_array[-1][0][1].color_L, cube_array[1][0][-1].color_L, \
        cube_array[0][0][1].color_L, cube_array[1][0][0].color_L

    elif(move == Moves.R):
        
        cube_array[1][-1][0].color_B, cube_array[-1][-1][1].color_U, cube_array[1][-1][-1].color_F, cube_array[0][-1][1].color_D, cube_array[-1][-1][0].color_B, cube_array[-1][-1][-1].color_U, \
        cube_array[0][-1][-1].color_F, cube_array[0][-1][0].color_D, cube_array[-1][-1][0].color_U, cube_array[-1][-1][-1].color_F, cube_array[0][-1][-1].color_D, cube_array[0][-1][0].color_B, \
        cube_array[-1][-1][0].color_R, cube_array[-1][-1][-1].color_R, cube_array[0][-1][-1].color_R, cube_array[0][-1][0].color_R, cube_array[1][-1][0].color_R, cube_array[-1][-1][1].color_R, \
        cube_array[1][-1][-1].color_R, cube_array[0][-1][1].color_R = \
        cube_array[-1][-1][1].color_U, cube_array[1][-1][-1].color_F, cube_array[0][-1][1].color_D, cube_array[1][-1][0].color_B, cube_array[-1][-1][-1].color_U, cube_array[0][-1][-1].color_F, \
        cube_array[0][-1][0].color_D, cube_array[-1][-1][0].color_B, cube_array[-1][-1][-1].color_F, cube_array[0][-1][-1].color_D, cube_array[0][-1][0].color_B, cube_array[-1][-1][0].color_U, \
        cube_array[-1][-1][-1].color_R, cube_array[0][-1][-1].color_R, cube_array[0][-1][0].color_R, cube_array[-1][-1][0].color_R, cube_array[-1][-1][1].color_R, cube_array[1][-1][-1].color_R, \
        cube_array[0][-1][1].color_R, cube_array[1][-1][0].color_R

    elif(move == Moves.Rp):

        cube_array[-1][-1][1].color_U, cube_array[1][-1][-1].color_F, cube_array[0][-1][1].color_D, cube_array[1][-1][0].color_B, cube_array[-1][-1][-1].color_U, cube_array[0][-1][-1].color_F, \
        cube_array[0][-1][0].color_D, cube_array[-1][-1][0].color_B, cube_array[-1][-1][-1].color_F, cube_array[0][-1][-1].color_D, cube_array[0][-1][0].color_B, cube_array[-1][-1][0].color_U, \
        cube_array[-1][-1][-1].color_R, cube_array[0][-1][-1].color_R, cube_array[0][-1][0].color_R, cube_array[-1][-1][0].color_R, cube_array[-1][-1][1].color_R, cube_array[1][-1][-1].color_R, \
        cube_array[0][-1][1].color_R, cube_array[1][-1][0].color_R = \
        cube_array[1][-1][0].color_B, cube_array[-1][-1][1].color_U, cube_array[1][-1][-1].color_F, cube_array[0][-1][1].color_D, cube_array[-1][-1][0].color_B, cube_array[-1][-1][-1].color_U, \
        cube_array[0][-1][-1].color_F, cube_array[0][-1][0].color_D, cube_array[-1][-1][0].color_U, cube_array[-1][-1][-1].color_F, cube_array[0][-1][-1].color_D, cube_array[0][-1][0].color_B, \
        cube_array[-1][-1][0].color_R, cube_array[-1][-1][-1].color_R, cube_array[0][-1][-1].color_R, cube_array[0][-1][0].color_R, cube_array[1][-1][0].color_R, cube_array[-1][-1][1].color_R, \
        cube_array[1][-1][-1].color_R, cube_array[0][-1][1].color_R

    elif(move == Moves.M_RL):
        
        cube_array[-1][1][1].color_U, cube_array[1][1][-1].color_F, cube_array[0][1][1].color_D, cube_array[1][1][0].color_B, cube_array[-1][1][-1].color_U, cube_array[0][1][-1].color_F, \
        cube_array[0][1][0].color_D, cube_array[-1][1][0].color_B, cube_array[-1][1][-1].color_F, cube_array[0][1][-1].color_D, cube_array[0][1][0].color_B, cube_array[-1][1][0].color_U, \
        cube_array[-1][1][-1].color_L, cube_array[0][1][-1].color_L, cube_array[0][1][0].color_L, cube_array[-1][1][0].color_L, cube_array[-1][1][1].color_L, cube_array[1][1][-1].color_L, \
        cube_array[0][1][1].color_L, cube_array[1][1][0].color_L = \
        cube_array[1][1][0].color_B, cube_array[-1][1][1].color_U, cube_array[1][1][-1].color_F, cube_array[0][1][1].color_D, cube_array[-1][1][0].color_B, cube_array[-1][1][-1].color_U, \
        cube_array[0][1][-1].color_F, cube_array[0][1][0].color_D, cube_array[-1][1][0].color_U, cube_array[-1][1][-1].color_F, cube_array[0][1][-1].color_D, cube_array[0][1][0].color_B, \
        cube_array[-1][1][0].color_L, cube_array[-1][1][-1].color_L, cube_array[0][1][-1].color_L, cube_array[0][1][0].color_L, cube_array[1][1][0].color_L, cube_array[-1][1][1].color_L, \
        cube_array[1][1][-1].color_L, cube_array[0][1][1].color_L

    elif(move == Moves.M_RLp):
        cube_array[1][1][0].color_B, cube_array[-1][1][1].color_U, cube_array[1][1][-1].color_F, cube_array[0][1][1].color_D, cube_array[-1][1][0].color_B, cube_array[-1][1][-1].color_U, \
        cube_array[0][1][-1].color_F, cube_array[0][1][0].color_D, cube_array[-1][1][0].color_U, cube_array[-1][1][-1].color_F, cube_array[0][1][-1].color_D, cube_array[0][1][0].color_B, \
        cube_array[-1][1][0].color_L, cube_array[-1][1][-1].color_L, cube_array[0][1][-1].color_L, cube_array[0][1][0].color_L, cube_array[1][1][0].color_L, cube_array[-1][1][1].color_L, \
        cube_array[1][1][-1].color_L, cube_array[0][1][1].color_L = \
        cube_array[-1][1][1].color_U, cube_array[1][1][-1].color_F, cube_array[0][1][1].color_D, cube_array[1][1][0].color_B, cube_array[-1][1][-1].color_U, cube_array[0][1][-1].color_F, \
        cube_array[0][1][0].color_D, cube_array[-1][1][0].color_B, cube_array[-1][1][-1].color_F, cube_array[0][1][-1].color_D, cube_array[0][1][0].color_B, cube_array[-1][1][0].color_U, \
        cube_array[-1][1][-1].color_L, cube_array[0][1][-1].color_L, cube_array[0][1][0].color_L, cube_array[-1][1][0].color_L, cube_array[-1][1][1].color_L, cube_array[1][1][-1].color_L, \
        cube_array[0][1][1].color_L, cube_array[1][1][0].color_L

    elif(move == Moves.M_FB):
        
        cube_array[-1][1][1].color_U, cube_array[1][-1][1].color_R, cube_array[0][1][1].color_D, cube_array[1][0][1].color_L, cube_array[-1][1][1].color_F, cube_array[1][-1][1].color_F, \
        cube_array[0][1][1].color_F, cube_array[1][0][1].color_F, cube_array[-1][0][1].color_U, cube_array[-1][-1][1].color_R, cube_array[0][-1][1].color_D, cube_array[0][0][1].color_L, \
        cube_array[-1][0][1].color_L, cube_array[-1][-1][1].color_U, cube_array[0][-1][1].color_R, cube_array[0][0][1].color_D, cube_array[-1][0][1].color_F, cube_array[-1][-1][1].color_F, \
        cube_array[0][-1][1].color_F, cube_array[0][0][1].color_F = \
        cube_array[1][0][1].color_L, cube_array[-1][1][1].color_U, cube_array[1][-1][1].color_R, cube_array[0][1][1].color_D, cube_array[1][0][1].color_F, cube_array[-1][1][1].color_F, \
        cube_array[1][-1][1].color_F, cube_array[0][1][1].color_F, cube_array[0][0][1].color_L, cube_array[-1][0][1].color_U, cube_array[-1][-1][1].color_R, cube_array[0][-1][1].color_D, \
        cube_array[0][0][1].color_D, cube_array[-1][0][1].color_L, cube_array[-1][-1][1].color_U, cube_array[0][-1][1].color_R, cube_array[0][0][1].color_F, cube_array[-1][0][1].color_F, \
        cube_array[-1][-1][1].color_F, cube_array[0][-1][1].color_F

    elif(move == Moves.M_FBp):
        cube_array[1][0][1].color_L, cube_array[-1][1][1].color_U, cube_array[1][-1][1].color_R, cube_array[0][1][1].color_D, cube_array[1][0][1].color_F, cube_array[-1][1][1].color_F, \
        cube_array[1][-1][1].color_F, cube_array[0][1][1].color_F, cube_array[0][0][1].color_L, cube_array[-1][0][1].color_U, cube_array[-1][-1][1].color_R, cube_array[0][-1][1].color_D, \
        cube_array[0][0][1].color_D, cube_array[-1][0][1].color_L, cube_array[-1][-1][1].color_U, cube_array[0][-1][1].color_R, cube_array[0][0][1].color_F, cube_array[-1][0][1].color_F, \
        cube_array[-1][-1][1].color_F, cube_array[0][-1][1].color_F = \
        cube_array[-1][1][1].color_U, cube_array[1][-1][1].color_R, cube_array[0][1][1].color_D, cube_array[1][0][1].color_L, cube_array[-1][1][1].color_F, cube_array[1][-1][1].color_F, \
        cube_array[0][1][1].color_F, cube_array[1][0][1].color_F, cube_array[-1][0][1].color_U, cube_array[-1][-1][1].color_R, cube_array[0][-1][1].color_D, cube_array[0][0][1].color_L, \
        cube_array[-1][0][1].color_L, cube_array[-1][-1][1].color_U, cube_array[0][-1][1].color_R, cube_array[0][0][1].color_D, cube_array[-1][0][1].color_F, cube_array[-1][-1][1].color_F, \
        cube_array[0][-1][1].color_F, cube_array[0][0][1].color_F

    elif(move == Moves.M_UD):
        
        cube_array[1][1][-1].color_F, cube_array[1][-1][1].color_R, cube_array[1][1][0].color_B, cube_array[1][0][1].color_L, cube_array[1][0][-1].color_F, cube_array[1][0][-1].color_L, \
        cube_array[1][-1][-1].color_F, cube_array[1][-1][-1].color_R, cube_array[1][-1][0].color_R, cube_array[1][-1][0].color_B, cube_array[1][0][0].color_B, cube_array[1][0][0].color_L, \
        cube_array[1][0][-1].color_D, cube_array[1][-1][-1].color_D, cube_array[1][-1][0].color_D, cube_array[1][0][0].color_D, cube_array[1][1][-1].color_D, cube_array[1][-1][1].color_D, \
        cube_array[1][1][0].color_D, cube_array[1][0][1].color_D = \
        cube_array[1][0][1].color_L, cube_array[1][1][-1].color_F, cube_array[1][-1][1].color_R, cube_array[1][1][0].color_B, cube_array[1][0][0].color_L, cube_array[1][0][0].color_B, \
        cube_array[1][0][-1].color_L, cube_array[1][0][-1].color_F, cube_array[1][-1][-1].color_F, cube_array[1][-1][-1].color_R, cube_array[1][-1][0].color_R, cube_array[1][-1][0].color_B, \
        cube_array[1][0][0].color_D, cube_array[1][0][-1].color_D, cube_array[1][-1][-1].color_D, cube_array[1][-1][0].color_D, cube_array[1][0][1].color_D, cube_array[1][1][-1].color_D, \
        cube_array[1][-1][1].color_D, cube_array[1][1][0].color_D

    elif(move == Moves.M_UDp):

        cube_array[1][0][1].color_L, cube_array[1][1][-1].color_F, cube_array[1][-1][1].color_R, cube_array[1][1][0].color_B, cube_array[1][0][0].color_L, cube_array[1][0][0].color_B, \
        cube_array[1][0][-1].color_L, cube_array[1][0][-1].color_F, cube_array[1][-1][-1].color_F, cube_array[1][-1][-1].color_R, cube_array[1][-1][0].color_R, cube_array[1][-1][0].color_B, \
        cube_array[1][0][0].color_D, cube_array[1][0][-1].color_D, cube_array[1][-1][-1].color_D, cube_array[1][-1][0].color_D, cube_array[1][0][1].color_D, cube_array[1][1][-1].color_D, \
        cube_array[1][-1][1].color_D, cube_array[1][1][0].color_D = \
        cube_array[1][1][-1].color_F, cube_array[1][-1][1].color_R, cube_array[1][1][0].color_B, cube_array[1][0][1].color_L, cube_array[1][0][-1].color_F, cube_array[1][0][-1].color_L, \
        cube_array[1][-1][-1].color_F, cube_array[1][-1][-1].color_R, cube_array[1][-1][0].color_R, cube_array[1][-1][0].color_B, cube_array[1][0][0].color_B, cube_array[1][0][0].color_L, \
        cube_array[1][0][-1].color_D, cube_array[1][-1][-1].color_D, cube_array[1][-1][0].color_D, cube_array[1][0][0].color_D, cube_array[1][1][-1].color_D, cube_array[1][-1][1].color_D, \
        cube_array[1][1][0].color_D, cube_array[1][0][1].color_D

def Handle_Mouse(Player_Mouse, cube_array):

    global change

    # U
    if((Player_Mouse.new_X + 25) < Player_Mouse.prev_X):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("U")
                Move_Cubes(cube_array, Moves.U)
                change = 1

    # U'
    if(Player_Mouse.new_X > (Player_Mouse.prev_X + 25)):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("U'")
                Move_Cubes(cube_array, Moves.Up)
                change = 1

    # F
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 25)):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("F")
                Move_Cubes(cube_array, Moves.F)
                change = 1

    # F'
    if((Player_Mouse.new_Y - 25) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("F'")
                Move_Cubes(cube_array, Moves.Fp)
                change = 1

    # L
    if((Player_Mouse.new_Y - 25) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("L")
                Move_Cubes(cube_array, Moves.L)
                change = 1

    # L'
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 25)):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("L'")
                Move_Cubes(cube_array, Moves.Lp)
                change = 1


    # R
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 25)):
        if((Player_Mouse.prev_X > cube_array[-1][-1][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][-1][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][-1][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][-1][-1].point4[1])):
                print("R")
                Move_Cubes(cube_array, Moves.R)
                change = 1

    # R'
    if((Player_Mouse.new_Y - 25) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][-1][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][-1][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][-1][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][-1][-1].point4[1])):
                print("R'")
                Move_Cubes(cube_array, Moves.Rp)
                change = 1

    # B
    if((Player_Mouse.new_Y - 25) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][0][0].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][0].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][0].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][0].point4[1])):
                print("B")
                Move_Cubes(cube_array, Moves.B)
                change = 1

    # B'
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 25)):
        if((Player_Mouse.prev_X > cube_array[-1][0][0].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][0].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][0].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][0].point4[1])):
                print("B'")
                Move_Cubes(cube_array, Moves.Bp)
                change = 1

    # D
    if(Player_Mouse.new_X > (Player_Mouse.prev_X + 25)):
        if((Player_Mouse.prev_X > cube_array[0][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[0][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[0][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[0][0][-1].point4[1])):
                print("D")
                Move_Cubes(cube_array, Moves.D)
                change = 1

    # D'
    if((Player_Mouse.new_X + 25) < Player_Mouse.prev_X):
        if((Player_Mouse.prev_X > cube_array[0][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[0][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[0][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[0][0][-1].point4[1])):
                print("D'")
                Move_Cubes(cube_array, Moves.Dp)
                change = 1

    # M_RL
    if((Player_Mouse.new_Y - 25) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][1][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][1][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][1][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][1][-1].point4[1])):
                print("M_RL")
                Move_Cubes(cube_array, Moves.M_RL)
                change = 1

    # M_RL'
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 25)):
        if((Player_Mouse.prev_X > cube_array[-1][1][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][1][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][1][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][1][-1].point4[1])):
                print("M_RL'")
                Move_Cubes(cube_array, Moves.M_RLp)
                change = 1

    # M_FB
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 25)):
        if((Player_Mouse.prev_X > cube_array[-1][0][1].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][1].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][1].point4[1])):
                print("M_FB")
                Move_Cubes(cube_array, Moves.M_FB)
                change = 1

    # M_FB'
    if((Player_Mouse.new_Y - 25) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][0][1].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][1].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][1].point4[1])):
                print("M_FB'")
                Move_Cubes(cube_array, Moves.M_FBp)
                change = 1

    # M_UD
    if(Player_Mouse.new_X > (Player_Mouse.prev_X + 25)):
        if((Player_Mouse.prev_X > cube_array[1][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[1][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[1][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[1][0][-1].point4[1])):
                print("M_UD")
                Move_Cubes(cube_array, Moves.M_UD)
                change = 1

    # M_UD'
    if((Player_Mouse.new_X + 25) < Player_Mouse.prev_X):
        if((Player_Mouse.prev_X > cube_array[1][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[1][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[1][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[1][0][-1].point4[1])):
                print("M_UD'")
                Move_Cubes(cube_array, Moves.M_UDp)
                change = 1

    pass

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Cubos')

clock = pygame.time.Clock()

crashed = False

height = 3
width = 3
length = 3

cubes = Create_Cube_grid(200, HEIGHT-150, 50, length, width, height, Colors.orange, Colors.green, Colors.white, Colors.red, Colors.blue, Colors.yellow)

Print_Cube_Array(cubes, height, width, length)

Player_Mouse = Mouse()

scrambling_moves = [Moves.Dp, Moves.F, Moves.F, Moves.Lp, Moves.U,Moves.Rp, Moves.F, Moves.F, Moves.L, Moves.Bp, Moves.R, Moves.R, Moves.D, Moves.D, Moves.R, Moves.R, Moves.Bp, Moves.L, Moves.D, Moves.D, Moves.B, Moves.B, Moves.Dp, Moves.F, Moves.F, Moves.R, Moves.R, Moves.Fp, Moves.D, Moves.B, Moves.Rp, Moves.Lp, Moves.U, Moves.U, Moves.F]
#scrambling_moves = [Moves.Rp, Moves.U, Moves.U, Moves.B, Moves.Lp, Moves.Bp, Moves.U, Moves.U, Moves.L, Moves.L, Moves.U, Moves.D, Moves.Rp, Moves.B, Moves.D, Moves.D, Moves.U, Moves.U, Moves.Rp, Moves.Bp, Moves.U, Moves.U, Moves.L, Moves.L, Moves.B, Moves.B, Moves.Rp, Moves.L, Moves.Bp, Moves.F, Moves.F, Moves.L, Moves.L, Moves.R, Moves.B, Moves.B]

for i in range(len(scrambling_moves)):
    Move_Cubes(cubes, scrambling_moves[i])
    Print_Cube_Array(cubes, height, width, length)
    time.sleep(0.1)

solve_chain = solver.GetSolveChain(cubes)

time.sleep(2)

for i in range(len(solve_chain)):
    Move_Cubes(cubes, solve_chain[i])
    Print_Cube_Array(cubes, height, width, length)
    time.sleep(0.05)

print("solved")

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            Player_Mouse.prev_X = pygame.mouse.get_pos()[0]
            Player_Mouse.prev_Y = pygame.mouse.get_pos()[1]

        if event.type == pygame.MOUSEBUTTONUP:
            Player_Mouse.new_X = pygame.mouse.get_pos()[0]
            Player_Mouse.new_Y = pygame.mouse.get_pos()[1]
            Handle_Mouse(Player_Mouse, cubes)
            if(change):
                Print_Cube_Array(cubes, height, width, length)
                change = 0

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()