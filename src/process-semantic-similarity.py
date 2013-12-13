import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

rcParams['text.usetex'] = True

filename = 'similarity-matrix.tsv'
delimiter = '\t'

data = np.loadtxt(filename,delimiter=delimiter)

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(np.sort(data,axis=1),interpolation='nearest',aspect='auto')
ax.set_ylabel(r'\Large \textbf{Comment}')
ax.set_xlabel(r'\Large \textbf{Comment}')
plt.colorbar(cax)
plt.tight_layout()
plt.show()

