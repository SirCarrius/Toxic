import itertools
import string
import json

import numpy as np

from nltk.corpus import wordnet
from pprint import pformat
from termcolor import colored

morphy_tag = {'NN':wordnet.NOUN,'JJ':wordnet.ADJ,'VB':wordnet.VERB,'RB':wordnet.ADV}
listify = lambda item: item if type(item) == type([]) and item != None else list(item)

filename = 'semantic-distance-database.json'
READ = 'rb'
WRITE = 'wb'
db = json.load(open(filename,READ))

def lookup(one_sense,another_sense):
	#construct query
	queries =  ['%s-%s'%(one_sense.word,another_sense.word),'%s-%s'%(another_sense.word,one_sense.word)]
	if not any([query in db for query in queries]):
		similarity = np.average(filter(None,[a.path_similarity(b) 
					for a,b in itertools.combinations(one_sense.synset+another_sense.synset,2)]))
		distance = 1-similarity if similarity else None #But now None means both no distance and not found
		db[query] = distance
	return db[query]
		

class SemanticWord(object):

	def __init__(self,word,part_of_speech):
		self.word = wordnet.morphy(word) #Lemmatization
		self.part_of_speech = morphy_tag[part_of_speech] if part_of_speech in morphy_tag else wordnet.NOUN
		self.synset = listify(wordnet.synsets(word)) if self.word else None
		self.orphan = not self.synset

	def __sub__(self,other):
		if self.synset and other.synset: 
			return 0 if self.word == other.word else lookup(self,other)
		else:
			return None

	def __repr__(self):
		return 'word: %s \n sense: %s'%(self.word,pformat(self.synset) if not self.orphan else 'Not in WordNet')

json.dump(db,open(filename,WRITE))