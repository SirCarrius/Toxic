import itertools

from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from pprint import pprint
from time import time
from progress.bar import Bar

import matplotlib.pyplot as plt
import numpy as np

fname = "positive-control_.txt"
with open(fname) as f:
	corpus = [string.strip() 
			for string in f.readlines()[0].split(',')]

corpus = corpus[:10]
similarity = np.zeros((len(corpus),len(corpus)))
#TODO filter out stop words
#TODO filter out words with low tf-idf

def semantic_distance(one,two):
	return 

start = time()
orphan_words = []
bar = Bar('Calulating semantic distance')
for i in xrange(len(corpus)):
	for j in xrange(i):

	 	string_distance = 0
	 	for one in SemanticString(corpus[i]):
	 		for two in SemanticString(corpus[j]):
 				if len(one) and len(two):
	 				
	 				token_distance = filter(None,[a.path_similarity(b) for a,b in itertools.product(one.synsets,two.synsets)])

	 				count = len(token_distance)
	 				token_distance = sum(token_distance)/float(count)

		 			string_distance += token_distance 

				if not len(one):
 					orphan_words.append(one.orphans)
			
				if not len(two):
					orphan_words.append(two.orphans)


	 	string_distance /= 	float(len(one)+len(two))
 		similarity[i,j] = string_distance

 		bar.next()
	bar.next()

bar.finish()
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
