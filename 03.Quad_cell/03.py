import numpy
import shapely
from matplotlib import pyplot as plt
from shapely.geometry.polygon import Polygon
from Point import Point
import Helpers as h


CANVAS_SIZE = 10
STEP = 0.1
PIXEL_PER_ROW = int(CANVAS_SIZE/STEP)

plt.figure(1)


#Generate points
squad_points = h.generate_points_for_quads(CANVAS_SIZE)

# GENERATE QUADS
quads = h.generate_quads(squad_points, CANVAS_SIZE)

# Plot quads grid
for quad in quads:
    xs = []
    ys = []
    for p in quad.points:
        xs.append(p.x)
        ys.append(p.y)
    xs.append(xs[0])
    ys.append(ys[0])
    plt.plot(xs, ys, c="black")


#draw points (in graph)
for quad in quads:
    for point in quad.points:
        plt.scatter(point.x, point.y, c="black", s=8)
        pass

#draw grid
pixelGrid = h.generateGridPoints(CANVAS_SIZE, STEP)


rasterized = []
for p in pixelGrid:
    f_lambda = -2.0
    for quad in quads:
        poly = Polygon([quad.p1.to_array(),quad.p2.to_array(),quad.p3.to_array(),quad.p4.to_array()])
        if poly.contains(shapely.geometry.Point(p.x, p.y)):
            r, s = h.newtonMetod(p, quad).to_array()

            # Point P is in polygon "quad"
            # Work the magic
            r, s = h.newtonMetod(p, quad).to_array()

            f_i_1 = h.sinCos(quad.p1)
            f_i_2 = h.sinCos(quad.p2)
            f_i_3 = h.sinCos(quad.p3)
            f_i_4 = h.sinCos(quad.p4)

            phi_1 = (1.0 - r) * (1.0 - s)
            phi_2 = r * (1.0 - s)
            phi_3 = r * s
            phi_4 = (1.0 - r) * s

            f_lambda = (f_i_1 * phi_1) + (f_i_2 * phi_2) + (f_i_3 * phi_3) + (f_i_4 * phi_4)

    rasterized.append(f_lambda)


PIXEL_PER_ROW = numpy.sqrt(len(pixelGrid))
rasterizedMN = []
for y in range(int(PIXEL_PER_ROW)):
    rasterizedMN.append([])
    for x in range(int(PIXEL_PER_ROW)):
        idx = y * PIXEL_PER_ROW + x
        rasterizedMN[y].append(rasterized[int(idx)])

plt.figure(2)
plt.imshow(rasterizedMN, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.show()

