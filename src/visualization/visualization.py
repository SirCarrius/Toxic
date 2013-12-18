import matplotlib.pyplot as plt

		fig,(dist,ax) = plt.subplots(nrows=1,ncols=2)
		cax = ax.imshow(np.sort(M,axis=0), interpolation = 'nearest', aspect='auto', vmin=0,vmax=1)
		plt.colorbar(cax)
		dist.hist(np.ravel(similarity[similarity!=0]),bins=200,histtype='step',color='k', cumulative=True, range=(0,1))
		plt.tight_layout()
		plt.show()
