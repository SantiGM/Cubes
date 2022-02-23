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

WIDTH = 500
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

def Create_Cube_grid(x,y,length,num_cubes,grid_width,grid_length,grid_height,color_L,color_R,color_U):

    cube_list = []

    for i in range(num_cubes):
        cube_list.append(Cube(0,0,length,color_L,color_R,color_U))

    for i in range(grid_length):
        cube_list[i].x = x + (length*math.cos(DEG_TO_RAD_30))*i
        cube_list[i].y = y + (length*math.sin(DEG_TO_RAD_30))*i
        cube_list[i].update_points()

    for i in range(1,grid_width):
        for j in range(grid_length):
            cube_list[j+grid_length*i].x = cube_list[j].x + (abs(cube_list[j].point3[0] - cube_list[j].point6[0]))*i
            cube_list[j+grid_length*i].y = cube_list[j].y - (abs(cube_list[j].point3[1] - cube_list[j].point6[1]))*i
            cube_list[j+grid_length*i].update_points()

    for i in range(1,grid_height):
        for j in range(grid_length*grid_width):
            cube_list[j+(grid_width*grid_length*i)].x = cube_list[j].x
            cube_list[j+(grid_width*grid_length*i)].y = cube_list[j].y - cube_list[j].len*i
            cube_list[j+(grid_width*grid_length*i)].update_points()

    return cube_list
             
pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Cubos')

clock = pygame.time.Clock()

crashed = False

Cubo1 = Cube(200,HEIGHT-100,50,Colors.red,Colors.blue,Colors.yellow)

Cubo2 = Cube(Cubo1.x,Cubo1.y-Cubo1.len,Cubo1.len,Colors.red,Colors.blue,Colors.yellow)

Cubo3 = Cube(Cubo1.x,Cubo1.y-2*Cubo1.len,Cubo1.len,Colors.red,Colors.blue,Colors.yellow)

Cubo4 = Cube(Cubo1.x+Cubo1.len*math.cos(DEG_TO_RAD_30),Cubo1.y+(Cubo1.len/2),Cubo1.len,Colors.red,Colors.blue,Colors.yellow)

Cubo5 = Cube(Cubo1.x+2*Cubo1.len*math.cos(DEG_TO_RAD_30),Cubo1.y+Cubo1.len,Cubo1.len,Colors.red,Colors.blue,Colors.yellow)

Cubo6 = Cube(Cubo1.x+Cubo1.len*math.cos(DEG_TO_RAD_30),Cubo1.y-(Cubo1.len/2),Cubo1.len,Colors.red,Colors.blue,Colors.yellow)


#Cubo1.draw(gameDisplay)
#Cubo2.draw(gameDisplay)
#Cubo3.draw(gameDisplay)
#Cubo4.draw(gameDisplay)
#Cubo5.draw(gameDisplay)
#Cubo6.draw(gameDisplay)

cube_list = Create_Cube_grid(150,HEIGHT-100,50,63,3,3,7,Colors.red,Colors.green,Colors.yellow)

for i in range(7):
    cube_list[6+9*i].draw(gameDisplay)
    cube_list[3+9*i].draw(gameDisplay)
    cube_list[7+9*i].draw(gameDisplay)
    cube_list[0+9*i].draw(gameDisplay)
    cube_list[4+9*i].draw(gameDisplay)
    cube_list[8+9*i].draw(gameDisplay)
    cube_list[1+9*i].draw(gameDisplay)
    cube_list[5+9*i].draw(gameDisplay)
    cube_list[2+9*i].draw(gameDisplay)

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()