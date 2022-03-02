import pygame
import math

class Colors:
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    blue = (0,0,255)
    green = (0,255,0)
    yellow = (255,255,0)
    orange = (255,102,0)
    grey = (220,220,220)

class Mouse:

    def __init__(self):
        self.prev_X = 0
        self.prev_Y = 0
        self.new_X = 0
        self.new_Y = 0

WIDTH = 1000
HEIGHT = 600

DEG_TO_RAD_30 = 30*math.pi/180

class Cube:

    def __init__(self,x,y,len,color_L,color_R,color_U):
        self.x = x
        self.y = y
        self.len = len
        self.color_L = color_L
        self.color_R = color_R
        self.color_U = color_U

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

        #Right Face
        pygame.draw.polygon(screen, self.color_R, [self.point3,self.point4,self.point7,self.point6])

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

def Create_Cube_grid(x, y, length, grid_length, grid_width, grid_height, color_L, color_R, color_U):

    cube_array = []

    for h in range(grid_height):
        cube_array.append([])
        for w in range(grid_width):
            cube_array[h].append([])
            for l in range(grid_length):
                cube_array[h][w].append(Cube(x + (length*math.cos(DEG_TO_RAD_30))*l + (length*math.cos(DEG_TO_RAD_30))*w, y + (length*math.sin(DEG_TO_RAD_30))*l - (length*math.sin(DEG_TO_RAD_30))*w - length*h, length, color_L, color_R, color_U))
                cube_array[h][w][l].update_points()

    return cube_array

def Print_Cube_Array(cube_array, height, width, length):

    for h in range(height):
        for w in range(width):
            for l in range(length):
                cube_array[h][width-1-w][l].draw(gameDisplay)

    pass

def Handle_Mouse(Player_Mouse, cube_array):

    # U
    if((Player_Mouse.new_X + 50) < Player_Mouse.prev_X):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("U")

    # U'
    if(Player_Mouse.new_X > (Player_Mouse.prev_X + 50)):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("U'")

    # F
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 50)):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("F")

    # F'
    if((Player_Mouse.new_Y - 50) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("F'")

    # L
    if((Player_Mouse.new_Y - 50) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("L")

    # L'
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 50)):
        if((Player_Mouse.prev_X > cube_array[-1][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][-1].point4[1])):
                print("L'")


    # R
    if((Player_Mouse.new_Y - 50) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][-1][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][-1][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][-1][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][-1][-1].point4[1])):
                print("R")

    # R'
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 50)):
        if((Player_Mouse.prev_X > cube_array[-1][-1][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[-1][-1][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][-1][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[-1][-1][-1].point4[1])):
                print("R'")

    # B
    if((Player_Mouse.new_Y - 50) > Player_Mouse.prev_Y):
        if((Player_Mouse.prev_X > cube_array[-1][0][0].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][0].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][0].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][0].point4[1])):
                print("B")

    # B'
    if(Player_Mouse.new_Y < (Player_Mouse.prev_Y - 50)):
        if((Player_Mouse.prev_X > cube_array[-1][0][0].point1[0]) and (Player_Mouse.prev_X < cube_array[-1][0][0].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[-1][0][0].point1[1]) and (Player_Mouse.prev_Y > cube_array[-1][0][0].point4[1])):
                print("B'")

    # D
    if(Player_Mouse.new_X > (Player_Mouse.prev_X + 50)):
        if((Player_Mouse.prev_X > cube_array[0][0][-1].point1[0]) and (Player_Mouse.prev_X < cube_array[0][0][-1].point3[0])):
            if((Player_Mouse.prev_Y < cube_array[0][0][-1].point1[1]) and (Player_Mouse.prev_Y > cube_array[0][0][-1].point4[1])):
                print("D")

    # D'
    if((Player_Mouse.new_X + 50) < Player_Mouse.prev_X):
        if((Player_Mouse.prev_X > cube_array[0][0][-1].point3[0]) and (Player_Mouse.prev_X < cube_array[0][0][-1].point6[0])):
            if((Player_Mouse.prev_Y < cube_array[0][0][-1].point6[1]) and (Player_Mouse.prev_Y > cube_array[0][0][-1].point4[1])):
                print("D'")

    pass

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Cubos')

clock = pygame.time.Clock()

crashed = False

height = 3
width = 3
length = 3

cubes = Create_Cube_grid(200, HEIGHT-150, 50, length, width, height, Colors.blue, Colors.orange, Colors.white)

Print_Cube_Array(cubes, height, width, length)

Player_Mouse = Mouse()

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

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()