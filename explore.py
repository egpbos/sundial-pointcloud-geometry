import numpy as np
import logging
# data formats
import plyfile
import pandas as pd
import vaex as vx

logger = logging.getLogger('sundial-pointcloud-geometry.explore')
logger.setLevel(logging.DEBUG)


# BEGIN generic things
def open_plyfile(filename):
    plydata = plyfile.PlyData.read(filename)
    return plydata


def vertex_dict_from_plyfile(filename):
    plydata = open_plyfile(filename)
    xyz = dict(x=plydata['vertex']['x'], y=plydata['vertex']['y'], z=plydata['vertex']['z'])
    return xyz


def pandas_vertices_from_plyfile(filename):
    xyz = vertex_dict_from_plyfile(filename)
    return pd.DataFrame(xyz)


def vaex_vertices_from_plyfile(filename):
    xyz = vertex_dict_from_plyfile(filename)
    return vx.from_dict(xyz)


# END generic things


# BEGIN really specific to example dataset used for exploration
def load_example_cube():
    plydata = open_plyfile('data/cube.ply')

    return plydata


def load_example():
    plydata = open_plyfile('data/ObjID126.ply')

    return plydata


def load_example_full():
    plydata = open_plyfile('data/ObjID126.full.ply')

    return plydata

# END really specific to example dataset used for exploration
