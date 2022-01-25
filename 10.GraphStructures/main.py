import math
from math import sqrt
from random import random
import random
from lxml.etree import PI
from matplotlib import pyplot as plt
from Point import Point

CANVAS_SIZE = 500

def generate_random_points(count):
    points = []
    for i in range(count):
        points.append(Point(random.random() * CANVAS_SIZE, random.random() * CANVAS_SIZE))
    return points

plt.ion()
K = 10
DELTA = 1
T = 1

def getForceA(p1,p2):
    distance = sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    if(distance == 0):
      return [0,0]

    mod = (distance/K**3)
    mod/=10;
    return [mod*(p2.x-p1.x),mod*(p2.y-p1.y),mod,distance]

def getForceR(p1,p2):
    distance = sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    if(distance == 0):
      return [0,0]

    mod = -1 * ((K**2)/(distance**2))
    mod/=100

    return [mod*(p2.x-p1.x),mod*(p2.y-p1.y),mod,distance]

def randn_bm():
    u = 0
    v = 0
    while(u == 0):
        u = random() #Converting [0,1) to (0,1)
    while(v == 0):
        v = random()
    num = sqrt(-2.0 * math.log(u)) * math.cos(2.0 * 3.14 * v);
    num = num / 10.0 + 0.5; # Translate to 0 -> 1
    if (num > 1 or num < 0):
        return randn_bm() # resample between 0 and 1
    return num * CANVAS_SIZE

# Generujem 100 pointov
points = generate_random_points(50)

# Generaovanie hran
relations = []
for i in range(50):
    x = random.randrange(0,50)
    y = random.randrange(0,50)
    relations.append([x,y])

for time in range(000,1000,1):
    #Draw  points
    for p in points:
        plt.scatter(p.x,p.y, c="black", s=1)

    #draw Lines
    for r in relations:
        print(points[r[0]].x)
        plt.plot([points[r[0]].x,points[r[1]].x],[points[r[0]].y,points[r[1]].y], c="black", marker="o")

    #Sila
    forces = []
    for i in range(len(points)):
        force = [0,0]
        for j in range(len(points)):
            nF = getForceR(points[i],points[j])
            force[0] += nF[0]
            force[1] += nF[1]
        forces.append(force)

    for i in range(len(forces)):
        p1 = relations[i][0]
        p2 = relations[i][1]
        nF = getForceA(points[p2],points[p1])

        forces[p1][0] -= nF[0]
        forces[p1][1] -= nF[1]

        forces[p2][0] += nF[0]
        forces[p2][1] += nF[1]


    for i in range(len(forces)):
        force = forces[i]
        df = sqrt(force[0]**2 + force[1]**2)
        #force[0] = (force[0] / df) * min(DELTA, T * df)
        #force[1] = (force[1] / df) * min(DELTA, T * df)

        points[i].x += force[0]
        points[i].y += force[1]

        T -= T * 0.01

    plt.draw()
    plt.pause(0.1)
    plt.clf()