import plyfile
import numpy as np


# BEGIN generic things
def open_plyfile(filename):
    plydata = plyfile.PlyData.read(filename)
    return plydata

def ipv_plot(plydata, sample_frac=1, **kwargs):
    import ipyvolume
    
    if sample_frac < 1:
        sample = np.random.choice(plydata['vertex'].count, int(sample_frac * plydata['vertex'].count), replace=False)
        print("sample size:", int(sample_frac * plydata['vertex'].count), "out of total", plydata['vertex'].count)
        xyz = dict(x=plydata['vertex']['x'][sample], y=plydata['vertex']['y'][sample], z=plydata['vertex']['z'][sample])
    else:
        xyz = dict(x=plydata['vertex']['x'], y=plydata['vertex']['y'], z=plydata['vertex']['z'])
    ipyvolume.scatter(**xyz, **kwargs)
    ipyvolume.show()


def pptk_plot(plydata, **kwargs):
    import pptk
    
    pptk.viewer(np.array([plydata['vertex']['x'], plydata['vertex']['y'], plydata['vertex']['z']]).T)

# END generic things



# BEGIN really specific to example dataset used for exploration
def load_example_cube():
    plydata = open_plyfile('cube.ply')

    return plydata

def load_example():
    plydata = open_plyfile('ObjID126.ply')

    return plydata

def load_example_full():
    plydata = open_plyfile('ObjID126.full.ply')

    return plydata

# END really specific to example dataset used for exploration
