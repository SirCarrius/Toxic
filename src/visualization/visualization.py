import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['text.usetex'] = True


class SemanticVisualization(object):

	def __init__(self,trigger, delimiter = '\t'):
		self.trigger = trigger
		self.filename = '/Volumes/My Book/Toxic/data/%s.similarity-matrix-tsv'%(trigger)
		#again with the dangerous path constructions	
		self.delimiter = delimiter

		self.data = np.loadtxt(self.filename,delimiter=self.delimiter, dtype='str')

	def heatmap(self,ax=None, show=False,savename=None):

		if not ax:
			fig = plt.figure()
			ax = fig.add_subplot(111)

		cax = ax.imshow(self.data,interpolation='nearest',aspect='auto')
		ax.set_ylabel(r'\Large \textbf{Comment}')
		ax.set_xlabel(r'\Large \textbf{Comment}')
		ax.set_title(r'\Large \textbf{Similarity of tweets about %s}'%self.trigger)
		plt.colorbar(cax)
		plt.tight_layout()
		if savename:
			plt.savefig('%.png'%savename,dpi=200)
		if show:
			plt.show()

x = SemanticVisualization(trigger='alcohol')
x.heatmap(show=True)