import pygame, sys

sys.path.append("C:\\Users\\Admin\\Documents\\Code Night\\Code-Night\\New Boot Goffin\\Rubiks Solver\\backend")

for i in sys.path:
    print(i)
    
from rubiks_helper import * 
from rubiks_cube import RubiksCube

class Environment:
    def __init__(self, cubes, fov, distance):
        self.cubes = cubes
        self.fov = fov
        self.distance = distance 
        self.euler_angles = [0, 0, 0]

    def transform_vertices(self, vertices, width, height):
        transformed_vertices = vertices
        axis_list = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        for angle, axis in reversed(list(zip(list(self.euler_angles), axis_list))):
            transformed_vertices = rotate_vertices(transformed_vertices, angle, axis)
        transformed_vertices = project_vertices(transformed_vertices, width, height, self.fov, self.distance)
        return transformed_vertices

    def draw(self, surface):
        
        polygons = []
        for cube in self.cubes:
            transformed_vertices = self.transform_vertices(cube.get_vertices(), *surface.get_size())
            avg_z = cube.calculate_average_z(transformed_vertices)
            for z in avg_z:
                pointlist = cube.create_polygon(cube.get_face(z[0]), transformed_vertices)
                polygons.append((pointlist, z[1], cube))


        for poly in sorted(polygons, key=lambda x: x[1], reverse=True):
            pygame.draw.polygon(surface, poly[2].get_face_color(0), poly[0])
            pygame.draw.polygon(surface, (0, 0, 0), poly[0], 3)
            
rubiks_cube1 = RubiksCube()
scene = Environment(rubiks_cube1.cubes, 90, 5)

pygame.init()
window = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    scene.draw(window)
    mouse_clicked = pygame.event.get()
    # scene.euler_angles[1] += 0.2
    scene.euler_angles[0] += 0.3
    
    pygame.display.flip()

pygame.quit()      