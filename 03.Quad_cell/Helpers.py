from datetime import datetime
from random import random

import numpy

from Point import Point
from Quad import Quad

DEFORMATION_INDEX = 0.2


def cstrandom():
    # Generate random value between -0.5 and +0.5
    # Then multiply for deformation
    return (random() - 0.5) * DEFORMATION_INDEX


def generate_points_for_quads(size):
    points = []
    for x in range(size):
        for y in range(size):
            point = Point(float(x) + cstrandom(), float(y) + cstrandom())
            points.append(point)

    return points


def generate_quads(points, size):
    quads = []

    for x in range(0, size - 1, 1):
        for y in range(0, size - 1, 1):
            p1 = points[x * size + y]  # LEFT TOP CORNER
            p2 = points[x * size + y + 1]  # RIGHT TOP CORNER
            p3 = points[(x + 1) * size + y + 1]  # LEFT BOTTTOM CORNER
            p4 = points[(x + 1) * size + y]  # RIGHT BOTTOM CORNER
            quads.append(Quad([p1, p2, p3, p4]))
    return quads


def generateGridPoints(size=10, step=0.1):
    points = []

    y = 0.0
    while y <= size - 1:
        x = 0.0
        while x <= size - 1:
            points.append(Point(x, y))
            x += step
        y += step
    return points


def test_function_time(function, description):
    a = datetime.datetime.now()
    function()
    b = datetime.datetime.now()
    c = b - a
    return c


def newtonMetod(p: Point, quad: Quad) -> Point:
    r = 0.5
    s = 0.5

    iter = 0
    while iter < 20:
        iter += 1

        T_rs = T_quad(r, s, quad)
        J = J_matrix(r, s, quad)
        J_inv = numpy.linalg.inv(J)

        nextSolution = (r, s) - (J_inv @ (T_rs - p).to_array())

        r = nextSolution[0]
        s = nextSolution[1]

    return Point(r, s)


def T_quad(r: float, s: float, quad: Quad) -> Point:
    return (quad.p1 * (1.0 - r) + quad.p2 * r) * (1.0 - s) + (quad.p3 * r + quad.p4 * (1.0 - r)) * s


def J_matrix(r: float, s: float, quad: Quad) -> Point:
    #				(s - 1.0) * (quad.p1 - quad.p2) + s * (quad.p3 - quad.p4)
    diffR = (quad.p1 - quad.p2) * (s - 1.0) + (quad.p3 - quad.p4) * s
    diffS = (quad.p1 - quad.p4) * (r - 1.0) + (quad.p3 - quad.p2) * r

    return numpy.array([
        [diffR.x, diffS.x],
        [diffR.y, diffS.y],
    ])


def sinCos(p: Point) -> float:
    return numpy.sin(p.x) + numpy.cos(p.y)
