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
        pygame.draw.line(screen, (255,255,255), self.point3, self.point4,3)

        #center to right top
        pygame.draw.line(screen, (255,255,255), self.point4,self.point7,3)

        #right vertical
        pygame.draw.line(screen, (255,255,255), self.point7, self.point6,3)

        #center to right bottom
        pygame.draw.line(screen, (255,255,255), self.point3,self.point6,3)

        #center to left bottom
        pygame.draw.line(screen, (255,255,255), self.point3,self.point1,3)

        #center to left top
        pygame.draw.line(screen, (255,255,255), self.point4,self.point2,3)

        #left vertical
        pygame.draw.line(screen, (255,255,255), self.point1, self.point2,3)

        #left to center
        pygame.draw.line(screen, (255,255,255), self.point2, self.point5,3)

        #right to center
        pygame.draw.line(screen, (255,255,255), self.point5,self.point7,3)

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

def Print_Cube_Array(height, width, length):

    for h in range(height):
        for w in range(width):
            for l in range(length):
                cubes[h][width-1-w][l].draw(gameDisplay)

    pass

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Cubos')

clock = pygame.time.Clock()

crashed = False

height = 3
width = 3
length = 3

cubes = Create_Cube_grid(200, HEIGHT-150, 50, length, width, height, Colors.red, Colors.green, Colors.yellow)

Print_Cube_Array(height, width, length)

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()