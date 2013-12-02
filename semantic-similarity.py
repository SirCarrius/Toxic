import numpy as np

from nltk.corpus import wordnet
from pprint import pprint
from time import time

import matplotlib.pyplot as plt

fname = "positive-control_.txt"
with open(fname) as f:
	corpus = [string.strip() 
			for string in f.readlines()[0].split(',')]

corpus = corpus[:40]
similarity = np.zeros((len(corpus),len(corpus)))
#Can make this much more efficient
#TODO filter out stop words
#TODO filter out words with low tf-idf
#TODO use optional POS argument

start = time()
for i in xrange(len(corpus)):
	for j in xrange(i):
	 	one = corpus[i].split()
	 	two = corpus[j].split()
	 	s = 0
	 	for first_word in one:
	 		for second_word in two:
	 			if first_word == second_word:
	 				sim = 1
	 			else:
		 			#hack for now
		 			if len(wordnet.synsets(first_word)) > 0 and len(wordnet.synsets(second_word)) > 0 :
			 			first_synset = wordnet.synsets(first_word)[0]
		 				second_synset = wordnet.synsets(second_word)[0]

		 				sim = first_synset.path_similarity(second_synset)
	 				else:
	 					sim = 0
			s += sim if sim else 0
	 	s /= float(len(one)*len(two))
 		similarity[i,j] = s

M = similarity
M += similarity.transpose()
M[np.diag_indices(len(corpus))] = 1
np.savetxt('similarity-matrix.tsv',M,fmt='%.04f',delimiter='\t')
print time()-start

fig,(dist,ax) = plt.subplots(nrows=1,ncols=2)
cax = ax.imshow(M, interpolation = 'nearest', aspect='auto')
plt.colorbar(cax)
dist.hist(np.ravel(similarity[similarity!=0]),bins=200,histtype='step',color='k', cumulative=True)
plt.tight_layout()
plt.show()
