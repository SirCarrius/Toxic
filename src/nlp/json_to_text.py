from __future__ import unicode_literals

from nltk.corpus import stopwords

import json, os

class TwitterRecord(object):
	def __init__(self,keywords):
		self.trigger = '-'.join(keywords)
		self.filenames = [filename for filename in os.listdir('../data/') 
			if self.trigger in filename and not filename.endswith('txt')]
		
		for filename in self.filenames:
			json.load(open('../data/%s'%filename,'rb'))

		self.tweets = [tweet['text'] for tweet in json.load(open('../data/%s'%(filename),'rb')) 
				for filename in self.filenames]

		self.textname = '../data/%s.txt'%(self.trigger)
		with open(self.textname,'wb') as f:
			for tweet in map(lambda tweet: tweet.encode('utf-8'),self.tweets):
				print>>f,tweet

'''
Can't regularlize here because WordNet lookup works better with a Part-of-Speech tag. 
This means that the text file that SemanticDistance accesses must have the entire tweet.
'''