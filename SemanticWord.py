import itertools
import string

import numpy as np

from nltk.corpus import wordnet
from pprint import pformat
from termcolor import colored

morphy_tag = {'NN':wordnet.NOUN,'JJ':wordnet.ADJ,'VB':wordnet.VERB,'RB':wordnet.ADV}
listify = lambda item: item if type(item) == type([]) and item != None else list(item)

class SemanticWord(object):

	def __init__(self,word,part_of_speech):
		self.word = wordnet.morphy(word) #Lemmatization
		self.part_of_speech = morphy_tag[part_of_speech] if part_of_speech in morphy_tag else wordnet.NOUN
		self.synset = listify(wordnet.synsets(word)) if self.word else None
		self.orphan = not self.synset

	def __sub__(self,other):
		if self.synset and other.synset:
			similarities = filter(None,[one.path_similarity(two) for one in self.synset for two in other.synset])  
			return 1-np.average(similarities) if similarities != [] else None
		else:
			return None

	def __repr__(self):
		return 'word: %s \n sense: %s'%(self.word,pformat(self.synset) if not self.orphan else 'Not in WordNet')
