import SemanticWord as sw
import numpy as np

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from itertools import izip_longest,product

class SemanticString(object):
	def __init__(self, string):
		self.tokens = [sw.SemanticWord(token,part_of_speech) for token,part_of_speech in pos_tag(word_tokenize(string))]
	
	def __len__(self):
		return len(filter(None,self.synsets)) if len(filter(None,self.synsets)) > 0 else None

	def __sub__(self,other):
		return np.average(filter(None,[one-two for one,two in itertools.product(self.tokens,other.tokens)]))