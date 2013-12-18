import json, os

from api.Twitter import Twitter
from nlp import SemanticDistance as SD
from nlp.json_to_text import TwitterRecord

keywords = ['bob']
trigger = '-'.join(keywords)

query_records = [filename for filename in os.listdir('../data') if not filename.endswith('txt') and trigger in filename]
text_records = [filename for filename in os.listdir('../data') if filename.endswith('txt') and trigger in filename]

#Acquire data from Twitter (here can generalize to other social media platform)
#Better to put these notifications within each class?
if not any([trigger in record for record in query_records]):
	print '------------------'
	print 'No local copies of query results. Asking Twitter.'
	
	query = Twitter(keywords)
	print 'Query finished.'
	print '------------------'
else:
	print 'Found a local copy of Twitter query for %s'%(trigger)

#Extract text from Twitter (to pass it to SemanticWord
if not any([trigger in record for record in text_records]):
	print '------------------'
	print 'Text not extracted from Twitter query. Extracing text.'
	TwitterRecord(keywords)
	print 'Text extracted.'
	print '------------------'
else:
	print 'Text already extracted for %s'%(trigger)

#Calculate semantic distance
corpus_name = '../data/%s.txt'%(trigger)
SD.SemanticDistance(corpus_name)

#Visualize results