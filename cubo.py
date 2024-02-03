import pygame
import math
import time
import solver
import random
import kociemba
import serial

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

Supported_Keys = [pygame.K_w, pygame.K_y, pygame.K_g, pygame.K_o, pygame.K_r, pygame.K_b]

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

def Create_Random_Scramble(Cube):

    random_list = []

    print("Scrambling...")

    for i in range(40):
        random_list.append(random.randint(0, 11))

    for i in range(len(random_list)):
        Move_Cubes(Cube, random_list[i])
        Print_Cube_Array(Cube, len(Cube), len(Cube[0]), len(Cube[0][0]))
        time.sleep(0.1)

    return random_list

def Solve_Pochmann(Cube):

    print("Solving Using Pochmann...")

    solve_chain = solver.GetSolveChain(Cube)

    for i in range(len(solve_chain)):
        Move_Cubes(Cube, solve_chain[i])
        Print_Cube_Array(Cube, len(Cube), len(Cube[0]), len(Cube[0][0]))
        time.sleep(0.05)

    print("Solved")

    pass

def Print_Layout(screen):

    font = pygame.font.Font('freesansbold.ttf', 25)

    # Down Face
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*2), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*3), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*4), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*2), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*3), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*4), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*2), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*3), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*4), 30, 30),  2)

    text = font.render('Y', True, Colors.white)
    textRect = text.get_rect()
    textRect.center = (WIDTH - (30*9) + 15, HEIGHT-(30*3) + 15)

    screen.blit(text, textRect)


    # Front Face
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*7), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*7), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*7), 30, 30),  2)

    text = font.render('G', True, Colors.white)
    textRect = text.get_rect()
    textRect.center = (WIDTH - (30*9) + 15, HEIGHT-(30*6) + 15)

    screen.blit(text, textRect)


    # Up Face
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*8), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*9), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*8), HEIGHT-(30*10), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*8), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*9), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*9), HEIGHT-(30*10), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*8), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*9), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*10), HEIGHT-(30*10), 30, 30),  2)

    text = font.render('W', True, Colors.white)
    textRect = text.get_rect()
    textRect.center = (WIDTH - (30*9) + 15, HEIGHT-(30*9) + 15)

    screen.blit(text, textRect)
    

    # Left Face
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*11), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*11), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*11), HEIGHT-(30*7), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*12), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*12), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*12), HEIGHT-(30*7), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*13), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*13), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*13), HEIGHT-(30*7), 30, 30),  2)

    text = font.render('O', True, Colors.white)
    textRect = text.get_rect()
    textRect.center = (WIDTH - (30*12) + 15, HEIGHT-(30*6) + 15)

    screen.blit(text, textRect)


    # Right Face
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*7), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*7), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*7), HEIGHT-(30*7), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*6), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*6), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*6), HEIGHT-(30*7), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*5), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*5), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*5), HEIGHT-(30*7), 30, 30),  2)

    text = font.render('R', True, Colors.white)
    textRect = text.get_rect()
    textRect.center = (WIDTH - (30*6) + 15, HEIGHT-(30*6) + 15)

    screen.blit(text, textRect)


    # Back Face
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*4), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*4), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*4), HEIGHT-(30*7), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*3), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*3), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*3), HEIGHT-(30*7), 30, 30),  2)

    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*2), HEIGHT-(30*5), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*2), HEIGHT-(30*6), 30, 30),  2)
    pygame.draw.rect(screen, Colors.white, pygame.Rect(WIDTH - (30*2), HEIGHT-(30*7), 30, 30),  2)

    text = font.render('B', True, Colors.white)
    textRect = text.get_rect()
    textRect.center = (WIDTH - (30*3) + 15, HEIGHT-(30*6) + 15)

    screen.blit(text, textRect)

    pass

