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
	for j in xrange(len(corpus)):
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
print time()-start

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(similarity, interpolation = 'nearest', aspect='auto')
plt.colorbar(cax)
plt.tight_layout()
plt.show()
