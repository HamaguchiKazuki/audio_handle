import numpy as np
import matplotlib.pyplot as plt
import cis

t = np.arange(0,1,1/8000)
a = 0.8
f = 440
y = a*np.sin(2*np.pi*f*t)
cis.audioplay(y,8000)