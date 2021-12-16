import torch
import numpy as np
from skimage.io import imread, imsave
import glob
import pdb

files = sorted(glob.glob('storage/*.tif'))
print(files)
files = [f.split('/')[-1][:10] for f in files]
files = np.array(files)
files = list(np.unique(files))

N = len(files)
print('Found %d images'%N)
print(files[:10])

for f in files:
    imgs = sorted(glob.glob('storage/'+f+'*'))
    mc_img = []
    for img in imgs:
        mc_img.append(imread(img))
    mc_img = np.array(mc_img)
    mc_img = mc_img.T.swapaxes(0,1)
    pdb.set_trace()
    imsave(f+'.tif',mc_img)