def Fill_Layout(screen, chain):

    font = pygame.font.Font('freesansbold.ttf', 25)

    j = 0

    for i in range(54):

        if j == 9:
            j = 0

        x = j % 3
        y = j // 3

        # Up Face
        if (i < 9):

            if(i < len(chain)):
            
                text = font.render(chain[i], True, Colors.white)
                textRect = text.get_rect()
                textRect.center = (WIDTH - (30*(10 - x)) + 15, HEIGHT-(30*(10 - y)) + 15)

                screen.blit(text, textRect)

            else:

                pygame.draw.rect(screen, Colors.black, pygame.Rect(WIDTH - (30*(10 - x)) + 2, HEIGHT-(30*(10 - y)) + 2, 28, 28))

        # Left Face
        elif (i < 18):

            if(i < len(chain)):

                text = font.render(chain[i], True, Colors.white)
                textRect = text.get_rect()
                textRect.center = (WIDTH - (30*(13 - x)) + 15, HEIGHT-(30*(7 - y)) + 15)

                screen.blit(text, textRect)

            else:

                pygame.draw.rect(screen, Colors.black, pygame.Rect(WIDTH - (30*(13 - x)) + 2, HEIGHT-(30*(7 - y)) + 2, 28, 28))

        # Front Face
        elif (i < 27):

            if(i < len(chain)):

                text = font.render(chain[i], True, Colors.white)
                textRect = text.get_rect()
                textRect.center = (WIDTH - (30*(10 - x)) + 15, HEIGHT-(30*(7 - y)) + 15)

                screen.blit(text, textRect)

            else:

                pygame.draw.rect(screen, Colors.black, pygame.Rect(WIDTH - (30*(10 - x)) + 2, HEIGHT-(30*(7 - y)) + 2, 28, 28))

        # Right Face
        elif (i < 36):

            if(i < len(chain)):

                text = font.render(chain[i], True, Colors.white)
                textRect = text.get_rect()
                textRect.center = (WIDTH - (30*(7 - x)) + 15, HEIGHT-(30*(7 - y)) + 15)

                screen.blit(text, textRect)

            else:

                pygame.draw.rect(screen, Colors.black, pygame.Rect(WIDTH - (30*(7 - x)) + 2, HEIGHT-(30*(7 - y)) + 2, 28, 28))

        # Back Face
        elif (i < 45):

            if(i < len(chain)):

                text = font.render(chain[i], True, Colors.white)
                textRect = text.get_rect()
                textRect.center = (WIDTH - (30*(4 - x)) + 15, HEIGHT-(30*(7 - y)) + 15)

                screen.blit(text, textRect)

            else:

                pygame.draw.rect(screen, Colors.black, pygame.Rect(WIDTH - (30*(4 - x)) + 2, HEIGHT-(30*(7 - y)) + 2, 28, 28))

        # Down Face
        else:

            if(i < len(chain)):

                text = font.render(chain[i], True, Colors.white)
                textRect = text.get_rect()
                textRect.center = (WIDTH - (30*(10 - x)) + 15, HEIGHT-(30*(4 - y)) + 15)

                screen.blit(text, textRect)

            else:

                pygame.draw.rect(screen, Colors.black, pygame.Rect(WIDTH - (30*(10 - x)) + 2, HEIGHT-(30*(4 - y)) + 2, 28, 28))

        j += 1

        pygame.display.update()

    pass

def Display_Menu(screen):

    font = pygame.font.Font('freesansbold.ttf', 50)

    text = font.render('Kociemba', True, Colors.white, Colors.green)
    textRect = text.get_rect()
    textRect.center = (WIDTH - 150, 50)

    screen.blit(text, textRect)

    text = font.render('Pochmann', True, Colors.white, Colors.red)
    textRect = text.get_rect()
    textRect.center = (500, 50)

    screen.blit(text, textRect)

    text = font.render('Scramble', True, Colors.white, Colors.blue)
    textRect = text.get_rect()
    textRect.center = (150, 50)

    screen.blit(text, textRect)

    text = font.render('Input State:', True, Colors.white, Colors.orange)
    textRect = text.get_rect()
    textRect.center = (WIDTH - 250, 200)

    screen.blit(text, textRect)

    font = pygame.font.Font('freesansbold.ttf', 25)

    text = font.render('Set State', True, Colors.black, Colors.white)
    textRect = text.get_rect()
    textRect.center = (WIDTH - 125, 345)

    screen.blit(text, textRect)

    text = font.render('Send Solution', True, Colors.black, Colors.white)
    textRect = text.get_rect()
    textRect.center = (WIDTH - 100, 525)

    screen.blit(text, textRect)

    text = font.render('Send Scramble', True, Colors.black, Colors.white)
    textRect = text.get_rect()
    textRect.center = (150, 100)

    screen.blit(text, textRect)

    Print_Layout(screen)

    pygame.display.update()

    pass

def Color_to_Face_Kociemba(color):

    switcher = {
        Colors.white: "U",
        Colors.yellow: "D",
        Colors.green: "F",
        Colors.blue: "B",
        Colors.orange: "L",
        Colors.red: "R",
    }

    return switcher.get(color, "")

