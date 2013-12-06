import itertools

from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from pprint import pprint
from time import time

import matplotlib.pyplot as plt
import numpy as np

fname = "positive-control_.txt"
with open(fname) as f:
	corpus = [string.strip() 
			for string in f.readlines()[0].split(',')]

#corpus = corpus[:100]
similarity = np.zeros((len(corpus),len(corpus)))
#TODO filter out stop words
#TODO filter out words with low tf-idf

start = time()
morphy_tag = {'NN':wordnet.NOUN,'JJ':wordnet.ADJ,'VB':wordnet.VERB,'RB':wordnet.ADV}
listify = lambda item: item if type(item) is type([]) else list(item)
for i in xrange(len(corpus)):
 	print i/float(len(corpus))
 	if i/float(len(corpus))%0.1 == 0:
 		print chr(27) + "[2J"
	for j in xrange(i):
	 	s = 0
	 	for one in pos_tag(word_tokenize(corpus[i])):
	 		for two in pos_tag(word_tokenize(corpus[j])):
	 			#First item of tuple is word, second is part of speech
	 			if one[0] == two[0]:
	 				sim = 1
	 			else:
	 				sim = 0
		 			synsets = {}
		 			synsets['one'] = listify(wordnet.synsets(one[0],pos=morphy_tag[one[1]] if one[1] in morphy_tag else wordnet.NOUN))
		 			synsets['two'] = listify(wordnet.synsets(two[0],pos=morphy_tag[two[1]] if two[1] in morphy_tag else wordnet.NOUN))
		 			if len(synsets['one'])>0 and len(synsets['two'])>0:
		 				tmp = 0
			 			for a,b in itertools.product(synsets['one'],synsets['two']):
			 				tmp += a.path_similarity(b) if a.path_similarity(b) else 0
		 				tmp /= float(sum(map(len,synsets.items())))
		 				sim += tmp
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
