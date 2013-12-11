import itertools
import random 

from SemanticString import SemanticString
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from pprint import pprint
from time import time
from progress.bar import Bar

import matplotlib.pyplot as plt
import numpy as np

fname = "positive-control_.txt"
with open(fname) as f:
	db = [string.strip() 
			for string in f.readlines()[0].split(',')]

corpus = db#random.sample(db,40)
similarity = np.zeros((len(corpus),len(corpus)))

#TODO filter out words with low tf-idf

start = time()
bar = Bar('Calulating semantic distance', max=len(corpus)*(len(corpus)+1)/2)
for i in xrange(len(corpus)):
	for j in xrange(i):

 		similarity[i,j] = SemanticString(corpus[i]) - SemanticString(corpus[j])

 		bar.next()
	bar.next()
bar.finish()

M = similarity
M += similarity.transpose()
M[np.diag_indices(len(corpus))] = 1
np.savetxt('similarity-matrix.tsv',M,fmt='%.04f',delimiter='\t')
print time()-start

fig,(dist,ax) = plt.subplots(nrows=1,ncols=2)
cax = ax.imshow(np.sort(M,axis=0), interpolation = 'nearest', aspect='auto', vmin=0,vmax=1)
plt.colorbar(cax)
dist.hist(np.ravel(similarity[similarity!=0]),bins=200,histtype='step',color='k', cumulative=True, range=(0,1))
plt.tight_layout()
plt.show()
