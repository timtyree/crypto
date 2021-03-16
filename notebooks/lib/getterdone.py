# automate the boring stuff
import time, os, sys, re
import dask.bag as db
beep = lambda x: os.system("echo -n '\\a';sleep 0.2;" * x)
if not 'nb_dir' in globals():
    nb_dir = os.getcwd()

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import animation
from IPython.display import HTML
from sklearn.datasets import load_digits
from umap import UMAP
import seaborn as sns
import itertools
sns.set(style='white', rc={'figure.figsize':(14, 12), 'animation.html': 'html5'})

# ignore user warnings
import warnings
warnings.simplefilter('ignore', UserWarning)

# import lib
from lib import *