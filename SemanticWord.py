import itertools

import numpy as np

from nltk.corpus import wordnet

morphy_tag = {'NN':wordnet.NOUN,'JJ':wordnet.ADJ,'VB':wordnet.VERB,'RB':wordnet.ADV}
listify = lambda item: item if type(item) == type([]) else list(item)

class SemanticWord(object):

	def __init__(self,word,part_of_speech):
		self.word = word
		self.part_of_speech = part_of_speech

		self.synset = listify(wordnet.synsets(word,pos=morphy_tag[part_of_speech] if part_of_speech in morphy_tag else wordnet.NOUN))

		self.orphan = not self.synset 

	def __sub__(self,other):
		if self.synset and other.synset:
			return 1-np.average([one.path_similarity(two) for one,two in itertools.combinations(one.synset + two.synset,2)])  
		else:
			return None
