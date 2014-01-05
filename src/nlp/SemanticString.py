import itertools
import string

import SemanticWord as sw
import numpy as np

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from pprint import pprint
from termcolor import colored

READ = 'rb'
stopwords = open('../data/stopwords',READ).readlines()

punctuation = set(string.punctuation) #Can make more efficient with a translator table

#create a list of emoticons
CLASSIFIER = 'txt'
emoticons = open('../data/emoticons', CLASSIFIER).readlines()
EMO = 'emt'
#regular expression: a group of punctuations containing no alphetical or numerical value
#use regular expressions to pick out emoticons
#might want to take out "if not in punctuation"
class SemanticString(object):
	def __init__(self, text,db):
		self.text = text
		self.db=db #if it's emoticon use EMT if not use pos_tag
		self.tokens = [sw.SemanticWord(token,part_of_speech,self.db) #pos_tag: creates a tuple (token, part_of_speech)
						for token,part_of_speech in pos_tag(word_tokenize(text))#tokenize: breaks the sentence down into a list of words
						if token not in punctuation and token not in stopwords and token not in emoticons						
						for token, EMO in pos_tag(word_tokenize(text))
						if token in emoticons and not in punctuation and token not in stopwords] #how do you tell if punctuations are not emoticons. "..." WE CARE	
		self.tokens = filter(lambda token: not token.orphan,self.tokens)

		self.synsets = [token.synset for token in self.tokens]
	def __len__(self):
		return len(filter(None,self.synsets)) if len(filter(None,self.synsets)) > 0 else None

	def __sub__(self,other):
		if self.text == other.text:
			return 0
		else:
			similarities = np.array(filter(None,[self.tokens[i] - other.tokens[j] 
								for i in xrange(len(self.tokens)) for j in xrange(len(other.tokens))]))
			similarities = similarities[~np.isnan(similarities)]
		return 1-np.average(similarities) if similarities != [] else None

	def __repr__(self):
		return  '%s--> %s'%(colored(self.text,'red'),colored(' '.join([token.word for token in self.tokens]),'green'))