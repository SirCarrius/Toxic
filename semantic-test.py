import json
from time import time

filename = 'semantic-distance-database.json'
READ = 'rb'
WRITE = 'wb'
db = json.load(open(filename,READ))

from SemanticString import SemanticString
from nltk.corpus import wordnet

test_string = "Colorless green ideas sleep furiously."
other_string = "I like drug stores."
start = time()
#Drop down to testing Semantic Word
d1 = SemanticString(test_string,db)
d2 = SemanticString(other_string,db)

print d1-d2
json.dump(db,open(filename,WRITE))	
print time()-start