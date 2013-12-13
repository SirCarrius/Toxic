import json
import itertools

from time import time
from pprint import pprint
from src.SemanticString import SemanticString
from nltk.corpus import wordnet
from termcolor import colored 

filename = './data/semantic-distance-database.json'
READ = 'rb'
WRITE = 'wb'
APPEND = 'a+'
db = json.load(open(filename,READ))

strings = ["Colorless green ideas sleep furiously.","I like drug stores."]
start = time()



print('/----------------Beginning test ------------\\')

for one in strings:
	for two in strings:

		d1 = SemanticString(one,db)
		d2 = SemanticString(two,db)

		print '|%s|'%(repr(d1))
		print '|%s|'%(repr(d2))

		print '|Semantic distance between them: %.04f |'%(d1-d2)

print '---'
json.dump(db,open(filename,WRITE))	
print '|Duration %.04f s|'%(time()-start)
print('\----------------Finished test ------------/')

