import logging
from ectopylasm import load_plyfile

logger = logging.getLogger('sundial-pointcloud-geometry.explore')
logger.setLevel(logging.DEBUG)


# BEGIN generic things


# END generic things


# BEGIN really specific to example dataset used for exploration
def load_example_cube():
    plydata = load_plyfile('data/cube.ply')

    return plydata


def load_example():
    plydata = load_plyfile('data/ObjID126.ply')

    return plydata


def load_example_full():
    plydata = load_plyfile('data/ObjID126.full.ply')

    return plydata

# END really specific to example dataset used for exploration
