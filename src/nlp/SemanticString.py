import itertools
import string
import re

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
	def __init__(self, text,db): #constructor
		self.text = text
		self.db=db #if it's emoticon use EMT if not use pos_tag
		self.tokens = [sw.SemanticWord(token,part_of_speech,self.db) #pos_tag: creates a tuple (token, part_of_speech)
						for token, part_of_speech in pos_tag_expand(word_tokenize_expand(text))#tokenize: breaks the sentence down into a list of words
						#if token not in punctuation and token not in stopwords and token not in emoticons				
						#for token, EMO in pos_tag(word_tokenize(text))
						#if token in emoticons and if not any([token in lst for lst in [punctuation,stopwords,emoticons]])] #how do you tell if punctuations are not emoticons. "..." WE CARE	
		self.tokens = filter(lambda token: not token.orphan,self.tokens)

		self.synsets = [token.synset for token in self.tokens]
		
	def pos_tag_expand(aList):
	  return [for pos_tag(token) if token not in emoticons else (token 'EMT') for token in aList]
		 
	def word_tokenize_expand(comment):
	  #wordList = re.split('(\W+)', comment)#I think this does the job of word_tokenize...
	  #remove whitespace within the string and between the strings
	  #wordList = filter(None, wordList)
	  #wordList = [s.strip() for s in wordList]
	   
	  #this splits the sentence, remove empty strings to a certain extent 
	  #removes whitespace in the strings
	  #doesn't really remove the whitespace that is its own element
	  #but hey whitespace as its own element, or empty strings aren't words/emoticons. they will be ignored.
	  #removing whitespace inside the words/emoticons make sure that we can always match something
	  return wordList = [s.strip() for s in filter(None,re.split('(\W+)', comment))]
	  
	  
	  #re.split('(\W+)', '...words, words...') output:['', '...', 'words', ', ', 'words', '...', '']
      #above statement thinks space is its own element of the list
	  
	  
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