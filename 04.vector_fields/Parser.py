from dataclasses import dataclass

import numpy as np
import yaml


def meta_constructor(loader, node):
    return loader.construct_mapping(node)


yaml.add_constructor(u'tag:yaml.org,2002:opencv-matrix', meta_constructor)


def create_path(index):
    if (index < 10):
        return "0000" + str(index)
    elif index < 100:
        return "000" + str(index)
    else:
        return "00" + str(index)


def crate_matrix_from_files(file_index):
    file_name = "flow_field/u" + create_path(file_index) + ".yml"
    print(file_name)

    # Read YAML file
    with open(file_name, 'r') as stream:
        data_loaded = yaml.load(stream, Loader=yaml.Loader)
    data = data_loaded['flow']['data']

    matrix = []
    for i in range(256):
        matrix.append([])
        for j in range(0,512,2):
            x = data[i * 512 + j]
            y = data[i * 512 + j + 1]
            matrix[i].append([x,y])
    return matrix

def repair_yaml_files():
    file_index = 0

    while file_index < 1000:
        file_name = "flow_field/u" + create_path(file_index) + ".yml"
        # print(file_name)

        # Read YAML file
        with open(file_name, 'r') as stream:
            data = stream.readlines()
        data[0] = data[0].replace(":", " ")
        # data[2] = data[2].replace("!!opencv-matrix"," ")

        with open(file_name, 'w') as stream:
            for line in data:
                stream.write(line)

        file_index += 1
