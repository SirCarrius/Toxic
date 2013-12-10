import itertools
import string

import SemanticWord as sw
import numpy as np

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from pprint import pprint
from termcolor import colored

punctuation = set(string.punctuation) #Can make more efficient with a translator table

class SemanticString(object):
	def __init__(self, text,db):
		self.text = text
		self.db = db
		self.tokens = [sw.SemanticWord(token,part_of_speech,self.db) 
						for token,part_of_speech in pos_tag(word_tokenize(text))
						if token not in punctuation]			
		self.tokens = filter(lambda token: not token.orphan,self.tokens)

		self.synsets = [token.synset for token in self.tokens]
	def __len__(self):
		return len(filter(None,self.synsets)) if len(filter(None,self.synsets)) > 0 else None

	def __sub__(self,other):
		similarities = np.array(filter(None,[self.tokens[i] - other.tokens[j] 
							for i in xrange(len(self.tokens)) for j in xrange(len(other.tokens))]))
		similarities = similarities[~np.isnan(similarities)]
		return np.average(similarities) if similarities != [] else None

	def __repr__(self):
		return  '%s--> %s'%(colored(self.text,'red'),colored(' '.join([token.word for token in self.tokens]),'green')) +'\n'+'\n'.join([repr(token) for token in self.tokens])