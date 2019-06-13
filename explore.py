import numpy as np
import logging
# data formats
import plyfile
import pandas as pd
import vaex as vx
# visualization
import ipyvolume as ipv
import pptk

logger = logging.getLogger('sundial-pointcloud-geometry.explore')
logger.setLevel(logging.DEBUG)


# BEGIN generic things
def open_plyfile(filename):
    plydata = plyfile.PlyData.read(filename)
    return plydata


def random_sample(xyz, total, sample_frac):
    sample = np.random.choice(total, int(sample_frac * total), replace=False)
    logger.debug("sample size:", int(sample_frac * total), "out of total", total)
    return dict(x=xyz['x'][sample], y=xyz['y'][sample], z=xyz['z'][sample])


def ipv_plot_plydata(plydata, sample_frac=1, **kwargs):
    if sample_frac < 1:
        xyz = random_sample(plydata['vertex'], plydata['vertex'].count, sample_frac)
    else:
        xyz = dict(x=plydata['vertex']['x'], y=plydata['vertex']['y'], z=plydata['vertex']['z'])
    ipv.scatter(**xyz, **kwargs)
    ipv.show()


def pptk_plot_plydata(plydata, **kwargs):
    pptk.viewer(np.array([plydata['vertex']['x'], plydata['vertex']['y'], plydata['vertex']['z']]).T)


def ipv_plot_df(df, sample_frac=1, **kwargs):
    if sample_frac < 1:
        xyz = random_sample(df, len(df), sample_frac)
    else:
        xyz = dict(x=df['x'], y=df['y'], z=df['z'])
    ipv.scatter(**xyz, **kwargs)
    ipv.show()


def pptk_plot_df(df, **kwargs):
    pptk.viewer(np.array([df['x'], df['y'], df['z']]).T)


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
