import itertools,json

from SemanticString import SemanticString
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from progress.bar import Bar

import numpy as np

class SemanticDistance(object):

	def __init__(self,path_to_corpus):
		
		self.filenames = {'corpus':path_to_corpus,'database':'../data/semantic-distance-database.json'}
		self.READ = 'rb'
		self.WRITE = 'wb'
		
		self.database = json.load(open(self.filenames['database'],self.READ))

		with open(self.filenames['corpus']) as f:
			self.corpus = [string.strip() for string in f.readlines()]

		self.similarity = np.zeros((len(self.corpus),len(self.corpus)))

		#TODO filter out words with low tf-idf <-- Does this make sense?

		self.bar = Bar('Calulating semantic distance', max=len(self.corpus)*(len(self.corpus)+1)/2)
		for i in xrange(len(self.corpus)):
			for j in xrange(i):

		 		self.similarity[i,j] = SemanticString(self.corpus[i],self.database) - SemanticString(self.corpus[j],self.database)

		 		self.bar.next()
			self.bar.next()
		self.bar.finish()

		json.dump(self.database,open(self.filenames['database'],self.WRITE))	

		self.M = self.similarity
		self.M += self.similarity.transpose()
		self.M[np.diag_indices(len(self.corpus))] = 1
		np.savetxt('%s.similarity-matrix-tsv'%(self.filenames['corpus'].rstrip('.txt')),self.M,fmt='%.04f',delimiter='\t')
