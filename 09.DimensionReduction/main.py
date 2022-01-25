import math

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def draw(colors,title):
    for i in range(17):
        hex_color = '#%02x%02x%02x' % (
            colors[i][0],colors[i][1],colors[i][2]
        )
        if math.isnan(fast_map_data[1][i])  or math.isnan(fast_map_data[1][i]):
            break
        print(hex_color)
        plt.scatter(fast_map_data[0][i],fast_map_data[1][i], c=hex_color)
    plt.title(title)
    plt.show()



def getColorArray(arr,max, min):
    colors = []
    diff = int(max) - int(min)
    for p in arr:
        res = (p - min) / diff
        try:
            R = int(255*res)
            B = int(255* (1-res))
            colors.append([R,0,0])
        except:
            colors.append([0,0,0])

    return colors

TITLES = ["Rok narodenia", "Pohlavie", "Dosiahnuty level vzdelania", "Počet rokov praxe", "Kolko zaraba"]
data = pd.read_csv('data2.txt', sep=";", header=None)
fast_map_data = pd.read_csv('reduced.txt', sep=";", header=None)

print(data[0])
print(data[1])

for i in range(len(TITLES)):
    max = np.max(data[i])
    min = np.min(data[i])
    colors = getColorArray(data[i],max, min)
    draw(colors, TITLES[i])
