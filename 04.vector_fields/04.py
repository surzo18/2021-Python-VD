"""
Čtvrté cvičení se věnuje vizualizaci vektorových polí.
Pokuste se o animaci vizualizace časoprostorových vzorků vektorového pole ze simulace proudění tekutin.
Vstupní data naleznete ZDE. Výsledná animace by měla obsahovat vhodné znázornění rotace a rychlosti vektorového pole,
trajektorie částic (proudnice) a mohla by vypadat třeba takto.
"""
import random

import numpy as np
from matplotlib import pyplot as plt
import Parser as parser
from Point import Point
import cv2


"""
Generate random points with random X,Y
"""
def generate_random_points(count):
    points = []
    for i in range(count):
        points.append(Point(random.random() * CANVAS_SIZE, random.random() * CANVAS_SIZE))
    return points

"""
Return index of red point from array of points
"""
def choose_red_point_index_from_points(points):
    for i in range(len(points)):
        if(points[i].x >180 and points[i].x <200 and points[i].y > 50 and points[i].y <60):
            return i
    #Ak nie je vyhovujuci bod
    points[len(points)-1].x = 181
    points[len(points)-1].y = 51
    return len(points) - 1

def rot(matrix, i,j):
    if i == 0 or i == 255:
        return 0
    elif j == 0 or j == 255:
        return 0

    frac1 = matrix[i][j+1][1] - matrix[i][j-1][1]
    frac2 = matrix[i+1][j][0] - matrix[i-1][j][0]
    return frac1/2-frac2/2







CANVAS_SIZE = 256
NUMBER_OF_GENERATED_POINTS = 300
CMAP = 'hot'

points = generate_random_points(NUMBER_OF_GENERATED_POINTS)
red_point_index = choose_red_point_index_from_points(points)
red_point_history = []

plt.ion()

for time in range(000,1000,1):
    print("Current timeframe " + "{:05d}".format(time))
    file_open = cv2.FileStorage("./flow_field/u" + "{:05d}".format(time) + ".yml", cv2.FILE_STORAGE_READ)
    file_node: int = file_open.getNode("flow")
    vector_mat = file_node.mat()


    map =[]
    for i in range(256):
        map.append([])
        for j in range(256):
            color = rot(vector_mat,j, i)
            map[i].append(color)

    plt.figure(3)
    plt.imshow(map, cmap=CMAP, interpolation='nearest')
    plt.colorbar()

    #update points
    for p in points:
        p.move([vector_mat[round(p.x),round(p.y)][1],vector_mat[round(p.x),round(p.y)][0]])

    # Draw red point
    for rp in red_point_history:
        plt.scatter(rp[0], rp[1], color="red", s=1)

    # Cycle through every point and draw it
    for point in points:
        if (points[red_point_index] == point):
            plt.scatter(point.x, point.y, color="red", s=1)
            red_point_history.append([point.x, point.y])
        else:
            plt.scatter(point.x, point.y, color="black", s=1)

    plt.draw()
    plt.pause(0.1)
    plt.clf()

"""

# Update frame
matrix = parser.crate_matrix_from_files(0)

def animate(s):
    #Update frame
    matrix = parser.crate_matrix_from_files(s)

    #Draw bgr
    for i in range(1,255):
        for j in range(1, 255):
            color = rot(matrix,i,j)
            if color < 0:
                color = 0
            if color > 255:
                color = 255
            plt.scatter(i,j,color=(color, 0.0, 0.0))

    for p in points:
        if p.x > 255 or p.y >255:
            continue
        p.x += matrix[round(p.x)][round(p.y)][0]
        p.y += matrix[round(p.x)][round(p.y)][1]

    #Draw red point
    for rp in red_point_history:
        plt.scatter(rp[0], rp[1], color="red", s=1)

    #Draw points
    for point in points:
        if (points[red_point_index] == point):
            plt.scatter(point.x, point.y, color="red", s=1)
            red_point_history.append([point.x,point.y])
        else:
            plt.scatter(point.x, point.y, color="black", s=1)

#ani = FuncAnimation(fig, animate, frames=1000, interval=100, repeat=False)


# Draw bgr
for i in range(200, 255):
    for j in range(200, 255):
        color = rot( i, j)
        if color < 0:
            color = 0
        if color > 255:
            color = 255
        plt.scatter(i, j, c=[color, 0.0, 0.0],s=1)


fig = plt.figure(1)
plt.title("Vector Fields")
plt.xlabel("x")
plt.ylabel("y")

plt.show()


#parser.repair_yaml_files()
"""