def Kociemba_Move_Translator(move):

    switcher = {
        "U": Moves.U,
        "U'": Moves.Up,
        "D": Moves.D,
        "D'": Moves.Dp,
        "F": Moves.F,
        "F'": Moves.Fp,
        "B": Moves.B,
        "B'": Moves.Bp,
        "R": Moves.R,
        "R'": Moves.Rp,
        "L": Moves.L,
        "L'": Moves.Lp,
    }

    return switcher.get(move,"")

def Solve_Kociemba(Cube):

    print("Solving Using Kociemba...")

    State_list = []
    SolveChain = []

    # U
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1][j][i].color_U))

    # R
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][-1][-1 - j].color_R))

    # F
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][j][-1].color_F))

    # D
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[0][j][-1 - i].color_D))

    # L
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][0][j].color_L))

    # B
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][-1 - j][0].color_B))

    # Concatenate all letters into one string
    State_list = ''.join(State_list)

    if(State_list != 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'):
        SolveChain_Kociemba = kociemba.solve(State_list)

        print('Solving Chain: ', SolveChain_Kociemba)

        SolveChain_Kociemba = SolveChain_Kociemba.split()

        for i in range(len(SolveChain_Kociemba)):
            if(SolveChain_Kociemba[i][-1] == '2'):
                SolveChain.append(Kociemba_Move_Translator(SolveChain_Kociemba[i][0]))
                SolveChain.append(Kociemba_Move_Translator(SolveChain_Kociemba[i][0]))
            else:
                SolveChain.append(Kociemba_Move_Translator(SolveChain_Kociemba[i]))

    print("Total Moves of Solution: ", len(SolveChain))

    # Perform Moves
    for i in range(len(SolveChain)):
        Move_Cubes(Cube, SolveChain[i])
        Print_Cube_Array(Cube, len(Cube), len(Cube[0]), len(Cube[0][0]))
        time.sleep(0.05)

    print("Solved")

    pass

def Letter_to_Face(letter):

    switcher = {
        "w": "U",
        "y": "D",
        "g": "F",
        "b": "B",
        "o": "L",
        "r": "R",
    }

    return switcher.get(letter, "")

def Set_Cube_State(Cube, chain):

    State_list_desired = []
    State_list = []
    SolveChain = []

    # U
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1][j][i].color_U))

    # R
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][-1][-1 - j].color_R))

    # F
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][j][-1].color_F))

    # D
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[0][j][-1 - i].color_D))

    # L
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][0][j].color_L))

    # B
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][-1 - j][0].color_B))

    # Concatenate all letters into one string
    State_list = ''.join(State_list)


    for i in range (9):
        State_list_desired.append(Letter_to_Face(chain[i]))

    for i in range (27, 36):
        State_list_desired.append(Letter_to_Face(chain[i]))

    for i in range (18, 27):
        State_list_desired.append(Letter_to_Face(chain[i]))

    for i in range (45, 54):
        State_list_desired.append(Letter_to_Face(chain[i]))

    for i in range (9, 18):
        State_list_desired.append(Letter_to_Face(chain[i]))

    for i in range (36, 45):
        State_list_desired.append(Letter_to_Face(chain[i]))


    # Concatenate all letters into one string
    State_list_desired = ''.join(State_list_desired)

    if(State_list != State_list_desired):
        SolveChain_Kociemba = kociemba.solve(State_list, State_list_desired)

        SolveChain_Kociemba = SolveChain_Kociemba.split()

        for i in range(len(SolveChain_Kociemba)):
            if(SolveChain_Kociemba[i][-1] == '2'):
                SolveChain.append(Kociemba_Move_Translator(SolveChain_Kociemba[i][0]))
                SolveChain.append(Kociemba_Move_Translator(SolveChain_Kociemba[i][0]))
            else:
                SolveChain.append(Kociemba_Move_Translator(SolveChain_Kociemba[i]))

    print("Setting defined state")

    # Perform Moves
    for i in range(len(SolveChain)):
        Move_Cubes(Cube, SolveChain[i])

    Print_Cube_Array(Cube, len(Cube), len(Cube[0]), len(Cube[0][0]))

    pass

def Move_translator_reverse(move):

    switcher = {
        Moves.U: "U",
        Moves.Up: "U'",
        Moves.D: "D",
        Moves.Dp: "D'",
        Moves.F: "F",
        Moves.Fp: "F'",
        Moves.B: "B",
        Moves.Bp: "B'",
        Moves.R: "R",
        Moves.Rp: "R'",
        Moves.L: "L",
        Moves.Lp: "L'",
    }

    return switcher.get(move,"")

