import pygame, sys

sys.path.append("C:\\Users\\Admin\\Documents\\Code Night\\Code-Night\\New Boot Goffin\\Rubiks Solver\\backend")

for i in sys.path:
    print(i)
    
from rubiks_helper import * 

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORAGNE = (0, 255, 255)

DEFAULT_FACE_COLORS = (128, 128, 192)

STARTING_POSITION= [(1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (1, 0, -1), (1, -1, 0), (1, 0, 1), (1, 1, 0), (1, 0, 0),            # Left column
                    (0, 1, 1), (0, 1, -1), (0, -1, -1), (0, -1, 1), (0, 0, -1), (0, -1, 0), (0, 0, 1), (0, 1, 0),                       # Middle column
                    (-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (-1, -1, 1), (-1, 0, -1), (-1, -1, 0), (-1, 0, 1), (-1, 1, 0), (-1, 0, 0)    # Right column
                    ]

DEFAULT_VERTICES = [(-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1), (-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1)]

class Cube():
    def __init__(self, vertices=DEFAULT_VERTICES, colors=DEFAULT_FACE_COLORS , originX=0, originY=0, originZ=0):
        self.__vertices = [pygame.math.Vector3(v) for v in vertices]
        self.__faces = {'front':{  'face':(0,1,2,3), 'color': DEFAULT_FACE_COLORS}, 
                        'back':{   'face':(1,5,6,2), 'color': DEFAULT_FACE_COLORS},
                        'right':{  'face':(5,4,7,6), 'color': DEFAULT_FACE_COLORS}, 
                        'left':{   'face':(4,0,3,7), 'color': DEFAULT_FACE_COLORS},
                        'top':{    'face':(3,2,6,7), 'color': DEFAULT_FACE_COLORS}, 
                        'bottom':{ 'face':(1,0,4,5), 'color': DEFAULT_FACE_COLORS}}
        self.cube_origins = [(originX, originY, originZ)]     

    def rotate(self, angle, axis):
        self.__vertices = rotate_vertices(self.__vertices, angle, axis)
        
    def scale(self, s):
        self.__vertices = scale_vertices(self.__vertices, s)
        
    def translate(self, t):
        self.__vertices = translate_vertices(self.__vertices, t)

    def calculate_average_z(self, vertices):
        for val in self.__faces.values():
            for i in val.values():
                faces = []
                print(i)
        return [(i, sum([vertices[j].z for j in f]) / len(f)) for i, f in enumerate([i for i in val.values() for val in self.__faces.values()  if val == 'face'])]

    def get_face_side(self, face_side):
        return self.__faces.get(face_side)
    
    def get_face(self, face_side):
        return self.__faces.get(face_side).get('face')
    
    def get_face_color(self, face_side):
        return self.__faces.get(face_side).get('color')

    def set_face_color(self, face_side, color):
        self.__faces.get(face_side).update({'color':color})
        
    def get_vertices(self):
        return self.__vertices

    def create_polygon(self, face, vertices):
        # print([(vertices[i].x, vertices[i].y) for i in [*face, face[0]]] )
        return [(vertices[i].x, vertices[i].y) for i in [*face, face[0]]]   
    
class RubiksCube:
    def __init__(self):
        self.cubes = []        
        for origin in STARTING_POSITION:
            cube = Cube(originX=origin[0], originY=origin[1], originZ=origin[2])            
            if (origin[0] == 0):
                cube.set_face_color('front', RED)
            # elif origin[0] == 1 and origin[1] == -1:
            #     cube.set_face_color(BLUE)
            # elif origin[0] == 0 and origin[1] == -1:
            #     cube.set_face_color(YELLOW)
            # elif origin[0] == -1 and origin[1] == 1:
            #     cube.set_face_color(WHITE)   
            # elif origin[0] == 1 and origin[1] == 1:
            #     cube.set_face_color(GREEN)
            # elif origin[0] == 0 and origin[1] == 1:
            #     cube.set_face_color(ORAGNE)                                                                             

            cube.scale((0.5, 0.5, 0.5))
            cube.translate(origin)
            self.cubes.append(cube)
    
              
          
          
          

    
     



    