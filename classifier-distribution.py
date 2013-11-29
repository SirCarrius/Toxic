import json
import matplotlib.pyplot as plt

from pprint import pprint
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D

rcParams['text.usetex'] = True

filename = 'validation-results.json'

format = lambda str: r'\Large \textbf{%s}'%str
READ = 'r'
y,n,m = zip(*[(x['yes'],x['no'],x['maybe']) 
 		for x in json.load(open(filename,READ)).itervalues()])

def adjust_spines(ax,spines=['left','bottom']):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward',10)) # outward by 10 points
            spine.set_smart_bounds(True)
        else:
            spine.set_color('none') # don't draw spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        # no yaxis ticks
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])

data = {'yes':y,'no':n,'maybe':m}
labels = ['yes','no','maybe']
fig,axs = plt.subplots(nrows=3,ncols=3, sharex=True,sharey=True)
for i in range(len(axs)):
	for j in range(len(axs[0])):
		axs[i,j].scatter(data[labels[i]],data[labels[(j+i*3)%3]])
		adjust_spines(axs[i,j])
		axs[i,j].set_xlabel(format(labels[i]))
		axs[i,j].set_ylabel(format(labels[(j+i*3)%3]))
		plt.tight_layout()
plt.show()