def Send_Serial_Solution(Cube):

    State_list = []
    SolveChain_serial = []

    # U
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1][j][i].color_U))

    # R
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][-1][-1 - j].color_R))

    # F
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][j][-1].color_F))

    # D
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[0][j][-1 - i].color_D))

    # L
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][0][j].color_L))

    # B
    for i in range(3):
        for j in range(3):
            State_list.append(Color_to_Face_Kociemba(Cube[-1 - i][-1 - j][0].color_B))

    # Concatenate all letters into one string
    State_list = ''.join(State_list)

    if(State_list != 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'):
        SolveChain_Kociemba = kociemba.solve(State_list)

        print('Solving Chain: ', SolveChain_Kociemba)

        SolveChain_Kociemba = SolveChain_Kociemba.split()

        for i in range(len(SolveChain_Kociemba)):
            if(SolveChain_Kociemba[i][-1] == '2'):
                SolveChain_serial.append(SolveChain_Kociemba[i][0])
                SolveChain_serial.append(SolveChain_Kociemba[i][0])
            elif(SolveChain_Kociemba[i][-1] == "'"):
                SolveChain_serial.append(SolveChain_Kociemba[i][0])
                SolveChain_serial.append(SolveChain_Kociemba[i][1])
            else:
                SolveChain_serial.append(SolveChain_Kociemba[i])

    print("Total Moves of Solution: ", len(SolveChain_serial))

    SolveChain_serial = ''.join(SolveChain_serial)

    # Send String
    arduino = serial.Serial(port='COM4', baudrate=9600)

    time.sleep(5)

    SolveChain_serial = SolveChain_serial + '\n'
    
    arduino.write(SolveChain_serial.encode())

    arduino.close()


    print("String sent to serial device")

    pass

def Send_Scramble(scramble):

    Scramble_serial = []

    for i in range(len(scramble)):
        Scramble_serial.append(Move_translator_reverse(scramble[i]))

    Scramble_serial = ''.join(Scramble_serial)

    Scramble_serial = Scramble_serial + '\n'

    # Send String
    arduino = serial.Serial(port='COM4', baudrate=9600)

    time.sleep(5)
    
    arduino.write(Scramble_serial.encode())

    arduino.close()


    print("Scramble string sent to serial device")

    pass

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Rubiks Cube')

clock = pygame.time.Clock()

crashed = False
change = 0

height = 3
width = 3
length = 3

cubes = Create_Cube_grid(200, HEIGHT-150, 50, length, width, height, Colors.orange, Colors.green, Colors.white, Colors.red, Colors.blue, Colors.yellow)

Print_Cube_Array(cubes, height, width, length)

Player_Mouse = Mouse()

user_text = []

last_scramble = []

Display_Menu(gameDisplay)

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

            if((Player_Mouse.new_X > (30)) and (Player_Mouse.new_X < (270)) and (Player_Mouse.new_Y > 25) and (Player_Mouse.new_Y < 75)):
                last_scramble = Create_Random_Scramble(cubes)
            elif((Player_Mouse.new_X > (50)) and (Player_Mouse.new_X < (250)) and (Player_Mouse.new_Y > 85) and (Player_Mouse.new_Y < 115)):
                Send_Scramble(last_scramble)  
            elif((Player_Mouse.new_X > (365)) and (Player_Mouse.new_X < (635)) and (Player_Mouse.new_Y > 25) and (Player_Mouse.new_Y < 75)):
                Solve_Pochmann(cubes)
            elif((Player_Mouse.new_X > (725)) and (Player_Mouse.new_X < (975)) and (Player_Mouse.new_Y > 25) and (Player_Mouse.new_Y < 75)):                
                Solve_Kociemba(cubes)
            elif((Player_Mouse.new_X > (820)) and (Player_Mouse.new_X < (930)) and (Player_Mouse.new_Y > 332) and (Player_Mouse.new_Y < 357)):
                if(len(user_text) == 54):
                    Set_Cube_State(cubes, user_text)                    
            elif((Player_Mouse.new_X > (815)) and (Player_Mouse.new_X < (985)) and (Player_Mouse.new_Y > 512) and (Player_Mouse.new_Y < 537)):
                    Send_Serial_Solution(cubes)
            else:
                Handle_Mouse(Player_Mouse, cubes)
                if(change):
                    Print_Cube_Array(cubes, height, width, length)
                    change = 0

        if event.type == pygame.KEYDOWN:
            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
  
                # get text input from 0 to -1 i.e. end. 
                user_text = user_text[:-1] 
  
            # Unicode standard is used for string 
            # formation 
            else:
                if len(user_text) < 54:
                    if event.key in Supported_Keys:
                        user_text.append(event.unicode)

            Fill_Layout(gameDisplay, user_text)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()